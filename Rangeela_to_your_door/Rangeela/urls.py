from django.urls import path
from Rangeela import views
app_name = 'Rangeela'

urlpatterns =[
    path('',views.index, name='index')
]