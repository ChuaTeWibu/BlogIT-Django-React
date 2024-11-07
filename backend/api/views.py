from django.shortcuts import render # su dung de render ra giao dien
from django.http import JsonResponse # su dung de tra ve response dang json
from django.core.mail import EmailMultiAlternatives # su dung de gui email
from django.template.loader import render_to_string # su dung de render ra template
from django.conf import settings # su dung de lay setting
from django.contrib.auth.tokens import default_token_generator # su dung de tao token
from django.utils.http import urlsafe_base64_encode # su dung de encode url
from django.utils.encoding import force_bytes # su dung de encode bytes
from django.db.models import Sum # su dung de tinh tong

# Restframework
from rest_framework import status # su dung de tra ve status code
from rest_framework.decorators import api_view, APIView # su dung de tao API
from rest_framework.response import Response # su dung de tra ve response
from rest_framework_simplejwt.views import TokenObtainPairView # su dung de lay token
from rest_framework import generics # su dung de tao API
from rest_framework.permissions import AllowAny, IsAuthenticated # su dung de xac thuc
from rest_framework.decorators import api_view, permission_classes # su dung de tao API
from rest_framework_simplejwt.tokens import RefreshToken # su dung de tao token

from drf_yasg import openapi # su dung de tao swagger
from drf_yasg.utils import swagger_auto_schema # su dung de tao swagger
from datetime import datetime # su dung de lay thoi gian

# khac thu vien khac
import json # su dung de chuyen doi sang json
import random # su dung de random

# Import serializer va model de xu ly du lieu
from api import serializer as api_serializer # su dung de serializer
from api import models as api_models # su dung de lay model



## NOTICE:

# Tai lieu API:
# Tài liệu API là một tài liệu kỹ thuật mô tả các thông tin về API của bạn, bao gồm:

# Tên của endpoint: Tên của endpoint, ví dụ: get_users, create_user, update_user,...
# Phương thức HTTP: Phương thức HTTP được hỗ trợ, ví dụ: GET, POST, PUT, DELETE,...
# Tham số yêu cầu: Các tham số yêu cầu, ví dụ: query parameters, body parameters,...
# Phản hồi: Các phản hồi có thể xảy ra, ví dụ: 200 OK, 404 Not Found, 500 Internal Server Error,...
# Ví dụ về yêu cầu và phản hồi: Các ví dụ về yêu cầu và phản hồi, ví dụ: GET /users, POST /users, PUT /users/1,...
# Mô tả: Mô tả về endpoint, ví dụ: "Lấy danh sách người dùng", "Tạo người dùng mới", "Cập nhật người dùng",...
# Tham số: Các tham số yêu cầu, ví dụ: id, name, email,...
# Kiểu dữ liệu: Kiểu dữ liệu của các tham số, ví dụ: integer, string, boolean,...
# Giá trị mặc định: Giá trị mặc định của các tham số, ví dụ: 0, "", false,...
# Ví dụ về dữ liệu: Các ví dụ về dữ liệu, ví dụ: {"id": 1, "name": "John Doe", "email": "john.doe@example.com"},...


# ## Tạo API endpoint trong Restframework tu generics module
# # generics la mot module cung cap cac lop view dung de tao ra cac API endpoint: CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
# # CreateAPIView tạo một endpoint (POST) để tạo được đối tượng: Nó chỉ hợ trình method POST, không hợ trình GET, PUT, DELETE
# # ListAPIView tao một endpoint (GET) để lấy danh sách các đối tượng: Nó chỉ hợ trình method GET, không hợ trình POST, PUT, DELETE
# # RetrieveAPIView tao môn endpoint (GET) de lay thong tin chi tiet mot doi tuong: cho phép xem (GET) và cập nhật (PUT/PATCH) một đối tượng.
# # UpdateAPIView tao một endpoint (PUT/PATCH) để cập nhật một đối tượng: Nó chỉ hợ trình method PUT/PATCH, không hợ trình GET, POST, DELETE
# # DestroyAPIView tao môn endpoint (DELETE) để xóa một đối tượng: Nó chỉ hợ trình method DELETE, không hợ trình GET, POST, PUT/PATCH



