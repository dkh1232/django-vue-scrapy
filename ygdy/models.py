from django.db import models
# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User

class  Category(models.Model):
    big_title = models.CharField(max_length=100)
    def __str__(self):
        return self.big_title

class Movie(models.Model):
    title = models.CharField(max_length=200,verbose_name='标题')
    img = models.CharField(max_length=200)
    tran_name = models.CharField(max_length=200)
    name  = models.CharField(max_length=200)
    year  = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    douban_rate = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    publish_date = models.CharField(max_length=200)
    movie_time = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    main_actor = models.CharField(max_length=200)
    download_url = models.CharField(max_length=2000)
    created = models.DateTimeField(default=timezone.now)
    lookuser = models.ManyToManyField(User,blank=True,related_name='userlike_movie')
    class Meta():
        db_table = 'Movie'
        verbose_name = '电影'
        verbose_name_plural = verbose_name
    def __srt__(self):
        return self.title

# class UserLike(models.Model):



