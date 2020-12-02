from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('content',ContentView,)
router.register('register',ProfileRegisterView)

urlpatterns = [
    path('',include(router.urls)),
    path('register/',include(router.urls),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),


]