######################## User APIs ########################

# Class xử lý việc đăng nhập và tạo JWT token
# Khi user đăng nhập thành công, sẽ trả về access_token và refresh_token
class MyTokenObtainPairView(TokenObtainPairView): # Dang Nhap # TokenObtainPairView xử lý việc tạo cặp token JWT (access token và refresh token)
    # Sử dụng serializer tùy chỉnh để xử lý dữ liệu token
    serializer_class = api_serializer.MyTokenObtainPairSerializer
    

# Class xử lý việc đăng ký tài khoản mới
# Tạo API endpoint POST /register/
class RegisterView(generics.CreateAPIView):  #Dang Ky
    # generics la mot module cung cap cac lop view dung de tao ra cac API endpoint: CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
    # CreateAPIView là view xử lý request POST để tạo mới đối tượng
    # Nó chỉ hỗ trợ method POST, không hỗ trợ GET, PUT, DELETE
    
    # Xác định tập dữ liệu là tất cả users trong database
    queryset = api_models.User.objects.all()
    
    # Cho phép tất cả người dùng truy cập API này mà không cần xác thực
    permission_classes = [AllowAny] # AllowAny cho phep moi nguoi truy cap
    
    # Sử dụng RegisterSerializer để validate và xử lý dữ liệu đăng ký
    serializer_class = api_serializer.RegisterSerializer
    
    
# Class xử lý xem và cập nhật thông tin profile người dùng
# Tạo API endpoint GET và PUT/PATCH /profile/<user_id>/
class ProfileView(generics.RetrieveUpdateAPIView): # Xem Profile
    # generics la mot module cung cap cac lop view dung de tao ra cac API endpoint: CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
    # RetrieveUpdateAPIView là một generic view của DRF cho phép xem (GET) và cập nhật (PUT/PATCH) một đối tượng.
    # Giải thích chi tiết:
    # - GET: Xem chi tiết profile
    # - PUT: Cập nhật toàn bộ profile
    # - PATCH: Cập nhật một phần profile
    
    
    # Cho phép tất cả người dùng truy cập API này
    permission_classes = [AllowAny]
    
    # Sử dụng ProfileSerializer để xử lý dữ liệu profile
    serializer_class = api_serializer.ProfileSerializer

    # Override method get_object để lấy profile dựa vào user_id
    def get_object(self): # 
        # Lấy user_id từ URL parameters
        user_id = self.kwargs['user_id'] 
        # self.kwargs là dictionary chứa các tham số URL động
        # self.kwargs là một thuộc tính trong Django view, chứa tất cả các tham số của URL dưới dạng một dictionary.
        # user_id = self.kwargs['user_id']: Lấy giá trị của user_id từ dictionary kwargs
        # vi du: GET /api/user/5/dashboard
        # Django sẽ chuyển user_id=5 vào self.kwargs, để self.kwargs trở thành {'user_id': 5}.
        # Khi đó, self.kwargs['user_id'] sẽ trả về 5, và dòng user_id = self.kwargs['user_id'] sẽ gán user_id = 5

        # Sử dụng user_id để tìm user trong database
        user = api_models.User.objects.get(id=user_id)
        
        # Tìm profile tương ứng với user đó
        profile = api_models.Profile.objects.get(user=user)
        return profile
    


######################## Post APIs ########################

# Class này dùng để lấy danh sách các danh mục
# Kế thừa từ ListAPIView nên chỉ hỗ trợ method GET
class CategoryListAPIView(generics.ListAPIView): # Xem Danh Muc
    # generics la mot module cung cap cac lop view dung de tao ra cac API endpoint: CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
    # ListAPIView chỉ hỗ trợ method GET để lấy danh sách
    # Ví dụ: Lấy danh sách các danh mục (categories)
    
    # Sử dụng CategorySerializer để xử lý dữ liệu danh mục
    serializer_class = api_serializer.CategorySerializer
    
    # Cho phép ai cũng có thể xem danh sách
    permission_classes = [AllowAny]
    
    # Lấy tất cả các danh mục từ database
    def get_queryset(self):
        return api_models.Category.objects.all()

