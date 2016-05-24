from django.db import models

class Postage(models.Model):
	title = models.CharField(
				max_length=200,
	)
	image = models.ImageField(
				upload_to='image/postage/',
	)
	description = models.TextField()
	is_transferable = models.BooleanField(default=False)
	is_limit = models.BooleanField(default=False)
	quantity = models.IntegerField()
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
