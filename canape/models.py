from django.db import models
from django.conf import settings


class Canape(models.Model):
    maker = models.ForeignKey(
                settings.AUTH_USER_MODEL,
                on_delete=models.CASCADE,
    )
    title = models.CharField(
                max_length=200,
    )
    image = models.ImageField(
                upload_to='image/canape/',
    )
    description = models.TextField()
    is_transferable = models.BooleanField(default=False)
    is_limit = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)


class Code(models.Model):
    gainer = models.ForeignKey(
                settings.AUTH_USER_MODEL,
                on_delete=models.CASCADE,
    )
    canape = models.ForeignKey(
                Canape,
                on_delete=models.CASCADE,
    )
    code = models.CharField(
                max_length=16,
                unique=True,
    )
    serial = models.IntegerField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
