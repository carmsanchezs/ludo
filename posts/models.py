"""Post models."""

# Django
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Post model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    content = models.TextField()
    url_reference = models.URLField()

    labels = models.CharField(max_length=500)
    order = models.IntegerField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""

        return '{} by @{}'.format(self.title, self.user.username)



class Comment(models.Model):
    """Comment model."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE, null=True, blank=True)
    is_approved = models.BooleanField(default=True)

    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    