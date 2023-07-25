from portfolio import views
from django.urls import path,include

urlpatterns = [
    
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('resume',views.resume, name='resume'),
    path('blog',views.blog, name='blog'),
    path('portfolio',views.portfolio, name='portfolio'),
    path('services',views.services, name='services'),
    

]