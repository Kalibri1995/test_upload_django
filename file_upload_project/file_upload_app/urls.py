from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload-file'),
    path('files/', views.file_list, name='file-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
