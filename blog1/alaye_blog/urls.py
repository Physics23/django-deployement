from django.urls import path
from.import views

from django.urls import path

from . import views

urlpatterns = [
    path('<slug:slug>/', views.detail, name='Post_detail'),

]
