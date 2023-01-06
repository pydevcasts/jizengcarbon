from django.urls import re_path, include
from rest_framework import routers 
from api.views import NewsLetterView


router = routers.DefaultRouter()




urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^newsletter/',NewsLetterView.as_view(), name = "subscribe"),

    
]
