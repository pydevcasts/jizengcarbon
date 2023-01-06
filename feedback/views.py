
from django.shortcuts import render
from django.views.generic import ListView
from .models import CustomerFeedback
from django.views.generic import ListView
from django.shortcuts import render


class CustomerFeedbackListView(ListView):
    def get(self, request, *args, **kwargs):
        customer_feedbacks = CustomerFeedback.objects.filter(status= 1).order_by('-published_at')
        return render (request, 'frontend/landing/home.html', {
            'feedbacks':customer_feedbacks,
        })