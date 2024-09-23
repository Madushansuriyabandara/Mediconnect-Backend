from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mediconnect_app.urls')),
    path('users/', include('mediconnect_app.urls')),
    path('users/create/', include('mediconnect_app.urls')),
    path('users/<str:pk>/', include('mediconnect_app.urls')),
    path('users/<str:pk>/update/', include('mediconnect_app.urls')),
    path('users/<str:pk>/delete/', include('mediconnect_app.urls')),

    path('patients/', include('mediconnect_app.urls')),
    path('patients/create/', include('mediconnect_app.urls')),
    path('patients/<str:pk>/', include('mediconnect_app.urls')),
    path('patients/<str:pk>/update/', include('mediconnect_app.urls')),
    path('patients/<str:pk>/delete/', include('mediconnect_app.urls')),
]
