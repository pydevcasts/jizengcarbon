import datetime
from django import forms
from django.utils.translation import gettext_lazy as _
from users.models import Profile
from django import forms
import string
from django.contrib.auth import get_user_model

User = get_user_model()


class UserForm(forms.ModelForm):
    model = User
    fields = ['first_name', 'last_name', 'email', 'mobile']

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="Firstname", max_length=16)
    last_name = forms.CharField(label="Lastname", max_length=255)
    mobile = forms.CharField(label="Cellphone", max_length=255)
    email = forms.EmailField(label="Email")

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', 'published_at','instagram','whatsapp', 'linkedin', 'birthday', 'about']
        widgets = {
            'birthday': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }



    def clean_first_name(self):

        letters = set(string.punctuation)
        digits = set(string.digits)
        data = self.cleaned_data.get('first_name')
        v = set(data)
        if not v.isdisjoint(letters) or not v.isdisjoint(digits):
            raise forms.ValidationError('Only character is acceptible')
        if len(data) < 3:
            raise forms.ValidationError("Length not must be less than 3 character")
        return data



    def clean_last_name(self):

        letters = set(string.punctuation)
        digits = set(string.digits)
        data = self.cleaned_data.get('last_name')
        v = set(data)
        if not v.isdisjoint(letters) or not v.isdisjoint(digits):
            raise forms.ValidationError('Only character is acceptible')
        if len(data) < 3:
            raise forms.ValidationError("Length not must be less than 3 character")
        return data

 

    def clean_birthday(self):
        data = self.cleaned_data.get('birthday')
        if data != None and data > datetime.date.today():
            raise forms.ValidationError(
                    """
                    \'to\'Birthday must be less than today.
                    """)



def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg



