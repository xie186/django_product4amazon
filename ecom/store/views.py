from django.shortcuts import get_object_or_404, render

from .models import Category, Product, Carousel, LightingDeal
from django.views.generic.list import ListView


def product_all(request):
    products = Product.products.all()
    carousel = Carousel.objects.all()
    lightingdeal = LightingDeal.objects.all()
    return render(request, 'store/index.html', {'products': products, 'carousels': carousel, 'lightingdeals': lightingdeal})

#class Index(ListView):
#    model = Carousel
#    template_name="store/index.html"
#    products = Product.products.all()
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['nav_status_home'] = "active"
#        return context

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/single.html', {'product': product})
