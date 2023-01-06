from django.db import models
from painless.models.mixins import OrganizedMixin
from painless.models.managers import PostPublishedManager
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from painless.models.validations import validate_file_extension, validate_file_size



class About(OrganizedMixin):
    summary = models.CharField(max_length = 128, blank = True, null = True)
    banner = models.ImageField(upload_to = 'about/%Y/%m/%d', null = True, blank = True, validators=[validate_file_extension, validate_file_size])
    content = RichTextField(blank=True,null=True)
    
    objects = models.Manager()

    class Meta:
        verbose_name = "about"
        verbose_name_plural = "abouts"
     

    def __str__(self):
        return self.title

    
    