# Class này dùng để lấy danh sách các bài viết theo danh mục
# Kế thừa từ ListAPIView nên chỉ hỗ trợ method GET
class PostCategoryListAPIView(generics.ListAPIView):
    # generics la mot module cung cap cac lop view dung de tao ra cac API endpoint: CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
    # Sử dụng PostSerializer để chuyển đổi dữ liệu bài viết thành JSON
    serializer_class = api_serializer.PostSerializer
    
    # Cho phép tất cả người dùng có thể xem danh sách bài viết
    permission_classes = [AllowAny]
    
    # Override phương thức get_queryset để lọc bài viết theo category: danh mục
    def get_queryset(self):
        # Lấy category_slug từ URL
        # Ví dụ URL: # URL: /api/categories/dien-thoai/
        # thì category_slug = 'dien-thoai'
        category_slug = self.kwargs['category_slug']
         # self.kwargs là dictionary chứa các tham số URL động
        # self.kwargs là một thuộc tính trong Django view, chứa tất cả các tham số của URL dưới dạng một dictionary.
        # category_slug = self.kwargs['category_slug']:
        
        # Lấy category_slug từ self.kwargs. Đây là giá trị được trích xuất từ URL, ví dụ: nếu URL là /api/category/python/, thì category_slug sẽ có giá trị 'python'.
        # category = api_models.Category.objects.get(slug=category_slug):
        # Tìm đối tượng Category có slug khớp với category_slug. Điều này giúp đảm bảo chúng ta làm việc với danh mục chính xác.

        # vidu: /api/category/python/— Với category_slug là 'python'
        # /api/category/web-development/ — Với category_slug là 'web-development'  
          
        
        # Tìm category dựa vào slug
        category = api_models.Category.objects.get(slug=category_slug)
        
        # Trả về danh sách các bài viết:
        # 1. Thuộc category đã tìm được
        # 2. Có trạng thái là "Active"
        return api_models.Post.objects.filter(
            category=category,  # Lọc theo category
            status="Active"     # Chỉ lấy bài viết đang active
        )

# Class này dùng để lấy danh sách các bài viết
# Kế thừa từ ListAPIView nên chỉ hỗ trợ method GET
class PostListAPIView(generics.ListAPIView):
    # generics la mot module cung cap cac lop view dung de tao ra cac API endpoint: CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
    # Sử dụng PostSerializer để chuyển đổi dữ liệu bài viết thành JSON  
    serializer_class = api_serializer.PostSerializer
    
    # Cho phép tất cả người dùng có thể xem danh sách bài viết
    permission_classes = [AllowAny]

    # Lấy tất cả các bài viết từ database
    def get_queryset(self):
        return api_models.Post.objects.filter(status="Active")
        

# Class này dùng để lấy chi tiết bài viết
# Kế thừa từ RetrieveAPIView nên chỉ hỗ trợ method GET
class PostDetailAPIView(generics.RetrieveAPIView): # Xem Bai Viet
    # generics la mot module cung cap cac lop view dung de tao ra cac API endpoint: CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
    # RetrieveAPIView là một endpoint de lay thong tin chi tiet cua doi tuong
    # Giải thích chi tiết:
    # - GET: Xem chi tiết bài viết
    # - PUT: Cập nhật toàn bộ bài viết
    # - PATCH: Cập nhật một phần bài viết    
    
    
    # Sử dụng PostSerializer để chuyển đổi dữ liệu bài viết thành JSON
    serializer_class = api_serializer.PostSerializer
    
    # Cho phép tất cả người dùng có thể xem chi tiết bài viết
    permission_classes = [AllowAny] # Cho phep người dùng truy cập API này mà không cần xác thực

    # Override phương thức get_object để lấy bài viết dựa vào slug
    def get_object(self):
        # Lấy slug từ URL
        slug = self.kwargs['slug'] # slug la tham so truyen vao URL vidu: /api/posts/123/ thi slug = 123
        
        # Tìm bài viết dựa vào slug
        post = api_models.Post.objects.get(slug=slug, status="Active")
        
        # Tăng số lượt xem lên 1
        post.view += 1
        post.save()
        
        return post


