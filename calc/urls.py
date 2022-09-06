
from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home' ),
    path('getsome',views.get_only, name='get_only' ),
    path('postsome',views.post_only, name='post_only' ),
]
