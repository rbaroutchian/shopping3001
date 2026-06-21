from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView



# روش اول
# def product_list(request):
#     products = Product.objects.all()
#     context = {'products': products
#                }
#     return render(request, 'product_modules/product_list.html', context)
#
#
# def product_details(request, slug):
#     product = get_object_or_404(Product, slug=slug)
#     return render(request, 'product_modules/product_detail.html',
#                   {'product': product})

# روش دوم
class productListView(TemplateView):
    template_name = 'product_modules/product_list.html'
    def get_context_data(self, **kwargs):
        product = Product.objects.all().order_by('title')[:5]
        context = super(productListView, self).get_context_data(**kwargs)
        context['products'] = product
        return context

# class productDetailView(DetailView):
#     template_name = 'product_moduels/product_detail.html'
#     model = Product
#
#     def get_queryset(self):
#         query = super(productDetailView, self).get_queryset()
#         query = query.filter(is_active=True)
#         return query
#
#     def get_context_data(self, **kwargs):
#         context = super(productDetailView, self).get_context_data(**kwargs)
#         product: Product = kwargs.get('object')
#         return context


class productDetailView(TemplateView):
    template_name = 'product_modules/product_detail.html'
    def get_context_data(self, **kwargs):
        context = super(productDetailView, self).get_context_data()
        slug = kwargs['slug']
        product = get_object_or_404(Product, slug=slug)
        context['product'] = product
        return context