class LikePostAPIView(APIView): # APIView co nghia la view co the truy cap nhung khong can xac thuc
    #APIView la mot lop view co ban de tao ra cac API endpoint don gian: vidu ho tro method HTTP GET, POST, PUT, PATCH, DELETE, ho tro cho cac serializer, ho tro cac permission va van van.
   #APIView là một lớp tuỳ chỉnh, không cần serializer, nhưng mình phải chủ động viết code xử lý các yêu cầu Get và Post của endpoint nay.
    
    # @swagger_auto_schema là một decorator được cung cấp bởi thư viện drf-yasg (Django Rest Framework YAML Swagger Generator).
    # @swagger_auto_schema là một decorator (trang trí) được sử dụng trong Django để tự động tạo tài liệu API cho các endpoint (điểm cuối) của ứng dụng.
    # Sử dụng decorator @swagger_auto_schema để tự động tạo tài liệu API cho endpoint nay
    @swagger_auto_schema(
        # Định nghĩa schema cho request body
        request_body=openapi.Schema( # Schemas là một ánh xạ của một đối tượng
            # Xác định rằng request body sẽ là một đối tượng JSON
            type=openapi.TYPE_OBJECT, # type được dùng để dịnh nghĩa một đối tượng JSON
            #  Định nghĩa các thuộc tính chi tiết của đối tương JSON đó trong request body
            properties={
                # Định nghĩa thuộc tính user_id là một số nguyên
                'user_id': openapi.Schema(type=openapi.TYPE_INTEGER), # openapi.Schema: Định nghĩa một thuộc tính, trong đó type sẽ là một số nguyên
                # Định nghĩa thuộc tính post_id là một số nguyên
                'post_id': openapi.Schema(type=openapi.TYPE_INTEGER), # openapi.Schema: Định nghĩa một thuộc tính, trong đó type sẽ là một số nguyên
            },
        ),
    )
    def post(self, request):
        # dựa trên properties, thì mình sẽ gửi một request Post với các thuộc tính: post_id, user_id, đến API endpoint, sau đó API endpoint sẽ xữ lý request này nếu cần thiết, API endpoint sẽ tương tác với cơ sở dữ liệu để lưu trữ, cập nhật, hoặc lấy dữ liệu.
        # Lấy giá trị của thuộc tính user_id từ request body
        user_id = request.data['user_id']
        # Lấy giá trị của thuộc tính post_id từ request body
        post_id = request.data['post_id']
    
        # Tìm kiếm và lấy đối tượng User từ cơ sở dữ liệu dựa trên giá trị user_id
        user = api_models.User.objects.get(id=user_id)
        # Tìm kiếm và lấy đối tượng Post từ cơ sở dữ liệu dựa trên giá trị post_id
        post = api_models.Post.objects.get(id=post_id)
    
        # Kiểm tra xem người dùng hiện tại đã thích bài viết hay chưa
        if user in post.likes.all():
            # Nếu người dùng đã thích bài viết, hãy xóa người dùng khỏi danh sách những người đã thích bài viết
            post.likes.remove(user)
            # Trả về một phản hồi với thông báo "Post Disliked" và trạng thái HTTP 200 (OK)
            return Response({"message": "Post Disliked"}, status=status.HTTP_200_OK)
        else:
            # Nếu người dùng chưa thích bài viết, hãy thêm người dùng vào danh sách những người đã thích bài viết
            post.likes.add(user)
            
            # Tạo một thông báo mới cho người dùng là tác giả của bài viết
            api_models.Notification.objects.create(
                user=post.user,
                post=post,
                type="Like",
            )
            # Trả về một phản hồi với thông báo "Post Liked" và trạng thái HTTP 201 (Created)
            return Response({"message": "Post Liked"}, status=status.HTTP_201_CREATED)
        
