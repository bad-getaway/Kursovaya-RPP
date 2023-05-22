from rest_framework import serializers
from . import models



class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'


class GameSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Games
        fields = '__all__'