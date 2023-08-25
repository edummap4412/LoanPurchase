from django.contrib import admin
from django.urls import path
from rest_framework import routers

from djangoapp.views import RegisterClientViewSet

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register-cli/', RegisterClientViewSet.as_view(), name='register-client'),

]