class PostCommentAPIView(APIView):
    """
    Class này định nghĩa một API endpoint để nhận và lưu trữ các bình luận của người dùng
    """
    @swagger_auto_schema(
        # request_body: Định nghĩa một đối tượng, trong đó type sẽ là một đối tương, properties sẽ là một dictionary chọn 
        request_body=openapi.Schema( # Schemas là một ánh xạ của một đối tượng
            type=openapi.TYPE_OBJECT,# type được dùng để dịnh nghĩa một đối tượng JSON
            # Định nghĩa các thuộc tính chi tiết của đối tương JSON đó trong request body
            properties={
                'post_id': openapi.Schema(type=openapi.TYPE_INTEGER), # openapi.Schema: Định nghĩa một thuộc tính, trong đó type sẽ là một số nguyên
                'name': openapi.Schema(type=openapi.TYPE_STRING), # openapi.Schema: Định nghĩa một thuộc tính, trong đó type sẽ là một chuỗi
                'email': openapi.Schema(type=openapi.TYPE_STRING), # openapi.Schema: Định nghĩa môn thuộc tính, trong đó type sẽ là môn chuỗi
                'comment': openapi.Schema(type=openapi.TYPE_STRING), # openapi.Schema: Định nghĩa một thuộc tính, trong đó type sẽ là một chuỗi
            },
        ),
    )
    def post(self, request):
        """
        Phương thức này sẽ được gọi khi người dùng gửi một yêu cầu POST đến API endpoint
        """
        # dựa trên properties, thì mình sẽ gửi một request Post với các thuộc tính: post_id, name, email, comment đến API endpoint, sau đó API endpoint sẽ xữ lý request này nếu cần thiết, API endpoint sẽ tương tác với cơ sở dữ liệu để lưu trữ, cập nhật, hoặc lấy dữ liệu.
        post_id = request.data['post_id'] # post_id dùng để lọc bài viết
        name = request.data['name'] # name dùng để lọc bài viết
        email = request.data['email']
        comment = request.data['comment']

        # Tìm kiếm và lấy đối tượng Post từ cơ sở dữ liệu dựa trên giá trị post_id
        post = api_models.Post.objects.get(id=post_id)

        # Tạo một bình luận mới
        api_models.Comment.objects.create(
            post=post,
            name=name,
            email=email,
            comment=comment,
        )

        # Tạo một thông báo mới cho người dùng là tác giả của bài viết
        api_models.Notification.objects.create(
            user=post.user,
            post=post,
            type="Comment",
        )

        # Trả về một phản hồi cho người dùng
        return Response({"message": "Comment Sent"}, status=status.HTTP_201_CREATED)

