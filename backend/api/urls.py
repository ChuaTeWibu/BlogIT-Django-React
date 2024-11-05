from django.urls import path # su dung de tao url       
from rest_framework_simplejwt.views import TokenRefreshView # su dung de refresh token
from api import views as api_views # su dung de lay view


urlpatterns = [
    
    ################ User Endpoints ################
    # as_view() chuyển đổi class-based view thành function-based view
    # Django yêu cầu view phải là một function
    
    # URL để lấy JWT token khi đăng nhập
    # POST /api/user/token/
    # Request body: {"username": "...", "password": "..."}
    # Response: {"access": "access_token...", "refresh": "refresh_token..."}
    
    path('user/token/', api_views.MyTokenObtainPairView.as_view()), # Dang Nhap

    # URL để làm mới access token khi hết hạn
    # POST /api/user/token/refresh/
    # Request body: {"refresh": "refresh_token..."}
    # Response: {"access": "new_access_token..."}
    path('user/token/refresh/', TokenRefreshView.as_view()), # Refresh Token

    # URL để đăng ký tài khoản mới
    # POST /api/user/register/
    # Request body: {"username": "...", "password": "...", "email": "...", ...}
    # Response: Thông tin user mới tạo
    
    # Khi có request đến, as_view() sẽ:
    # 1. Tạo một instance của class RegisterView
    # 2. Gọi phương thức phù hợp (get/post/put...) dựa vào HTTP method
    path('user/register/', api_views.RegisterView.as_view()), # Dang Ky

    # URL pattern định nghĩa tham số user_id
    path('user/profile/<user_id>/', api_views.ProfileView.as_view()), # Xem Profile
    # Khi truy cập: /api/profile/123/
    # self.kwargs sẽ là: {'user_id': 123}
    
    
    
    
    ################ Post Endpoints ################
    path('post/category/list', api_views.CategoryListAPIView.as_view()), # Xem Bai Viet Theo Danh Muc
    path('post/category/post/<category_slug>/', api_views.PostCategoryListAPIView.as_view()), # Xem Bai Viet Theo Danh Muc
    path('post/lists/', api_views.PostListAPIView.as_view()), # Xem Bai Viet Theo Danh Muc
    path('post/detail/<slug>/', api_views.PostDetailAPIView.as_view()), # Xem Bai Viet Theo Danh Muc
    path('post/like-post/', api_views.LikePostAPIView.as_view()), # Like bai viet 
    path('post/comment-post/', api_views.PostCommentAPIView.as_view()), # Comment bai viet
    path('post/bookmark-post/', api_views.BookmarkPostAPIView.as_view()),
    
]




