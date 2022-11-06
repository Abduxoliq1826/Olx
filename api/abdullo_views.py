from rest_framework import authentication, permissions
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import *
from rest_framework.views import APIView
from rest_framework import generics, status
from django.contrib.auth import login, logout, authenticate
from main.models import *

@api_view(['GET'])
def Categorys(request, pk):
    category = Category.objects.get(id=pk)
    category_list = []
    ads = Ads.objects.all()
    for i in ads:
        if i.category.category.name == category.name:
            category_list.append(i)
        else:
            pass
    data = {
        'catyegory_ads': AdsSerializer(category_list, many=True).data
    }
    return Response(data)


@api_view(['GET'])
def UserAds(request,pk):
    user = User.objects.get(id=pk)
    ads = Ads.objects.all()
    adss = []
    for i in ads:
        if i.owner.username == user.username:
            adss.append(i)
        else:
            pass
    data = {
        'ads': AdsSerializer(adss, many=True).data
    }
    return Response(data)

@api_view(['GET'])
def Index(request):
    is_top = []
    is_recommended = []
    for i in Ads.objects.all():
        if i.is_top == True:
            is_top.append(i)
    for i in Ads.objects.all():
        if i.is_recommended == True:
            is_recommended.append(i)

    data = {
        'is_top': AdsSerializer(is_top, many=True).data,
        'is_recommended': AdsSerializer(is_recommended, many=True).data,
        'information': InformationSerializer(Information.objects.last()).data
    }
    return Response(data)










