from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, login_view, MovieViewSet

router = DefaultRouter()
router.register('customers', CustomerViewSet, basename='customer')
router.register('movies', MovieViewSet, basename='movie')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view, name='login'),
]