"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from coin.apis.apis import CoinView
from coin.views import home_page as home
from river.apis.apis import RiverView

urlpatterns = [
    path('', home, ),
    path('admin/', admin.site.urls),
    path('coin/<str:coin>/', home),
    path('api/coin/<str:coin>/', CoinView.as_view()),
    path('api/river/', RiverView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
