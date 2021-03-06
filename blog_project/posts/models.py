from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, related_name="posts",
                             on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title
