from django.db import models

# Create your models here.

class Video(models.Model):
    filename = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.filename

class Animation(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    animation_type = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    font = models.CharField(max_length=200)
    font_size = models.IntegerField(default=11)
    pos_top = models.IntegerField(default=100)
    pos_left = models.IntegerField(default=50)
    time_app = models.IntegerField(default=10)
    time_dis = models.IntegerField(default=10)
    size_w = models.CharField(max_length=5,blank=True)
    size_h = models.CharField(max_length=5,blank=True)
    path = models.CharField(max_length=200,blank=True)
    is_image = models.BooleanField(default=False)

    def __str__(self):
        return self.text
