import os
from django.db.models.signals import pre_save,post_delete
from django.dispatch import receiver
from product.models import Product
from django.utils.text import slugify


@receiver(post_delete, sender=Product)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.banner_1:
        if os.path.isfile(instance.banner_1.path):
            os.remove(instance.banner_1.path)
    if instance.banner_2:
        if os.path.isfile(instance.banner_2.path):
            os.remove(instance.banner_2.path)
    if instance.banner_3:
        if os.path.isfile(instance.banner_3.path):
            os.remove(instance.banner_3.path)




@receiver(pre_save, sender=Product)
def auto_delete_file_on_change_banner_1(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = Product.objects.get(pk=instance.pk).banner_1
    except Product.DoesNotExist:
        return False
    if not old_file:
        return
    new_file = instance.banner_1
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


@receiver(pre_save, sender=Product)
def auto_delete_file_on_change_banner_3(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = Product.objects.get(pk=instance.pk).banner_3
    except Product.DoesNotExist:
        return False
    if not old_file:
        return
    new_file = instance.banner_3
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


@receiver(pre_save, sender=Product)
def auto_delete_file_on_change_banner_2(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = Product.objects.get(pk=instance.pk).banner_2
    except Product.DoesNotExist:
        return False
    if not old_file:
        return
    new_file = instance.banner_2
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)



@receiver(pre_save,sender=Product)
def create_product(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=create_uniqe_slug(instance)


def create_uniqe_slug(instance,newslug=None):
    if newslug is not None:
        slug=newslug
    else:
        slug=slugify(instance.title,allow_unicode=True)

    instanClass=instance.__class__
    qs=instanClass.objects.filter(slug=slug)

    if qs.exists():
        newslug=f"{slug}-{qs.first().id}"
        return create_uniqe_slug(instance,newslug)

    return slug
   