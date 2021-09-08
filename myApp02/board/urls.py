from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

app_name = 'board'

urlpatterns = [
    path('', views.index, name="index"),
    path('list/', views.list, name="list"),
    path('list/<int:pk>', views.view, name="view"),
    path('write/', views.write, name="write"),
    path('list/<int:pk>/delete', views.delete, name="delete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)