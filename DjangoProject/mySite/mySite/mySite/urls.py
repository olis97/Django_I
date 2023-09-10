from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("personal/", include("personal.urls")),
    path("admin/", admin.site.urls),
]