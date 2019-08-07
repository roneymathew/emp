from django.contrib import admin
from django.urls import path
from .views import IndexPage,CreatePage,SearchPage,UpdatePage,SignUp

urlpatterns = [
	path('signup/', SignUp.as_view(), name='signup'),
    path('', IndexPage.as_view(),name='index'),
    path('create',CreatePage.as_view(),name='create'),
    path('search',SearchPage.as_view(),name='search'),
    path('update/<int:ab>/',UpdatePage.as_view(),name='update'),

]
