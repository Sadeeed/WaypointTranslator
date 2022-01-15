from django.urls import path

from . import views

urlpatterns = [
    path('', views.VoxelMapToXaeroConverterView.as_view(), name='voxel_to_xaero'),
    path('download/', views.DownloadFileView.as_view(), name='download'),
]
