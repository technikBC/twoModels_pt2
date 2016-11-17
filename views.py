#You dont need all of these imports
from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse
from .models import ModelOne, ModelTwo

class review_page(ListView):
    model = ModelOne #burner line required for class to iterate
    template_name = 'webpage/list_entries.html' #entry like post. url, picture…

    def get_context_data(self,**kwargs):
        ctx = super(review_page, self).get_context_data(**kwargs)
        ctx['dbOne'] = ModelOne.objects.all().order_by('-date') #I had a date field
        ctx['dbTwo'] = ModelTwo.objects.all().order_by('-date')
        #ctx['model3'] = ModelThree.objects.all()
return ctx
