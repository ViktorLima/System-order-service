from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,   name='home'),
    path('<int:customer_id>', views.view_customer,   name='view_customer'),
    path('delete/<int:customer_id>', views.delete_customer,   name='delete_customer'),
    path('seach/', views.seach,   name='seach'),
]

