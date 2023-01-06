from django import forms
from product.models import Product



class ProductForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'ckeditor'}))
    class Meta:
        model = Product
        exclude=("slug","published_at")


    def clean_title(self):
        data = self.cleaned_data.get('title')
        if len(data) < 5:
            raise forms.ValidationError("The length must not be less than 5 character")
        return data

    def clean_summary(self):
        data = self.cleaned_data.get('summary')
        if len(data) < 10:
            raise forms.ValidationError("The length must not be less than 10 character")
        return data





           