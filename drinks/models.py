from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class drink(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=200, default ='')
    description = models.TextField()
    ingredients = models.TextField( default = '')
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='drinks', null=True,  default=None)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def get_absolute_url(self):
        return reverse("drinks-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title