from django.urls import path

from products import views

app_name = 'products'


urlpatterns = [
    path('checkout/', views.CheckoutPage.as_view(), name='checkout'),
    path('cart/', views.CartView.as_view(), name='cart'),
]