from django.db import models
from django.contrib.auth.models import  AbstractUser


class CustomUser(AbstractUser):
    def __str__(self):
        return self.username



class Profile(models.Model):
    objects = None
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=400)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} "


class Post(models.Model):
    objects = None
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    objects = None
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commenter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class Reply(models.Model):
    objects = None
    reply = models.TextField()
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    replier = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reply


class FavoritePost(models.Model):
    objects = None
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s favorite post: {self.post.title}"