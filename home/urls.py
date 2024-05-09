from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("profile/", views.profileview, name="profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
