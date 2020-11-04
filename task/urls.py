from django.urls import path
from .views import *
urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create'),
    path('param/', get_parameter, name='param'),
    path('lists/', PosListView.as_view(), name='lists')
]