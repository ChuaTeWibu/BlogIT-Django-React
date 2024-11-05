from django.contrib import admin # module admin
from django.urls import path,include # import path, include
from django.conf import settings # import settings
from django.conf.urls.static import static # import static

# swagger
from rest_framework import permissions # rest_framework la thu vien de tao API cho Django, permissions la module trong rest_framework dung de xac thuc quyen truy cap
from drf_yasg.views import get_schema_view #get_schema_view la ham trong drf_yasg dung de tao ra swagger
from drf_yasg import openapi   # openapi la module trong drf_yasg dung de tao ra swagger

# tao ra swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Blog Backend APIs",  # ten cua API
        default_version="v1",  # version cua API
        description="Day la tai lieu danh cho APIs cua Blog Backend",  # mo ta chung ve API
        terms_of_service="https://www.facebook.com/profile.php?id=100085808780556",  # dieu khoan su dung
        contact=openapi.Contact(email="tytybill123@.gmail.com"),  # email lien he
        license=openapi.License(name="BSD Licence"),  # giay phep
    ),
    public=True,  # public thi moi co the truy cap duoc
    permission_classes = (permissions.AllowAny, )  # cho phep truy cap cho moi nguoi
)

# Danh sach cac URL trong project
urlpatterns = [
    # URL cho swagger UI
    # schema_view la mot ham tao ra swagger UI
    # with_ui la mot phuong thuc cua schema_view dung de chon giao dien cho swagger UI
    # cache_timeout la thoi gian luu tru cache, neu la 0 thi moi lan reload thi se load lai swagger UI
    # name la ten cua URL, duoc dung de reverse URL
    path("", schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    # URL cho admin
    path('admin/', admin.site.urls),
    # URL cho API
    # include la mot ham trong django.urls dung de nhap URLconf cua app khac vao project
    # "api.urls" la ten cua URLconf cua app api
    path('api/v1/', include("api.urls")),
]

# Them cac URL cho MEDIA va STATIC
# static la mot ham trong django.conf.urls.static dung de them cac URL cho MEDIA va STATIC
# MEDIA_URL la URL cua MEDIA, MEDIA_ROOT la thu muc luu tru MEDIA
# STATIC_URL la URL cua STATIC, STATIC_ROOT la thu muc luu tru STATIC
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