class BookmarkPostAPIView(APIView):
    """
    API endpoint để bookmark hoặc un-bookmark một bài viết.
    """
    
    @swagger_auto_schema(
        # request_body: Định nghĩa một đối tượng, trong đó type sẽ là một đối tương, properties sẽ là một dictionary chọn
        request_body=openapi.Schema(  # Schemas là một ánh xạ của một đối tượng
            type=openapi.TYPE_OBJECT, # type được dùng để dịnh nghĩa một đối tượng JSON
            # properties: Định nghĩa các thuộc tính chi tiết của đối tương JSON đó trong request body
            properties={
                'user_id': openapi.Schema(type=openapi.TYPE_INTEGER), # openapi.Schema: Định nghĩa một thuộc tính, trong đó type sẽ là một số nguyên
                'post_id': openapi.Schema(type=openapi.TYPE_STRING), # openapi.Schema: Định nghĩa một thuộc tính, trong đó type sẽ là một số nguyên
            },
        ),
    )

    def post(self, request):
        
        """
        Xử lý yêu cầu POST để bookmark hoặc un-bookmark một bài viết.

        Args:
            request (HttpRequest): Đối tượng yêu cầu HTTP.

        Returns:
            Response: Đối tượng phản hồi HTTP với một thông điệp chỉ ra kết quả của hoạt động.
        """

        # dựa trên properties, thì mình sẽ gửi một request Post với các thuộc tính: post_id, user_id, đến API endpoint, sau đó API endpoint sẽ xữ lý request này nếu cần thiết, API endpoint sẽ tương tác với cơ sở dữ liệu để lưu trữ, cập nhật, hoặc lấy dữ liệu.
        # Lấy giá trị của thuộc tính user_id từ request body
        user_id = request.data['user_id']
        post_id = request.data['post_id']

        # Lấy đối tượng người dùng và bài viết từ cơ sở dữ liệu:
        # Tìm kiếm và lấy đối tượng User từ cơ sở dữ liệu dựa trên giá trị user_id
        user = api_models.User.objects.get(id=user_id)
        # Tìm kiếm và lấy đối tượng Post từ cơ sở dữ liệu dựa trên giá trị post_id
        post = api_models.Post.objects.get(id=post_id)

        # Kiểm tra xem người dùng đã bookmark bài viết này chưa
        # Trong truy vấn này, post=post và user=user là các điều kiện lọc. post=post chỉ định rằng chỉ những bookmark có thuộc tính post bằng với đối tượng post hiện tại mà chúng ta đang xử lý. user=user chỉ định rằng chỉ những bookmark có thuộc tính user bằng với đối tượng user hiện tại mà chúng ta đang xử lý.
        # filter phương thức được sử dụng để tạo một truy vấn lọc dữ liệu. 
        # first() phương thức được sử dụng để lấy một bookmark duy nhất từ kết quả truy vấn. Nếu không có bookmark nào thỏa mãn các điều kiện lọc, first() sẽ trả về None.
        bookmark = api_models.Bookmark.objects.filter(post=post, user=user).first() 
        if bookmark:
             # Nếu người dùng đã bookmark bài viết, thì xóa bookmark trên cơ sở dữ liệu
            bookmark.delete()
            return Response({"message": "Post Un-Bookmarked"}, status=status.HTTP_200_OK)
        else:
            # Nếu người dùng chưa bookmark bài viết, thì tạo bookmark trên cơ sở dữ liệu
            # Tạo một bookmark mới cho người dùng và bài viết
            api_models.Bookmark.objects.create(
                user=user,
                post=post
            )

            # Tạo một thông báo cho người dùng của bài viết
            api_models.Notification.objects.create(
                user=post.user,
                post=post,
                type="Bookmark",
            )

            return Response({"message": "Post Bookmarked"}, status=status.HTTP_201_CREATED)
        
######################## Dashboard APIs ########################

