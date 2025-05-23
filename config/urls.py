"""config URL Configuration

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
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (TokenObtainPairView,
    TokenRefreshView, TokenVerifyView)
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.documentation import include_docs_urls

from apps.grocers_panel.views import (
    ShopViewSet,
    RatingViewSet,
    OfferViewSet,
    GrocerViewSet,
MealViewSet,
)

from apps.admin_panel.views import (
    CategoryViewSet,
    UserViewSet,
    AuthAPIView,
    RegisterAPIView,
    UserDetailAPIView,
)

from apps.buyers_panel.views import (
    BillingAddressViewSet,
    OrderViewSet,
    geocode,
    get_zone,
)

from apps.food_panel.views import (
    FoodViewSet,
    PopularFoodViewSet,
    RecommendedFoodViewSet,
    DrinksViewSet,
)

router = routers.DefaultRouter()
router.register(r'ratings', RatingViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'offers', OfferViewSet)
router.register(r'shops', ShopViewSet)
router.register(r'users', UserViewSet)
router.register(r'grocers', GrocerViewSet)
router.register(r'meals', MealViewSet)

router2 = routers.DefaultRouter()
router2.register(r'products(/?P<category>[a-zA-Z]+)', FoodViewSet)
router2.register(r'addresses', BillingAddressViewSet)
router2.register(r'orders', OrderViewSet)

urlpatterns = [
    path('docs/', include_docs_urls(title='Grocery API')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
    path('api-token-auth/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
    path('api-token-verify/', TokenVerifyView.as_view()),

    path('api/v1/', include(router.urls)),
    path('api/v1/', include(router2.urls)),

    path(r'', TemplateView.as_view(template_name='index.html'), name='index'),
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
    path('api/v1/signin/', AuthAPIView.as_view(), name='login'),
    path('api/v1/signup/', RegisterAPIView.as_view(), name='register'),
    path('api/v1/customer-info/', UserDetailAPIView.as_view(), name='user_detail'),
    path('api/v1/geocode/', geocode, name='geocode'),
    path('api/v1/zone/', get_zone, name='zone'),
])

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
