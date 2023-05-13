from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo=models.ImageField(upload_to='userphotos',blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    class Meta:
        verbose_name="User"
        verbose_name_plural="Users"
    def __str__(self):
        return self.username

    def save(self,*args,**kwargs):
        is_new_user=self.pk
        if is_new_user:
            Channel.objects.create(name=f"{self.username}'s Channel",
            description="My channel Description",
            user=self)
        super(User, self).save(*args, **kwargs)

class Video(models.Model):
    title=models.CharField(max_length=255)
    discription=models.TextField(blank=True,null=True)
    upload_date=models.DateTimeField(auto_now_add=True)
    video_file = models.FileField(upload_to='videos/')
    thumbnail=models.ImageField(upload_to='videos/')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="video")

    def __str__(self):
        return str(self.title)

    @property
    def likes_count(self):
        return self.likes.filter(is_liked=True).count()



class Channel(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="channel")
    videos = models.ManyToManyField(Video,related_name="channel")
    def __str__(self):
        return self.name
    
    @property
    def subscribe_count(self):
        return self.subsribe.filter(is_subscribed=True).count()






    
class Comment(models.Model):
    description=models.CharField(max_length=255)
    video=models.ForeignKey(Video,on_delete=models.CASCADE,related_name="comments")
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="comments")

    def __str__(self):
        return str(self.description)
     
class Like(models.Model):
    is_liked=models.BooleanField(default=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="likes")
    video=models.ForeignKey(Video,on_delete=models.CASCADE,related_name="likes")
    def _str__(self):
        return str(self.id)

class Subscribe(models.Model):
    is_subscribed=models.BooleanField(default=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="subsribe")
    channel=models.ForeignKey(Channel,on_delete=models.CASCADE,related_name="subsribe")
    
    def _str__(self):
        return str(self.id)

   


