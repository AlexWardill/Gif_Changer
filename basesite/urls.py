from django.urls import path, reverse
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
  path('', views.home, name='basesite'),
  path('display-gif', views.display_gif, name='basesite-display-gif')
]