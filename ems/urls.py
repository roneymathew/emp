"""ems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from api import views
from rest_framework_jwt.views import refresh_jwt_token



router = routers.DefaultRouter(trailing_slash=True)
router.register('api/users', views.UserViewSet)
router.register('api/empapi', views.EmpViewSet)
router.register('tree',views.TreeViewSet)


urlpatterns = [
    url('', include(router.urls)),
    url(r'^', include('rest_auth.urls')),
    url(r'^registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('employee/',include('employee.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^refresh-token/', refresh_jwt_token),

]
