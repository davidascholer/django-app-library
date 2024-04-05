from django.contrib import admin
from django.urls import path, include
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('auth/', include('core.urls')),
    path('profiles/', include('userprofile.urls')),
    path('users/', include('core.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
