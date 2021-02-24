from django.db import models
from django.conf import settings

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=200, default=None)
    branch = models.CharField(max_length=200, default=None)
    category = models.CharField(max_length=300,  default=None)
    File_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50, default="")
    upload_date = models.DateTimeField(auto_now_add=True, blank=True)
    uploaded_file = models.FileField(upload_to=settings.MEDIA_ROOT, null=True)

    def __str__(self):
        return self.File_name


