from django.urls import path,include
from pro_app.views import *

urlpatterns = [
    path('',homepage,name='index'),
    path('about-us/',about_us,name='about-us'),
    path('our-menu/',our_menu,name='our-menu'),
    path('our-services/',our_services,name='our-services'),
    path('allergy-advice/',allergy_advice,name='allergy-advice'),
    path('contact-us/',contact_us,name='contact-us'),
    path('get-in-touch/',get_in_touch,name='get-in-touch'),

]