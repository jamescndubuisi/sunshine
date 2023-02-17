"""sunshine URL Configuration

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

from django.urls import path
from .views import (home, GPListAPIView, GPListUnseenAPIView, GPListSeenAPIView,
                    DiscountListAPIView, DiscountListUnseenAPIView, DiscountListSeenAPIView,
                    BillListAPIView, BillListUnseenAPIView, BillListSeenAPIView)
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', home),
    path('list-gp', GPListAPIView.as_view()),
    path('list-gp-seen', GPListSeenAPIView.as_view()),
    path('list-gp-unseen', GPListUnseenAPIView.as_view()),
    path('list-discount', DiscountListAPIView.as_view()),
    path('list-discount-seen', DiscountListSeenAPIView.as_view()),
    path('list-discount-unseen', DiscountListUnseenAPIView.as_view()),
    path('list-bill', BillListAPIView.as_view()),
    path('list-bill-seen', BillListSeenAPIView.as_view()),
    path('list-bill-unseen', BillListUnseenAPIView.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)
