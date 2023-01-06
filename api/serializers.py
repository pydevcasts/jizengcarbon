from rest_framework.serializers import ModelSerializer
from newsletters.models import NewsLetter
from django.contrib.auth import get_user_model
User = get_user_model()


class NewsLetterSerializer(ModelSerializer):
    class Meta:
        model = NewsLetter
        fields = '__all__'