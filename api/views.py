from django.contrib.auth import get_user_model
from rest_framework.response import Response
from api.serializers import NewsLetterSerializer
from newsletters.models import NewsLetter, decrypt_email
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

User = get_user_model()



@method_decorator(csrf_exempt, name='dispatch')
class NewsLetterView(APIView):
    def post(self, request):
        serializer = NewsLetterSerializer(data = request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 401)


@method_decorator(csrf_exempt, name='dispatch')
class UnsubscribeView(APIView):
    def get(self, request, unsubscribe_token, *args, **kwargs):
        email = decrypt_email(unsubscribe_token)
        try :
            email_obj = NewsLetter.objects.get(email = email)
        except NewsLetter.DoesNotExist:
            return Response({
                "error": "ایمیل وجود ندارد"
            }, status = 404
            )

        email_obj.delete()
        return Response({
            "message":"unsubscribed."
        }, status = 204)