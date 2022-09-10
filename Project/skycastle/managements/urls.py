from django.urls import path
from . import views

urlpatterns = [
    path("", views.start, name="start"),
    path("oauth/", views.Kakaoview.as_view()),
    path("oauth/callback/", views.Kakaocallback.as_view()),
    path("managements/", views.management, name="management"),
    path("managements/logout/", views.log_out, name="logout"),
]
