from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),
    
    # Swagger view
    path('api/v1/', include('api_swagger.urls')),
    
    # API endpoints
    path('api/v1/movies/', include('movies.urls')),
    path('api/v1/auth/', include('authentication.urls')),
]
