from logging import exception
import uuid
import markdown2
import jwt
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from painless.models.mixins import  OrganizedMixin, TimeStampedMixin
from django.core.validators import validate_email
from django.contrib.sites.models import Site



class NewsLetter(OrganizedMixin):
    title, slug = None, None
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    subscriber = models.EmailField(max_length = 128, unique = True, validators = [validate_email])
    

    objects = models.Manager()

    class Meta:
        ordering = ['subscriber']
        verbose_name = "newsletter"
        verbose_name_plural ="newsletters"


    def __str__(self):
        return self.subscriber


class ScheduleMail(TimeStampedMixin):
    subject = models.CharField(max_length=255, null = True, blank = True)
    content = models.TextField(max_length=3000)

    class Meta:
        ordering = ['-created']
        verbose_name = "schedulemail"
        verbose_name_plural = "schedulemails"
    
    def __str__(self):
        return self.subject


    @property
    def html_content(self):
        markdown = markdown2.Markdown()
        return markdown.convert(self.content)


def encrypt_email(email: str)->str:
    encode_jwt = jwt.encode({'email':email}, settings.SECRET_KEY)
    return encode_jwt


def decrypt_email(token: str)->str:
    data = jwt.decode(
        token, settings.SECRET_KEY, 
        algorithms = ['HS256'],
        options = {"varify_exp":False},
    )
    
    return data['email']



def generate_unsub_url(token:str, https:bool=False)->str:
    
    try:
        site = Site.objects.get(name = "127.0.0.1:8000")
    except Site.DoesNotExist:
        raise Exception("Site does not exists")

    full_domain = f"http{'s' if https else ''}://{site.domain}"
    return f"{full_domain}/mail/newsletter/unsubscribe/{token}"
