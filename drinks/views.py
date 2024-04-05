from django.forms import BaseModelForm
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import drink
from django.urls import reverse_lazy
from . import models
from django.views.decorators.csrf import csrf_protect


# Create your views here.
def home(request):
    drinks = models.drink.objects.all()
    context = {
        'drinks':drinks
    }
    return render(request, "drinks/home.html", context)
    
class DrinkListView(ListView):
    model =models.drink
    template_name = 'drinks/home.html'
    context_object_name ='drinks'

class DrinkDetailView(DetailView):
    model=models.drink

class DrinkCreateView( LoginRequiredMixin, CreateView):#over riding the form valid method
    model = models.drink
    fields=['title','description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class DrinkUpdateView( LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = models.drink
    fields=['title','description']

    def test_func(self):
        drink = self.get_object()
        return self.request.user == drink.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class DrinkDeleteView( LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = models.drink
    success_url=  reverse_lazy('drinks-home')
    template_name = 'drinks/drink_confirm_delete.html'

    def test_func(self):
        drink = self.get_object()
        return self.request.user == drink.author

    

def about(request):
    return render(request, "drinks/about.html",{'title':'about us page'})
    