from rest_framework import authentication, permissions
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import *
from rest_framework.views import APIView
from rest_framework import generics, status
from django.contrib.auth import login, logout, authenticate
from main.models import *
from rest_framework.pagination import PageNumberPagination
@api_view(['GET'])
def UserProfile(request):
    user = request.user
    if user.type == 1:
        context = {
            'user': UserSerializer(user).data
        }
        return Response(context)

    context = {
        'message': 'siz user emassiz'
    }
    return Response(context)

# ishladi
class StandartPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_siz'
    max_page_size = 1000

class Adspage(generics.ListAPIView):
    queryset = Ads.objects.all()
    pagination_class = StandartPagination
    serializer_class = AdsSerializer
@api_view(['GET'])
def UserAds(request):
    user = request.user
    print(user)
    ads = Ads.objects.filter(owner_id=user.id)
    context = {
        'user': UserSerializer(user).data,
        'ads': AdsSerializer(ads, many=True).data,
    }
    return Response(context)




@api_view(['POST'])
def UserAddAds(request):
    username = request.POST.get('username')
    users = User.objects.get(username=username)
    region = request.POST.get('region')
    category = request.POST.get('category')
    photo = request.POST.getlist('photo')
    name = request.POST.get('name')
    price = request.POST.get('price')
    description = request.POST.get('description')
    ads = Ads.objects.create(owner=users, price=price, region_id=region, category_id=category, name=name, description=description)
    for i in photo:
        ads.photo.add(i)

    context = {
        'ads': AdsSerializer(ads).data,
    }
    return Response(context)


@api_view(['POST'])
def AddSold(request,pk):
    ads = Ads.objects.get(id=pk)
    ads.status = 4
    ads.save()
    return Response('ok')

@api_view(['POST'])
def Register(request):
    name = request.POST['name']
    password = request.POST.get('password')
    if name.startswith('+998'):
        phones = name[1:13]
        if phones.isnumeric():
            if len(phones) == 12:
                User.objects.create_user(username=phones, phone=name, password=password)
                return Response('Siz registratsiyadan o`ttingiz')
            else:
                return Response('zxfsdvk')
        else:
            return Response('yoq')
    else:
        return Response('zor')




@api_view(['POST'])
def Login_user(request):
    phone = request.POST['phone']
    password = request.POST['password']
    users = User.objects.filter(username=phone)
    if users is not None:
        usr = authenticate(username=phone, password=password)
        if usr is not None:
            login(request, usr)
            return Response('ok')
        return Response('no')
    return Response('salom')