from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q


class UserCommentQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)

    def search(self, query, user=None):
        lookup = Q(first_name__icontains=query) | Q(comment__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs

class UserCommentManager(models.Manager):
    def get_queryset(self, *args,**kwargs):
        return UserCommentQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)


class UserComment(models.Model):
    first_name = models.CharField( max_length=40)
    last_name = models.CharField( max_length=40)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(null=False, max_length=400)
    public = models.BooleanField(default=True)

    objects = UserCommentManager()

    def name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return f"{self.first_name} {self.last_name} : \"{self.comment}\""



from django.core.validators import MinLengthValidator
from django.conf import settings


class Picture(models.Model):
    title = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # Picture
    picture = models.BinaryField(null=True, blank=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, blank=True,
                                    help_text='The MIMEType of the file')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title