from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from reviews.models import ModelOne,ModelTwo
from reviews import views

class model_one(DetailView):
    model = ModelOne
    template_name = 'reviews/model_one.html’

class model_two(DetailView):
    model = ModelTwo
    template_name = 'reviews/model_two.html’

urlpatterns = [
    url(r'^$', views.review_page.as_view(), name='review_page'),
    url(r'^stuff_in_modelone/(?P\d+)$', model_one.as_view(), name = 'model1'),
    url(r'^stuff_in_modeltwo/(?P\d+)$', model_two.as_view(), name = 'model2'),
        ]
