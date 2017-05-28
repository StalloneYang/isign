from django.db import models
# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True, null=False)
    user_name = models.CharField(max_length=32, null=False)
    user_pass = models.CharField(max_length=255, null=False)
    user_email = models.EmailField(max_length=255)
    user_phone = models.CharField(max_length=11)

    def __str__(self):
        return self.user_name

class Site(models.Model):
    site_id = models.AutoField(primary_key=True, null=False)
    site_name = models.CharField(max_length=255, null=False)
    site_url = models.CharField(max_length=255, null=False)

class Sign(models.Model):
    sign_id = models.AutoField(primary_key=True, null=False)
    site_id = models.IntegerField(max_length=11)
    site_name = models.CharField(max_length=255, null=False)
    site_pass = models.CharField(max_length=255, null=False)
    site_time = models.TimeField()
    user_id = models.IntegerField(max_length=11, null=False)

class Detail(models.Model):
    detail_id = models.AutoField(primary_key=True, null=False)
    sign_id = models.IntegerField(max_length=11, null=False)
    sign_status = models.CharField(max_length=32)
    detail_time = models.DateTimeField()
    detail_points = models.IntegerField(max_length=11)