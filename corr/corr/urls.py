"""corr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('userReservationList/', views.userReservationList.as_view(), name="user_list"),
    path('latestReservation/', views.latestReservation.as_view(), name="latest_reservation"),
    path('create/', views.create),
    path('vacant/', views.vacant.as_view(), name="vacantRoom"),
    path('res/', views.res.as_view(), name="reservation_info"),
    path('res1/', views.res1.as_view(), name="continuation"),
    path('index/', views.index),
    path('rooms/', views.rooms),
    path('roomList/', views.roomList.as_view(), name="room_list"),
    path('dashboard/', views.dashboard),
    path('reservation/', views.reservation.as_view(), name="reservation_user"),
    path('upload/', views.image_upload_view)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


  


