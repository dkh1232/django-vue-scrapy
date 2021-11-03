from django.contrib import admin
from ygdy.models import User,Movie
from comment.models import Comment
# Register your models here.
admin.site.register(Movie)
admin.site.register(Comment)
