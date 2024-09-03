from django.urls import path
from .views import new, index, edit, delete, show, download
from .api.views import SourceFilesListView

urlpatterns = [
    path('new/', new, name='files_new'),
    path('', index, name='files_index'),
    path('edit/<int:id>/', edit, name='files_edit'),
    path('delete/<int:id>/', delete, name='files_delete'),
    path('show/<int:id>', show, name='files_show'),
    path('download/<int:id>', download, name='files_download'),
    path('api/sourcefiles/', SourceFilesListView.as_view(), name='sourcefiles_api'),
]