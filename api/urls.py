from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .ahrorbek_views import *
from .abdullo_views import *

urlpatterns = [
    # Ahrorbek
    path('get-ads/', Ads_Get),
    path('filter_sub_cat/', Filter_category_sup),
    path('filter_ads_sub/', Filter_supcategory_ads),
    path('reset_password/', ResetPassword),
    path('search/', Search),
    

    # Abduxoliq
    path('user_profile/', UserProfile),
    path('add_ads/', UserAddAds),
    path('user_ads/', UserAds),
    path('add_sold/<int:pk>/', AddSold),
    path('register/', Register),
    path('pagination/', Adspage.as_view()),
    path('login/', Login_user),


    # Abdullo
    path('category/<int:pk>/', Categorys),
    path('index/', Index),
    path('wishlistadd/', wishlistadd),
    path('category/<int:pk>/', Categorys),



    ]

