from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views
from .views import PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("profile/", views.profileview, name="profile"),
    path("insurance/", views.insurance, name="insurance"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
