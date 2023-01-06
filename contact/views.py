import folium
import geocoder
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls.base import  reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, DeleteView,UpdateView
from contact.models import Contact, Location
from contact.forms import ContactForm
from django.db.models import Q
from django.contrib.auth import get_user_model
User = get_user_model()
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings



class ListContactView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Contact
    permission_required = "contact.view_contact"
    context_object_name = 'contacts'
    template_name = 'dashboard/contact/list.html'
    paginate_by = 10

    def handle_no_permission(self):
        messages.warning(self.request, "You dont have permission to this page ")
        return redirect("dashboard:home")


    def get_queryset(self):
        filter_val = self.request.GET.get("filter", "")
        order_by = self.request.GET.get("orderby", "pk")
        if filter_val != "":
            contact = Contact.objects.filter(Q(title__contains=filter_val) | Q(
                description__contains=filter_val)).order_by(order_by)
        else:
            contact = Contact.objects.all().order_by(order_by)

        return contact

    def get_context_data(self, **kwargs):
        context = super(ListContactView, self).get_context_data(**kwargs)
        context["filter"] = self.request.GET.get("filter", "")
        context["orderby"] = self.request.GET.get("orderby", "pk")
        context["all_table_fields"] = Contact._meta.get_fields()
        context["segment"] = "contacts"
        return context


class CreateContactView(SuccessMessageMixin , CreateView):
    def post(self, request, *args, **kwargs):
            if request.method == 'POST':
                form = ContactForm(request.POST)
                if form.is_valid():
                    subject = form.cleaned_data["subject"]
                    from_email = form.cleaned_data["email"]
                    message = form.cleaned_data['content']
                    try:
                        send_mail(subject, message, from_email,('pydevcasts@gmail.com',),fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse("Invalid header found.")
                    form.save()
                    messages.success(request,
                                    "Your message is created successfully!")
                    return redirect("contact:contact-create")
            else:
                form = ContactForm()
            return render(request, 'frontend/contact/index.html',
                        {'form': form } 
                    )


    def get(self, request, **kwargs):
        user = User.objects.get(email = "pydevcasts@gmail.com", is_active = True, is_superuser = True)

        address = Location.objects.all().last()
        location = geocoder.osm(address)
        lat = location.lat
        lng = location.lng
        country = location.country
        map = folium.Map(location=[19,-12], zoom_start=2)
    
        folium.Marker([lat,lng],tooltip="click for more",popup = country).add_to(map)
        map = map._repr_html_()
        return render(request, 'frontend/contact/index.html',
                        {'map':map, 'segment': 'contact', 'user':user,"title": "contact"}
                        )




class DeleteContactView(SuccessMessageMixin, PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Contact
    permission_required = "contact.delete_contact"
    template_name = 'dashboard/contact/list.html'
    success_url = reverse_lazy('contact:list')
    success_message = "Contact Delete successfully"


    def handle_no_permission(self):
        messages.warning(self.request, " You dont have permission to this page ")
        return redirect("dashboard:home")

    def get(self, request, *args, **kwargs):
        pk=kwargs.get("pk")
        if pk is not None:
            Contact_object = Contact.objects.get_queryset().filter(pk= pk)
            if Contact_object is not None:
                Contact_object.delete()
                messages.success(request, "Your Message is delete successfully")
                return redirect('contact:contact-list')
        return redirect('dashboard/Contact/list.html')
       


class ContactShowView(SuccessMessageMixin,PermissionRequiredMixin, LoginRequiredMixin,UpdateView):
    permission_required = "contact.update_contact"
    model = Contact
    template_name = 'dashboard/contact/show.html'
    fields = "__all__" 
    success_url = reverse_lazy('contact:contact-list')
    
    def handle_no_permission(self):
        messages.warning(self.request, "You dont have permission to this page ")
        return redirect("dashboard:home")

