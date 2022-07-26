from django.urls import path
from . views import ProductView,ProductCreate,ProductDetail,RegistrationView
urlpatterns = [
    path('',ProductView.as_view(),name='home'),
    path('create/',ProductCreate.as_view(),name='create'),
    path('detail/<int:pk>',ProductDetail.as_view(),name='delete'),
    path('registration',RegistrationView.as_view(),name='register')
]
