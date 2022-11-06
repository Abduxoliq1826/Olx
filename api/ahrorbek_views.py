from django.shortcuts import redirect
from main.models import *
from rest_framework import authentication, permissions
from django.contrib.auth import login, logout, authenticate
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from ipware import get_client_ip

@api_view(['GET'])
def Search(request):
    name = request.GET.get('name')
    if name is not None:
        a = Ads.objects.filter(name=name)

    price = request.GET.get('price')
    if price is not None:
        a = Ads.objects.filter(price=price)

    kop = request.GET.get('kop')
    kam = request.GET.get('kam')
    if kop is not None and kam is not None:
        kop = request.GET.get('kop')
        kam = request.GET.get('kam')
        a = Ads.objects.filter(price__gte=kam, price__lte=kop)



    # region = request.GET.get('region')
    # if region is not None:
    #     a = Ads.objects.filter(region__icontains=region)

    context = {
        'ads' : AdsSerializer(a, many=True).data,
    }
    return Response(context)


@api_view(['GET'])
def Ads_Get(request):
    a = Ads.objects.all()
    data = {
        'a' : AdsSerializer(a, many=True).data
    }
    return Response(data)



@api_view(['GET'])
def Filter_category_sup(request):
    q = request.GET.get('q')
    a = Subcategory.objects.filter(category_id=q)
    serializer = SubCategorySerializer(a, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def Filter_supcategory_ads(request):
    q = request.GET.get('q')
    a = Ads.objects.filter(category_id=q)
    serializer = AdsSerializer(a, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def ResetPassword(request):
    username = request.POST.get('username')
    last_password = request.POST.get('last_password')
    new_password = request.POST.get('new_password')
    new_password2 = request.POST.get('new_password2')
    user = User.objects.get(username=username)
    usr = authenticate(username=user, password=last_password)
    if new_password == new_password2:
        if usr is not None:
            usr.username = username
            usr.set_password(new_password2)
            usr.save()
            return Response('done')
        return Response('bunday user yoq')
    return Response('Yangi parollar bir-biriga togri kemayapti!')



@api_view(['POST'])
def wishlistadd(request):
     ads_id = request.POST['ads_id']
     print(ads_id)
     client_ip, is_routable = get_client_ip(request)
     if client_ip is None:
         return Response({"Unable to get the client's IP address"})
     else:
        Wishlist.objects.create(ip=client_ip, ads_id=ads_id)
        return Response({"added"})
