from django.shortcuts import render
from .models import Customer, Movie
from .serializers import CustomerSerializer, MovieSerializer

from rest_framework import viewsets, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]  

@api_view(['POST'])  
@permission_classes([])  # Allow access to everyone (no authentication needed)
def login_view(request):
    serializer = TokenObtainPairSerializer(data=request.data)

    if serializer.is_valid():
        token = serializer.validated_data
        return Response(token, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  