"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from professional import views

router = routers.DefaultRouter()
router.register(r'organization', views.OrganizationView, 'Organization')

urlpatterns = [
    # Home Template
    url(r'^$', views.home, name='home'),
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
    
    # Your URLs
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshSlidingView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    
    path('api/professional/', views.ProfessionalView.as_view(), name='professional'),
    path('api/patient/', views.PatientView.as_view(), name='patient'),
    path('api/patient/<int:pk>/', views.PatientView.as_view(), name='Patient Edit'),
    
    path('api/album/', views.AlbumView.as_view(), name='Album'),
    path('api/album/<int:pk>/', views.AlbumView.as_view(), name='Album Edit'),
    
    path('api/scan/', views.ScanView.as_view(), name='Scan'),
    path('api/scan/<int:pk>/', views.ScanView.as_view(), name='Scan Edit'),
]


admin.site.site_header = "Foot Scanning"
admin.site.index_title = "Foot Scanning administration"
admin.site.site_title = "Foot Scanning"