# Serializer là bộ chuyển đổi dữ liệu giữa các định dạng khác nhau
# chuyen doi mot cau truc phuc tap nhu object cua python thanh mot cau truc don gian nhu JSON,...


from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
# from rest_framework.validators import UniqueValidator

from api import models as api_models


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    # Mục đích: Tùy chỉnh JWT token để thêm thông tin user (full_name, email, username)
    # vào payload của token, giúp client có thể truy cập thông tin user mà không cần
    # gọi API bổ sung
    @classmethod
    def get_token(cls, user):
        # Call the parent class's get_token method
        token = super().get_token(user)
        
        # Them tuy chinh cho token 
        token['full_name'] = user.full_name
        token['email'] = user.email
        token['username'] = user.username
        return token

class RegisterSerializer(serializers.ModelSerializer):
    # Mục đích: Xử lý đăng ký user mới với các validation:
    # - Kiểm tra độ mạnh của password
    # - Xác nhận password nhập lại khớp với password ban đầu
    # - Tự động tạo username từ phần đầu của email
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    # write_only=True: tham số này chỉ định rằng trường password chỉ được sử dụng khi tạo (POST) hoặc cập nhật (PUT/PATCH), Password sẽ không bao giờ được trả về trong response API (GET), Đây là một biện pháp bảo mật quan trọng để đảm bảo mật khẩu không bị lộ
    # required=True: Chỉ định rằng trường password là bắt buộc, Nếu không có password khi gửi request, serializer sẽ báo lỗi validation
    # validators=[validate_password]: Nó kiểm tra độ mạnh của mật khẩu theo các tiêu chí mặc định của Django: Độ dài tối thiểu (thường là 8 ký tự), Không được quá giống với thông tin cá nhân của user, Không được quá phổ biến hoặc dễ đoán, Không được chỉ chứa số

    password2 = serializers.CharField(write_only=True, required=True)

    ## Class Meta duoc hieu nhu la 1 lop metadata co the thuc hien cac chuc nang bo sung vi du nhu
    # -Điều chỉnh hiển thị: Đặt tên hiển thị cho model, Sắp xếp dữ liệu
    # -Cấu hình Database:  Đặt tên bảng, Đặt tên trường, Đặt tên cột, tạo các index, thiet lap cac rang buoc (constraints)
    # -Phân quyền: Đặt tên quyền truy cập, thiết lập các quyền truy cập cho các trường dữ liệu
    # -Cau hinh khac: Abstract model, ordering, verbose_name, verbose_name_plural
    class Meta:
        
        # Chi dinh models de co the anh xa den
        model= api_models.User # (special attribute) model khong the thay bang bien khac duoc, bien model la bat buoc, model khong them 's vi trong Django Rest yeu cau thuoc tinh model phai la so it trong class Meta  để xác định model nào sẽ được serialize
        # Xac dinh truong du lieu tu models ma no co the lien quan den trong serializer nay
        fields = ('full_name', 'email',  'password', 'password2') # (special attribute) fields khong the thay bang bien khac duoc, bien fields la bat buoc, fields co nhieu truong nen them 's
    
    # Ham validate duoc su dung de kiem tra xem password va password2 co giong nhau khong
    def validate(self, attr):
        # Xac dinh mot ham xac thuc de kiem tra xem password va password2 co giong nhau khong
        if attr['password'] != attr['password2']:
            # Neu khong giong nhau thi raise ra loi validation
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        # Tra ve cac thuoc tinh duoc xac thuc
        return attr

    def create(self, validated_data):
        # Xac dinh mot ham de tao mot user moi dua tren du lieu duoc xac thuc
        user = api_models.User.objects.create(
            full_name=validated_data['full_name'],  # lay du lieu tu validated_data trong truong full_name
            email=validated_data['email'], # lay du lieu tu validated_data trong truong email
        )
        email_username, mobile = user.email.split('@') # tach email thanh 2 phan: email_username va mobile
        user.username = email_username # gan username bang email_username

        # Dat password cho user dua tren du lieu duoc xac thuc
        user.set_password(validated_data['password'])
        user.save()

        # Tra ve user moi duoc tao
        return user
    
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = api_models.User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = api_models.Profile
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    # Mục đích: Serialize thông tin category và tính toán số lượng bài post 
    # trong mỗi category thông qua phương thức get_post_count
    def get_post_count(self, category):
        return category.posts.count()
    
    class Meta:
        model = api_models.Category
        fields = ['id', 'title', 'image','slug', 'post_count']
        
