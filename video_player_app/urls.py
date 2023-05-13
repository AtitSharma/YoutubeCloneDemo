from django.urls import path
from video_player_app.views import(home,video_detail,comment_video,subscribe_channel,
    like_video,UserLogin,register,user_logout,upload_video,view_channel)

app_name="video"
urlpatterns = [
    path("home/",home,name="home"),
    path("video-detail/<int:id>/",video_detail,name="video_detail"),
    path("like-video/<int:id>/",like_video,name="video_like"),
    path("login/",UserLogin.as_view(),name="login"),
    path("register/",register,name="register"),
    path('comment/<int:id>/',comment_video,name="comment"),
    path('subsribe/<str:username>/<int:pk>',subscribe_channel,name="subscribe"),
    path("logout/",user_logout,name="logout"),
    path("upload-video/",upload_video,name="upload_video"),
    path("view_channel/<str:username>/",view_channel,name="view_channel")
]
