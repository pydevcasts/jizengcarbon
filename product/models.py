import uuid
from django.db import models
from django.conf import settings
from django.urls.base import reverse
from comment.models import Comment
from painless.models.mixins import OrganizedMixin
from painless.models.managers import PostPublishedManager
from tag.models import Tag
from category.models import Category
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType





class Product(OrganizedMixin):
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = '+', on_delete = models.CASCADE,verbose_name = _("نویسنده"))
    summary = models.CharField(max_length = 128)
    banner_1 = models.ImageField(upload_to = 'product/%Y/%m/%d', null = True, blank = True)
    banner_2 = models.ImageField(upload_to = 'product/%Y/%m/%d', null = True, blank = True)
    banner_3 = models.ImageField(upload_to = 'product/%Y/%m/%d', null = True, blank = True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name = 'products')
    views= models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, related_name = 'tags',  blank = True)
    content = RichTextField(blank=True,null=True)
    comments = GenericRelation(Comment)

    objects = PostPublishedManager()

    class Meta:
        ordering = ['-published_at']
        verbose_name = "product"
        verbose_name_plural = "products"
        get_latest_by = ['-published_at']
    

    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse("product:detail", args=[self.published_at.year,
                             self.published_at.month,
                             self.published_at.day, 
                             self.slug])
    
    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type
    

    




