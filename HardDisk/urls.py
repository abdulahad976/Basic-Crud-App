from django.urls import path
from .views import Display, AddDisk, UpdateDisk, DeleteDisk

urlpatterns = [
    path('', Display, name='display'),
    path('adddisk/', AddDisk, name='adddisk'),
    path('updatedisk/<int:disk_id>/', UpdateDisk, name='updatedisk'),
    path('deletedisk/<int:disk_id>/', DeleteDisk, name='deletedisk'),
]
