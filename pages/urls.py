from django.urls import path

from pages import views

app_name = 'pages'

urlpatterns = [
    path('', views.PageView.as_view(), name='pages'),
    path('404/', views.ErrorView.as_view(), name='404'),
    path('aboutus/', views.AboutUs.as_view(), name='aboutus'),
    path('contactus/', views.ContactUs.as_view(), name='contactus'),
    path('account/', views.AccountPage.as_view(), name='accountpage'),
    path('login/',views.LoginPage.as_view(), name='login'),
    path('register/',views.RegisterView.as_view(), name='register'),
    path('wishlist/', views.WishlistPage.as_view(), name='wishlist'),
]
