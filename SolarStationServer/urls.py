"""
URL configuration for SolarStationServer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views
from django.contrib import admin
from accounts.views import login_redirect, base_page, api_login, api_register, api_logout
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, re_path, include
from rest_framework.permissions import AllowAny
from graphene_django.views import GraphQLView
from .views import hello_world
from telegram.views import telegram


schema_view = get_schema_view(
    openapi.Info(
        title="Solar Station Server API",
        default_version='v1',
        description="Документація API для проекту Solar Station Server",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=([AllowAny]),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/data_collector', views.data_collector, name='data_collector'),
    path('api/get_current_data', views.get_current_data, name='get_current_data'),
    path('', login_redirect, name='login_redirect'),
    path('base/', base_page, name='base_page'),
    path('api/login/', api_login, name='api_login'),
    path('api/register/', api_register, name='api_register'),
    path('api/logout/', api_logout, name='api_logout'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('graphql/', GraphQLView.as_view(graphiql=True), name='graphql'),
    path('hello-world/', hello_world),
    path('telegram', telegram, name='telegram'),
]
