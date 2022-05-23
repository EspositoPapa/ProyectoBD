from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.ingreso),
    path("BDfamiliares", views.BDfamiliares),
    path("IngresoFam", views.IngresoFam)
]

