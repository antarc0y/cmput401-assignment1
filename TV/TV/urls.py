"""TV URL Configuration

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
from django.urls import path
from TV import views
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title='TV Docs',
        default_version='v1',
        description='This API tracks TV shows, it respondes to GET, POST, PUT, DELETE' 
   ),
    public = True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin', admin.site.urls),
    path('shows/', views.show_list),
    path('shows', views.show_list),
    path('shows/<int:id>', views.show_detail),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema_redoc'),
    path('docs', schema_view.with_ui('redoc', cache_timeout=0), name='schema_redoc'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema_swagger'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema_swagger'),
]


#urlpatterns = format_suffix_patterns(urlpatterns)
