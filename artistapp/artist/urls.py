from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('content',ContentView)
urlpatterns = [
    path('',include(router.urls)),
    path('register/',ProfileRegisterView.as_view(),name='register')

]

