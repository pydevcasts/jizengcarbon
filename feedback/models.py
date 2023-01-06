from django.db import models
from painless.models.mixins import OrganizedMixin
from painless.models.managers import PostPublishedManager
from ckeditor.fields import RichTextField

from painless.models.validations import validate_file_extension, validate_file_size




class CustomerFeedback(OrganizedMixin):
    title = None
    slug = None
    first_name = models.CharField(max_length = 128)
    last_name = models.CharField(max_length = 128)
    role = models.CharField(max_length = 128)
    banner = models.ImageField(upload_to = 'feedback/%Y/%m/%d', null = True, blank = True, validators=[validate_file_extension, validate_file_size])
    content = RichTextField(blank=True,null=True)

    objects = PostPublishedManager()

    class Meta:
        ordering = ['-published_at', 'first_name']
        verbose_name = "feedback"
        verbose_name_plural = "feedbacks"
        get_latest_by = ['-published_at']
    
    
    def __str__(self):
        return self.first_name
        
    

