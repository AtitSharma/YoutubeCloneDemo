from django.contrib import admin

# Register your models here.


from video_player_app.models import User,Video,Channel,Like,Comment,Subscribe

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=["username","email",'description',"photo"]

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display=["title","discription","video_file"]

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display=["name","description","user"]


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display=["is_liked","user","video"]

@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display=["is_subscribed","user","channel"]




    
    # def get_video_count(self, obj):
    #     return obj.videos.count()
    # get_video_count.short_description = "Number of videos"
    
    # def get_subscriber_count(self, obj):
    #     return obj.subscribers.all().count()
    # get_subscriber_count.short_description = "Number of subscribers"