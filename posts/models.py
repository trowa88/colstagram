from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


def set_image_filename(filename):
    now = datetime.now()
    return '{0}_{1}'.format(
        now.strftime('%Y%m%d-%H:%M:%S%f'),
        filename
    )


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(
        instance.user.id,
        set_image_filename(filename)
    )


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_constraint=False)
    contents = models.TextField()
    is_enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'post'
        indexes = [
            models.Index(fields=['updated_at'], name='idx_01'),
        ]

    def __str__(self):
        return self.id


class PostImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_constraint=False)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, db_constraint=False)
    image = models.ImageField(upload_to=user_directory_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'post_image'

    def __str__(self):
        return f'id={self.id}, post_id={self.post_id}'
