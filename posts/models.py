from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    img = models.ImageField(upload_to='posts')
    caption = models.TextField()#default="-"
    likes = models.IntegerField(default=0)
    datetime = models.DateTimeField(default=timezone.now())
# p_id = models.AutoField(validators=[])

    def __str__(self):
        return f"{self.user.username} Post"

    def get_absolute_url(self):
        return reverse('profile')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.img.path)
        if img.height >500 or img.width > 500:
            output_size = (500,500)
            img.thumbnail(output_size)
            img.save(self.img.path)

class Like(models.Model):
    post = models.ForeignKey(Post,on_delete= models.CASCADE)
    like_by = models.ForeignKey(User,on_delete= models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now())
    

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(blank=False,max_length=300)
    datetime = models.DateTimeField(default=timezone.now())