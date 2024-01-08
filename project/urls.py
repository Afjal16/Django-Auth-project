from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('app1.urls')),
    path('', include('auth1.urls')),
    
    
]
