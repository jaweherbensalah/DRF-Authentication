
from django.contrib import admin
from django.urls import path
from accounts.views import ListUsers, CustomAuthToken
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.i18n import i18n_patterns
from rest_framework.routers import DefaultRouter
from translation.views import PostViewSet

router= DefaultRouter()
router.register('', PostViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="Auth API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@expenses.local"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('translation/', include(router.urls)),

    path('social_auth/', include(('social_auth.urls', 'social_auth'),
                                 namespace="social_auth")),
    path('accounts/', include(('accounts.urls', 'accounts'),
                                 namespace="accounts")),


    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),

    path('api/api.json/', schema_view.without_ui(cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
    path('api/users/', ListUsers.as_view()),
    path('api/token/auth/', CustomAuthToken.as_view()),

]

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    ]