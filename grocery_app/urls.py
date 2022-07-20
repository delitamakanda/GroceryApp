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
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns

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

from buyers_panel.api.views import (
    BillingAddressViewSet,
    OrderViewSet,
)

from grocery_api.api.views import (
    FoodViewSet,
    PopularFoodViewSet,
    RecommendedFoodViewSet,
    DrinksViewSet,
)

router = routers.DefaultRouter()
router.register(r'billing-addresses', BillingAddressViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'highlights', HighlightsViewSet)
router.register(r'offers', OfferViewSet)
router.register(r'shops', ShopViewSet)
router.register(r'users', UserViewSet)

router2 = routers.DefaultRouter()
router2.register(r'products(/?P<category>[a-zA-Z]+)', FoodViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),

    path('api/', include(router.urls)),
    path('api/v1/', include(router2.urls)),
]

search_product_list = FoodViewSet.as_view({
    'get': 'list',
})
popular_product_list = PopularFoodViewSet.as_view({
    'get': 'list',
})
recommended_product_list = RecommendedFoodViewSet.as_view({
    'get': 'list',
})
drinks_list = DrinksViewSet.as_view({
    'get': 'list',
})

urlpatterns += format_suffix_patterns([
    path('api/v1/products/popular/', popular_product_list, name='popular_products'),
    path('api/v1/products/recommended/', recommended_product_list, name='recommended_products'),
    path('api/v1/products/drinks/', drinks_list, name='drinks'),
    path('api/v1/products/', search_product_list, name='search_product'),
])

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
