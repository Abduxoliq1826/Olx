from rest_framework import serializers
from main.models import *


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = "__all__"
    
class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distirc
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class AdImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdImage
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = "__all__"


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = "__all__"


class Helps_qSerializer(serializers.ModelSerializer):
    class Meta:
        model = Helps_q
        fields = "__all__"


class Helps_aSerializer(serializers.ModelSerializer):
    class Meta:
        model = Helps_a
        fields = "__all__"


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"