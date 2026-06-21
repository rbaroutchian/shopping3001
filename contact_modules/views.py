from django.shortcuts import render
from .form import ContactModelForm
from django.views import View
from django.shortcuts import redirect
# from django.views.generic.edit import FormView, CreateView

# Create your views here.
class ContactView(View):
    def get(self, request):
        contact_form = ContactModelForm()
        return render(request, 'contact_modules/contact_page.html', {
            'contact_form': contact_form,
        })

    def post(self, request):
        contact_form = ContactModelForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('product_list')
        return render(request, 'contact_modules/contact_page.html', {
            'contact_form': contact_form,
        })