class CommentSerializer(serializers.ModelSerializer):
    # Mục đích: Xử lý serialize comment với 2 chế độ:
    # - Khi tạo comment mới (POST): chỉ cần ID của các relationship
    # - Khi đọc comment (GET): hiển thị đầy đủ thông tin của các relationship
    # để giảm số lượng API calls cần thiết
    class Meta:
        model = api_models.Comment
        fields = '__all__'
    # vi du lop cha: 
    # class ModelSerializer:
    #     def __init__(self, instance=None, data=None, **kwargs):
    #         self.instance = instance
    #         self.data = data
    #         self.context = kwargs.get('context', {})
    
    # vi du lop con ke thua lop cha:
    def __init__(self, *args, **kwargs): # khoi tao lop con
        super(CommentSerializer, self).__init__(*args, **kwargs) # trong super phai la mot lop con chu khong phai la lop cha
        # neu co tinh dat super(ModelSerializer, self).__init__(*args, **kwargs) thi se
        # - Mất các thiết lập từ các lớp trung gian
        # - Không khởi tạo đúng các thuộc tính cần thiết
        # - Lỗi khi DRF cập nhật cấu trúc kế thừa va nhieu loi tiem an khac
        request =self.context.get("request")
        #  Serializer trong DRF có thể truy cập context chứa thông tin về request hiện tại
        # self.context.get("request") lấy đối tượng request từ context
        if request and request.method == 'POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1
        # - depth trong Meta class của serializer quyết định độ sâu của quan hệ được serialize
        # Khi depth = 0: chỉ trả về ID của các quan hệ
        # Khi depth = 1: serialize thêm một cấp của các quan hệ (nested relationships)
        # Mục đích của đoạn code:
        # - Khi người dùng tạo comment mới (POST request): chỉ cần gửi các ID của các quan hệ (depth = 0)
        # - Khi đọc comments (GET request): hiển thị thêm thông tin chi tiết của các quan hệ (depth = 1)
        
class PostSerializer(serializers.ModelSerializer):
    # Mục đích: Serialize bài post với 2 chế độ:
    # - POST: Chỉ lưu ID của các relationship (author, category, etc.)
    # - GET: Hiển thị đầy đủ thông tin của các relationship để giảm số lượng API calls
    class Meta:
        model = api_models.Post
        fields = "__all__"  # Serialize tất cả các trường của model Post

    def __init__(self, *args, **kwargs):
        super(PostSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        # Điều chỉnh độ sâu serialize dựa vào loại request
        if request and request.method == 'POST':
            # depth: Mở rộng mức độ chi tiết của các đối tượng liên kết trong JSON trả về.
            self.Meta.depth = 0  # Chỉ lưu ID khi tạo post mới
        else:
            self.Meta.depth = 3  # Hiển thị thêm 1 cấp relationship khi đọc post
            
class BookMarkSerializer(serializers.ModelSerializer):
    # Mục đích: Xử lý bookmark của user cho các bài post
    # Tương tự PostSerializer, sử dụng 2 chế độ depth khác nhau cho POST/GET
    class Meta:
        model = api_models.Bookmark
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(BookMarkSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request') # lay request tu context
        if request and request.method == 'POST':
            # depth: Mở rộng mức độ chi tiết của các đối tượng liên kết trong JSON trả về.
            self.Meta.depth = 0  # Chỉ cần ID post và user khi tạo bookmark
        else:
            self.Meta.depth = 1  # Hiển thị thông tin chi tiết khi xem bookmarks

class NotificationSerializer(serializers.ModelSerializer):  
    # Mục đích: Xử lý thông báo cho user (ví dụ: khi có comment mới, like mới, etc.)
    # Áp dụng cùng pattern về depth như các serializer trên
    class Meta:
        model = api_models.Notification
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(NotificationSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method == 'POST':
            # depth: Mở rộng mức độ chi tiết của các đối tượng liên kết trong JSON trả về.
            self.Meta.depth = 0  # Chỉ lưu các ID liên quan khi tạo notification
        else:
            self.Meta.depth = 1  # Hiển thị chi tiết khi đọc notifications
            
class AuthorSerializer(serializers.Serializer):
    # Mục đích: Tạo một serializer đặc biệt để hiển thị thống kê về author
    # Không kế thừa ModelSerializer vì không cần mapping trực tiếp với model nào
    # Chỉ dùng để hiển thị các số liệu thống kê
    views = serializers.IntegerField(default=0)     # Tổng số lượt xem
    posts = serializers.IntegerField(default=0)     # Số bài viết
    likes = serializers.IntegerField(default=0)     # Tổng số like nhận được
    bookmarks = serializers.IntegerField(default=0) # Số lần bài viết được bookmark
    


