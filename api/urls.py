from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('users/', views.UserList.as_view()),
    path('users//', views.UserDetail.as_view()),
    path('cabinets/', views.CabinetList.as_view()),
    path('queues/', views.QueueList.as_view()),
    path('queues//', views.QueueDetail.as_view()),
    #path('equeue/', views.equeueapp),
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)