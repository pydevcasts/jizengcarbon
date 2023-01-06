from django.db import models
from painless.models.mixins import OrganizedMixin
from ckeditor.fields import RichTextField
from painless.models.validations import validate_file_extension, validate_file_size


class Member(OrganizedMixin):
    title = None
    slug = None
    first_name = models.CharField(max_length=128, null = True, blank = True)
    last_name = models.CharField(max_length=128, null = True, blank = True)
    role = models.CharField(max_length=128, null = True, blank = True)
    phone = models.CharField(max_length=128, null = True, blank = True)
    banner = models.ImageField(upload_to = 'memnber/%Y/%m/%d', null = True, blank = True, validators=[validate_file_extension, validate_file_size])
    instagram = models.URLField(blank = True, null = True)
    whatsapp = models.URLField(blank = True, null = True)
    linkedin = models.URLField(blank = True, null = True)
    content = RichTextField(blank=True,null=True)
    team = models.ForeignKey("Team", on_delete=models.CASCADE, blank = True, null = True, related_name="team")
    
    class Meta:
        verbose_name = "member"
        verbose_name_plural = "members"
    def __str__(self) -> str:

        return f"member:{self.first_name}-{self.last_name}"



class Team(OrganizedMixin):
    slug = None
    summary = models.CharField(max_length = 128)
    content = RichTextField(blank=True,null=True)
  
    class Meta:
        verbose_name = "team"
        verbose_name_plural = "teams"
    
    def __str__(self):
        return self.title