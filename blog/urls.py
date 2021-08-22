from django.urls import path
from .views import BlogTop, signupview, loginview, logoutview, BlogList, BlogArticle

app_name = 'blog'

urlpatterns = [
    path('', BlogTop.as_view(), name='top'),
    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),
    path('list/', BlogList.as_view(), name='list'),
    path('article/<int:pk>/', BlogArticle.as_view(), name='article')

]