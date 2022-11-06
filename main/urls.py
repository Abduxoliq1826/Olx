from django.urls import path
from .views import *

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("login/", Login, name="login"),
    path('is_admin/', ProductFilter, name='productfilter'),
    path('about/<int:pk>/', About, name='about'),
    path('logins/', Logins, name='logins'),
    path('log-out/', LogOut, name='logout'),
    path('user/', All_User, name='users'),

    path('ads/', AllAds, name='ads'),
    path('isacepted/', IsAcepted, name='isacepted'),
    path('isrejected/', IsRejected, name='isrejected'),
    path('sort/', Sold, name='sold'),

    path('info/', InformationViews, name='info'),
    path('infos/', InformationsViews, name='infos'),
    path('delete-info/<int:pk>/', DeleteInfo, name='delete_info'),

    path('users/<int:pk>/', Users, name='users'),

    path('ads/<int:pk>/', AdsSingle, name='single-ads'),
    path('accepted/<int:pk>/', Accepted, name='accept'),
    path('rejected/<int:pk>/', Rejected, name='reject'),
    path('reset/', Reset, name='reset'),
    path('reset-user/', UpdateUser, name='reset_user'),

    path('helps_q/', Help_q_Create, name='helps_q'),
    path('update_hq/<int:pk>/', Update_hq, name='update_hq'),
    path('delete_hq/<int:pk>/', Delete_hq, name='delete_hq'),

    path('helps_a/', Help_a_Create, name='helps_a'),
    path('update_ha/<int:pk>/', Update_ha, name='update_ha'),
    path('delete_ha/<int:pk>/', Delete_ha, name='delete_ha'),


    path('category/', AddCategory, name='category'),
    path('single-category/<int:pk>/', SingleCategory, name='single_category'),
    path('delete-category/<int:pk>/', DeleteCategory, name='delete_category'),

    path('distirc/', DistircView, name='distirc'),
    path('distirc-create/', District_create, name='distirc-create'),
    path('single-distirc/<int:pk>/', District_update, name='update_distirc'),
    path('delete-distirc/<int:pk>/', District_delete, name='delete_distirc'),
    path('all-distirc/<int:pk>/', Distirc_all, name='distirc_all'),

    path('subcategory/', SubCategory, name='subcategory'),
    path('single-subcategory/<int:pk>/', SingleSubCategory, name='single_subcategory'),
    path('delete-sub-category/<int:pk>/', DeleteSubCategory, name='delete_supcategory'),

    path('regions/', Regions, name='regions'),
    path('single-region/<int:pk>/', SingleRegion, name='single_region'),
    path('delete-region/<int:pk>/', DeleteRegion, name='delete_region'),
]