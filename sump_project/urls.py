from django.contrib import admin
from django.urls import path
from monitoring.views import receive_sump_data
from monitoring.views import dashboard

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/sump/", receive_sump_data),
    path('dashboard/', dashboard, name='dashboard'),
]
