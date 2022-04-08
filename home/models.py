from django.db import models
from django.contrib.auth.models import User # model User
from django.conf import settings
from django.utils.timezone import now

# tag cua bai viet
class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=256)
    thumbnail = models.ImageField(null=True)
    summary = models.CharField(max_length=1024)
    content = models.TextField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    # format data 
    # @admin.display
    # def colored_name(self):
    #     return format_html(
    #         '<span style="color: #{};">{} {}</span>',
    #         self.color_code,
    #         self.first_name,
    #         self.last_name,
    #     )

