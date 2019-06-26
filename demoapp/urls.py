from django.urls import path
from demoapp import views

urlpatterns =  [
    path('save/', views.save_data, name='save'),
    path('show/', views.retrieve, name='show'),
    path('update/<int:id>/', views.data_update, name='update'),
    path('delete/<int:id>/', views.data_delete, name='delete'),
]