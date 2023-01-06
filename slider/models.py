from django.db import models
from painless.models.mixins import OrganizedMixin
from painless.models.managers import PostPublishedManager
from ckeditor.fields import RichTextField



class Slider(OrganizedMixin):
    summary = models.CharField(max_length = 128)
    banner = models.ImageField(upload_to = 'slider/%Y/%m/%d', null = True, blank = True)
    content = RichTextField(blank=True,null=True)
    
    condition = PostPublishedManager()

    class Meta:
        verbose_name = "slider"
        verbose_name_plural = "sliders"
     
    def __str__(self):
        return self.title

    
    