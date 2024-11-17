from django.contrib import admin
from django.urls import path, include
from .views import checker
from . import views
from .views import get_coordinates
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('',views.index, name ='index' ),
    path('get_coordinates/', views.get_coordinates, name='get_coordinates'),
    # path('quiz/', include('quiz.urls'), name='quiz'),
    # path('user_profile/', views.user_profile, name='user_profile'),
    # path('admin/', admin.site.urls,),
    path('checker/', checker, name = 'checker'),
    path('', get_coordinates, name ='cords'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('', TemplateView.as_view(template_name='index.html'), name = 'home'),
    # path('user_list/', views.user_list, name = 'user_list'),
    # path('signup/', views.signup_view, name='signup'),
    # path('login/', views.login_view, name='login'),
    # path('login/index/', views.index, name='login2'),
    # path('login/admin/', admin.site.urls, name='redirecting_admin'),
    # path('login/login_index.html', views.index),
    # path('accounts/login/index.html', views.index)
    # path('login/signup/admin', admin.site.urls, name='redirecting_admin'),
    # path('logout/', views.logout_view, name='logout'),
    # path('user_list/', views.user_list, name='user_list'),
]