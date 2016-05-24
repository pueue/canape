from django.db import models

class Postage(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField()
	description = models.TextField()
	is_transferable = models.BooleanField()
	is_limit = models.BooleanField()
	quantity = models.IntagerField()
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
