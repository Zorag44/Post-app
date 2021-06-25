from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=100)
    contents=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=CASCADE)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog1_index')

class profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self,*args,**kwargs):
        super(profile,self).save(*args,**kwargs)
        img=Image.open(self.image.path)
        if img.width>300 or img.height>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