# Import lớp ListAPIView từ Django REST framework, dùng để tạo một API trả về danh sách dữ liệu
class DashboardStats(generics.ListAPIView):
    # Định nghĩa serializer để chuyển dữ liệu Python thành JSON trước khi trả về cho client
    serializer_class = api_serializer.AuthorSerializer  # AuthorSerializer: Chuyển dữ liệu từ DB sang JSON
    
    # Đặt quyền truy cập cho API. AllowAny cho phép mọi người, kể cả người không đăng nhập, có thể truy cập.
    permission_classes = [AllowAny]  # AllowAny: không giới hạn quyền truy cập vào API này

    # Hàm get_queryset sẽ xác định dữ liệu nào sẽ được lấy từ DB
    def get_queryset(self):
        # Lấy user_id từ các tham số truyền vào URL (được truyền qua kwargs)
        user_id = self.kwargs['user_id']  # self.kwargs là dictionary chứa các tham số URL động
        #self.kwargs là một thuộc tính trong Django view, chứa tất cả các tham số của URL dưới dạng một dictionary.
        # user_id = self.kwargs['user_id']: Lấy giá trị của user_id từ dictionary kwargs
        # vi du: GET /api/user/5/dashboard
        # Django sẽ chuyển user_id=5 vào self.kwargs, để self.kwargs trở thành {'user_id': 5}.
        # Khi đó, self.kwargs['user_id'] sẽ trả về 5, và dòng user_id = self.kwargs['user_id'] sẽ gán user_id = 5

        # Lấy đối tượng User từ DB dựa trên user_id để lấy thông tin người dùng cụ thể
        user = api_models.User.objects.get(id=user_id)  # Tìm đối tượng User với id là user_id
        
        # Lấy tổng số lượt xem từ các bài viết của người dùng do  
        views = api_models.Post.objects.filter(user=user).aggregate(view=Sum("view"))['view']
        
        # Sử dụng .filter(user=user) để tìm tất cả bài viết của user, rồi dùng .aggregate(view=Sum("view"))
        # để tính tổng số lượt xem từ các bài viết này.
        
        # aggregate(): Đây là một phương thức của QuerySet cho phép thực hiện các phép toán tính toán (như tổng, trung bình, đếm,…) trên các trường cụ thể của các bản ghi được chọn.
        # Cú pháp chung: aggregate(<name>=<function>("field")), trong đó:
        # <name>: Tên của kết quả sau khi tính toán. Trong trường hợp này là view.
        # <function>: Phép toán tính toán mà ta muốn thực hiện. Ở đây là Sum.
        # "field": Trường dữ liệu mà phép toán sẽ tính toán. Ở đây là "view".
        # vidu: id: 1, post: Hello World, user_id: 1, view: 10
        # id: 2, post: Python, user_id: 1, view: 20
        # aggregate(view=Sum("view")): {'view': 30}  # Tổng số lượt xem cho các bài viết của user 5 la 30

        
        
        # Đếm tổng số bài viết mà người dùng đã đăng
        posts = api_models.Post.objects.filter(user=user).count()
        # .filter(user=user) lấy danh sách bài viết của người dùng, rồi dùng .count() để đếm số lượng bài viết.
        
        # Tính tổng số lượt thích của tất cả bài viết của người dùng
        likes = api_models.Post.objects.filter(user=user).aggregate(total_likes=Sum("likes"))['total_likes']
        # .aggregate(total_likes=Sum("likes")) tính tổng số lượt thích từ bài viết của người dùng.
        
        # Đếm tổng số lần đánh dấu (bookmark) của toàn hệ thống, không chỉ của riêng người dùng này
        bookmarks = api_models.Bookmark.objects.filter(user=user).count() 
        # user phía trước sẽ là trường nằm bên model còn user phía sau là thằng id đã được gán bên trên
        # .filter(post_user=user) lấy danh sách Bookmark của người dùng, rồi dùng .count() để đếm số lượng Bookmark.
        # .count() lấy tổng số lượng đối tượng Bookmark trong bảng Bookmark.
        
        # Trả về một danh sách chứa một dictionary với các thống kê đã tính toán
        return [{
            "views": views,        # Tổng số lượt xem từ bài viết của người dùng
            "posts": posts,        # Tổng số bài viết của người dùng
            "likes": likes,        # Tổng số lượt thích từ bài viết của người dùng
            "bookmarks": bookmarks # Tổng số lượt đánh dấu của toàn hệ thống
        }]

    # Hàm list ghi đè phương thức list mặc định của ListAPIView để trả về dữ liệu JSON
    def list(self, request, *args, **kwargs):
        # Gọi get_queryset để lấy dữ liệu thống kê của người dùng (được định nghĩa bên trên)
        queryset = self.get_queryset()
        
        # Sử dụng serializer (AuthorSerializer) để chuyển dữ liệu sang JSON
        serializer = self.get_serializer(queryset, many=True)  
        # `many=True` vì queryset là một danh sách (mặc dù chỉ có một dictionary bên trong)
        # vidu:
        # [
        # {'id': 1, 'name': 'John', 'age': 30},
        # {'id': 2, 'name': 'Jane', 'age': 25},
        # {'id': 3, 'name': 'Bob', 'age': 40}
        # ] -> trả về Json nếu many=True thì trả về hết list
        
        # [
        # {'id': 1, 'name': 'John', 'age': 30},
        # {'id': 2, 'name': 'Jane', 'age': 25},
        # {'id': 3, 'name': 'Bob', 'age': 40}
        # ]
            
        # còn nếu many=False thì trả về một dictionary -> {'id': 1, 'name': 'John', 'age': 30},
        
        
        # Trả về dữ liệu JSON đã được serializer trong một HTTP response
        return Response(serializer.data)
