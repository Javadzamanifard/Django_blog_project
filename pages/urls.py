from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('aboutus/', views.AboutUsPage.as_view(), name = 'aboutus'),
]
