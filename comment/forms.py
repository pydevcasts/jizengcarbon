
from django import forms
from product.models import Comment
from django.utils.translation import gettext_lazy as _



class CommentForm(forms.ModelForm):

        class Meta:
            model = Comment
            fields = ['content']