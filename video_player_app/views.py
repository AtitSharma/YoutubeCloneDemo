from django.shortcuts import render,get_object_or_404,redirect,reverse
from .models import Video,Channel,User,Like,Comment,Subscribe
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import UserRegisterForm,UserCommentForm,UserUploadVideoForm
# from django.db.models import Count
# Create your views here.
def home(request):
    videos=Video.objects.all()
    return render(request,"home.html",{"videos":videos})


def video_detail(request,id):
    videos=Video.objects.filter(id=id)

    return render(request,"video_detail.html",{"videos":videos})

@login_required
def like_video(request,id):
    video=get_object_or_404(Video,id=id)
    user=request.user
    like,created=Like.objects.get_or_create(video=video,user=user)
    if not created:
        if like.is_liked==True:
            like.is_liked=False
        else:
            like.is_liked=True
        like.save()
    total_likes=video.likes.filter(is_liked=True).count()
    return HttpResponseRedirect(reverse("video:video_detail",args=(id,)))



class UserLogin(LoginView):
    template_name="login.html"


def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("video:login")
    else:
        form=UserRegisterForm()
    return render(request,"register.html",{"form":form})



def comment_video(request,id):
    video=get_object_or_404(Video,id=id)
    if request.method=="POST":
        form=UserCommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.video=video
            comment.user=request.user
            comment.save()
            return HttpResponseRedirect(reverse("video:comment",args=(id,)))
    else:
        form=UserCommentForm()
    comments=Comment.objects.filter(video__id=id)
    context={
        "form":form,
        "comments":comments,
    }
    return render(request,"comment.html",context)
    
@login_required
def subscribe_channel(request,username,pk):
    id=Channel.objects.get(user__username=username).id
    channel=get_object_or_404(Channel,id=id)
    user=request.user
    subscribe,created=Subscribe.objects.get_or_create(channel=channel,user=user)
    if not created:
        if subscribe.is_subscribed==True:
            subscribe.is_subscribed=False
        else:
            subscribe.is_subscribed=True
        subscribe.save()
    total_subscribe=channel.subsribe.filter(is_subscribed=True).count() 
    return HttpResponseRedirect(reverse("video:video_detail",args=(pk,)))




def user_logout(request):
    logout(request)
    return redirect("video:login")


@login_required
def upload_video(request):
    print(request.POST)
    if request.method=="POST":
        form=UserUploadVideoForm(request.POST,request.FILES)
        if form.is_valid():
            video=form.save(commit=False)
            video.user=request.user
            video.save()
            return redirect("video:home")
        else:
            print("HELLO")
            print(form.errors)
    else:
        form=UserUploadVideoForm()
    return render(request,'upload_video.html',{"form":form})



def view_channel(request,username):
    videos=Video.objects.filter(user__username=username)
    subscribers=Channel.objects.get(user__username=username).subscribe_count
    context={
        "videos":videos,"username":username,
        "subscribers":subscribers
    }
    return render(request,"view_channel.html",context)

