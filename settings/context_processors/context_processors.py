

from category.models import Category
from django.contrib.auth import get_user_model
from django.db.models import Q

from product.models import Product
User = get_user_model()



def products_view_context_processor(request):
    users = User.objects.filter(email = "siyamak1981@gmail.com", is_active = True, is_superuser = True)
    categories = Category.objects.all().filter(status = "1")
   
    q = request.GET.get("q")
    if q:
        searchs = Product.objects.filter(Q(title__icontains=q) | Q(content__icontains=q) | Q(summary__icontains = q))
    else:
        searchs = ""   
 
    return ({'users':users, "categories":categories, "searchs":searchs })

