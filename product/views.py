
from django.shortcuts import get_object_or_404, render
from comment.forms import CommentForm
from product.models import Comment, Product
from category.models import Category
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib import messages
from newsletters.forms import NewsLettersForm
from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from newsletters.models import NewsLetter, decrypt_email
from django.views.generic.edit import FormMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from slider.models import Slider
from feedback.models import CustomerFeedback
from tag.models import Tag



def product_category_list(request, slug=None):
    category = None
    cats = Category.objects.prefetch_related('products').filter(parent = None)[:9]
    sliders = Slider.condition.filter(status = 1)
    customer_feedbacks = CustomerFeedback.objects.filter(status= 1).order_by('-published_at')
    if request.method == 'POST':
            form = NewsLetter(subscriber=request.POST['subscriber'])
            if NewsLetter.objects.filter(subscriber=form.subscriber).exists():
                messages.error(request," The Email is registred before ")
            else:
                form.save()
                messages.success(request,
                                    "Your Newsletter is registered successfully  !")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
         
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'),
                        {'form': NewsLettersForm() } 
                    )
            
    return render(request, "frontend/landing/home.html", {
                                                    'category':category,
                                                        "cats": cats,
                                                        'sliders':sliders,
                                                        'segment':'Carbon',
                                                        'feedbacks':customer_feedbacks,
                                                        })
def all_product_view(request):
    all_product = Product.objects.all().filter(status= 1).select_related('category').order_by('category_id')
    page = request.GET.get('page', 1)

    paginator = Paginator(all_product, 15)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, "frontend/products/index.html", {"all_product":all_product, "segment":"products", "title":"products", 'page_obj': page_obj})



class ProductDetailView(FormMixin, DetailView):
    template_name = 'frontend/products/detail.html'
    model = Product
    slug_field = 'slug'
    form_class = CommentForm
    obj = None
    list_ip = []

    def get_initial(self):
        instance = self.get_object()
        return {
            'content_type':instance.get_content_type,
            'object_id':instance.uid
        }
    

    def get_success_url(self):
        return reverse("frontend:detail", args=[self.published_at.year,
                             self.published_at.month,
                             self.published_at.day, 
                             self.slug])
  

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        product = get_object_or_404(Product, slug = self.kwargs['slug'])
        comments = Comment.objects.filter_by_instance(product)
        context['comments'] = comments
        context['title'] = product.title
        context['segment'] = "product"
        context['form'] = self.get_form_class()
   
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        self.list_ip.append(ip)
        if ip in self.list_ip:
            product.view = ""
        else:
            product.views += 1
        product.save()
        return context


    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            self.object = self.get_object()
            form = self.get_form_class()
            form = CommentForm(instance=self.obj, data=request.POST)

            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
       

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
                messages.info(self.request,"You need to signup before create a message")
                return HttpResponseRedirect("/signup/")

        user = self.request.user
        comment_content = form.cleaned_data['content']
        Comment.objects.create(
                content_object=Product.objects.get(slug=self.kwargs.get("slug")),
                content=comment_content,
                user=user,
                
            )
        messages.success(self.request, "Yore message is created successfully!")
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
        

    def form_invalid(self, form) -> HttpResponse:
        messages.error(self.request, "There is a problem")
        return super().form_invalid(form)





def unsubscrib_redirect_view(request, token, *args, **kwargs):
        print("token:", token)
        email = decrypt_email(token)
  
        try :
            email_obj = NewsLetter.objects.get(subscriber = email)
            email_obj.delete()
            messages.success(request,"Your unsubscribe was successfully")
        except NewsLetter.DoesNotExist:
            print(
                 " Email Does not exists"
            )
            html_template = loader.get_template('dashboard/dashboard/page-403.html')
            return HttpResponse(html_template.render({"title":"You have subscribed before"}, request))

        return redirect("product:product_and_category")



