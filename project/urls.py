"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from newspaper import views
from newspaper.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('newspaper.urls')),
    path('news/search/', PostsSearch.as_view(), name='search'),
    path('news/add/', PostsAdd.as_view(), name='add'),
    path('news/<int:pk>/edit/', PostEdit.as_view(), name='edit'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='delete'),
    # path('', views.home, name='home'),
    path('', include('protect.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
    path('category/<int:pk>', PostCategoryView.as_view(), name='category')
]
