from painless.models.mixins import TimeStampedMixin
from django.db import models
from django.templatetags.static import static
from django.contrib.auth import get_user_model
from painless.models.validations import validate_postal_code,validate_national_code
User = get_user_model()




class Profile(TimeStampedMixin):
  
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatar/%Y/%m/%d",  null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    code = models.CharField(validators=[validate_national_code], blank=True, null = True, max_length= 20)
    phone = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    zip = models.CharField(max_length=30, null=True, blank=True,validators=[validate_postal_code])
    instagram = models.URLField(blank = True, null = True)
    whatsapp = models.URLField(blank = True, null = True)
    linkedin = models.URLField(blank = True, null = True)
    about = models.TextField(null = True, blank = True)


    class Meta:
        verbose_name = "profile"
        verbose_name_plural = "profiles"

    def __str__(self):
        return self.user.email

    @property
    def get_avatar(self):
        return self.avatar.url if self.avatar else static('../static/assets/backend/img/team/profile-picture-1.jpg')

