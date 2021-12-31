"""grocery_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework import routers

from delivery_panel.api.views import (
    UserViewSet
)

from grocers_panel.api.views import (
    ShopViewSet,
    RatingViewSet,
    OfferViewSet,
)

from admin_panel.api.views import (
    CategoryViewSet,
    HighlightsViewSet,
)

router = routers.DefaultRouter()
router.register(r'ratings', RatingViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'highlights', HighlightsViewSet)
router.register(r'offers', OfferViewSet)
router.register(r'shops', ShopViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("stripe/", include("djstripe.urls", namespace='djstripe')),

    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),

    path('api/', include(router.urls)),

]
