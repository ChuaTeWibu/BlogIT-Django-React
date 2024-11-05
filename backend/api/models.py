from django.db import models
from django.contrib.auth.models import AbstractUser # AbstractBaseUser: là một lớp cơ sở cho các model user trong Django
from django.db.models.signals import post_save # post_save: khi có sự kiện lưu dữ liệu
from django.utils.text import slugify # slugify: chuyển đổi chuỗi thành slug

from shortuuid.django_fields import ShortUUIDField # ShortUUIDField: tạo ra các id ngắn
import shortuuid # shortuuid: tạo ra các id ngắn
# UUID (Universally Unique Identifier): tieu chuan 32 ky tu
# shortuuid: 22 ky tu

# Create your models here.

class User(AbstractUser):
    username = models.CharField(unique=True, max_length=100) # unique: chi co 1 username duy nhat khong duoc trung lap
    email = models.EmailField(unique=True) # unique: chi co 1 email duy nhat khong duoc trung lap
    full_name = models.CharField(max_length=100, null=True, blank=True)
    
    # Cho nguoi dung dang nhap bang email hay vi ten cua ho
    USERNAME_FIELD = 'email' # set ten nguoi dung la email de dang nhap
    REQUIRED_FIELDS = ['username'] # bat cu khi nao chung ta tao, username se duoc them vao
    
    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs): # *args, **kwargs: là các tham số không xác định
        email_username, mobile = self.email.split("@")
        # vi du: hothienty@gmail.com thi username se la hothienty: hothienty: email_username     @gmail.com:mobile
        if self.full_name == "" or self.full_name == None:
            self.full_name = email_username
        if self.username == "" or self.username == None:
            self.username = email_username
        # save: lưu dữ liệu vào database
        super(User,self).save(*args, **kwargs) # super: de giao tiep voi lop cha, save: key va value
        
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # OneToOneField: một-một giữa User và Profile
    image = models.FileField(upload_to="image", default="default/default-user.jpg", null=True, blank=True) # khong su dung ImageField vi no se bi gioi han boi mot so extension, nhung FileField thi cho phep
    full_name = models.CharField(max_length=100, null=True, blank=True)
    bio = models.CharField(max_length=100, null=True, blank=True)
    about = models.CharField(max_length=100, null=True, blank=True)
    author = models.BooleanField(default=False)
    country = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username # o class nay khong co username nen phai goi tu class User
    
    def save(self, *args, **kwargs): # *args: arguments: Doi so duoc luu tru trong tuple args, **kwargs: keyword arguments: Doi so duoc luu tru trong dictionary kwargs
        if self.full_name == "" or self.full_name == None:
            self.full_name = self.user.full_name
            
        # save: lưu dữ liệu vào database
        super(Profile,self).save(*args, **kwargs) # super: de giao tiep voi lop cha, save: key va value
  
  
# tu dong tao profile khi user duoc tao: 
# sender: Model gửi signal (trong trường hợp này là User model)
# instance: instance của model được gửi signal (trong trường hợp này là instance của User model)
# day la nhung tham so dac biet va bat buoc cua post_save signal
def create_user_profile(sender, instance, created, **kwargs): 
    if created:
        Profile.objects.create(user=instance)
        
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save() ## vi Profile lien ket 1-1 voi User nen Django tu tao ra mot thuoc tinh (reverse relationship) tren models User, 
    ##Theo mặc định, thuộc tính này có tên là tên của model liên kết viết thường, trong trường hợp này là profile.

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)



class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to="image", null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True) # SlugField: tạo ra một đường dẫn ngắn cho category, chi co 1 slug duy nhat khong duoc trung lap
    
    def __str__(self):
        return self.title   
    
    # class Meta:
    #     ordering = ['-date'] # sap xep theo ngay giam dan
    #     verbose_name_plural = "Categories" 
    #     # Nếu không có verbose_name_plural, Django sẽ tự động chuyển đổi verbose_name thành dạng số nhiều là "Danh mụcs", điều này không chính xác trong tiếng Việt 
    
    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title)
        super(Category,self).save(*args, **kwargs)
    
    def post_count(self):
        return Post.objects.filter(category=self).count()
        # dem so bai viet trong mot category thong qua category=self: Category, self la chi Category
        

class Post(models.Model):
    
    STATUS = (
        ("Active", "Active"),
        ("Draft", "Draft"),
        ("Disabled", "Disabled"),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True )
    image = models.FileField(upload_to="image", null=True, blank=True)
    status = models.CharField(choices=STATUS,max_length=100, default="Active")
    view = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, blank=True,related_name="likes_user") # null khong hoat dong voi many to many field, cho du co them thi no cung khong hoat dong
    slug = models.SlugField(unique=True, null=True, blank=True) # chi co 1 slug duy nhat khong duoc trung lap
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title   
    
    class Meta: 
        ## Class Meta duoc hieu nhu la 1 lop metadata co the thuc hien cac chuc nang bo sung vi du nhu
        # -Điều chỉnh hiển thị: Đặt tên hiển thị cho model, Sắp xếp dữ liệu
        # -Cấu hình Database:  Đặt tên bảng, Đặt tên trường, Đặt tên cột, tạo các index, thiet lap cac rang buoc (constraints)
        # -Phân quyền: Đặt tên quyền truy cập, thiết lập các quyền truy cập cho các trường dữ liệu
        # -Cau hinh khac: Abstract model, ordering, verbose_name, verbose_name_plural
        ordering = ['-date'] # sap xep theo ngay giam dan
        verbose_name_plural = "Post" 
        # Nếu không có verbose_name_plural, Django sẽ tự động chuyển đổi verbose_name thành dạng số nhiều là "Bài viếts", điều này không chính xác trong tiếng Việt 
        
    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title) + "-" + shortuuid.uuid()[:2]# shortuuid.uuid()[:2]: tạo ra một chuỗi ngẫu nhiên 2 ký tự
            # vi du: "Ho Thien Ty Dep Trai" -> "ho-thien-ty-dep-trai" -> "ho-thien-ty-dep-trai-k9"
            # viec nay se giup cho cac user khi tao mot bai dang co cung mot tieu de, vao mot thoi diem
            # se khong bi loi vi da co doan code tren giai quyet van de la tao ra 2 ky tu ngau nhien
        super(Post,self).save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    comment = models.TextField()
    reply = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title
    
    class Meta:
        ordering = ["-date"]
        verbose_name_plural = "Comment"
        
class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post.title} - {self.user.username}"
    
    class Meta:
        ordering = ["-date"]
        verbose_name_plural = "Bookmark"
        
        
class Notification(models.Model):
    NOTI_TYPE = ( 
        ("Like", "Like"),
        ("Comment", "Comment"),
        ("Bookmark", "Bookmark")
)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    type = models.CharField(choices=NOTI_TYPE, max_length=100)
    seen = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    # neu post ton tai thi hien thi ten bai viet, nguoc lai thi hien thi "Notification"
    def __str__(self):
        if self.post:
            return f"{self.post.title} - {self.type} "
        else:
            return "Notification"
        
    class Meta:
        ordering = ["-date"]
        verbose_name_plural = "Notification"
    
