from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('client', views.ClientViewSet)
router.register('contact', views.ContactViewSet)
urlpatterns = [
    path('', include(router.urls))
]