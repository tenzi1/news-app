
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("articles/", include("articles.urls")),
    path("accounts/", include("django.contrib.auth.urls") ),
    path("accounts/", include("accounts.urls")),
    path("", include('pages.urls')),
]
