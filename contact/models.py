import uuid
from django.db import models
from django.core.validators import validate_email

class Contact(models.Model):
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    subject = models.CharField(max_length = 128)
    email = models.EmailField(validators = [validate_email])
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        ordering = ['-created', 'subject']
        verbose_name = "contact"
        verbose_name_plural = "contacts"
        get_latest_by = ['-created']

    def __str__(self):
        return self.subject




class Location(models.Model):
    address = models.CharField(max_length=200, null = True)
    date = models.DateTimeField(auto_now_add = True)
    class Meta:
        verbose_name = "map"
        verbose_name_plural = "maps"

    def __str__(self):
        return self.address