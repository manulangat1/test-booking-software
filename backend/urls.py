from django.urls import path,include
from . import views
from knox import views as knox_views

urlpatterns = [
    path('register/',views.RegisterAPI.as_view()),
    path('login/',views.LoginAPI.as_view()),
    path('user/',views.UserAPI.as_view()),
    path('test/',views.TestApi.as_view()),
    path('tests/<pk>/',views.TestDetailsApi.as_view()),
    path('logout/',knox_views.LogoutView.as_view())
]