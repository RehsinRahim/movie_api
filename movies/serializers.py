from rest_framework import serializers
from .models import Customer, Movie

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__' 

class MovieSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    class Meta:
        model = Movie
        fields = '__all__'