from django.urls import path
from . import views

urlpatterns = [
    path('getIcras/', views.getIcras),
    path('getDavas/', views.getDavas),
    path('getNotes/', views.getNotes),
    path('getAppointments/',views.getAppointments),
    path('getOurServices/',views.getOurServices),
    path('getArticlesAndNews/',views.getArticleAndNews),
    path('getLawyers/',views.getLawyers),
    path('getReferences/',views.getReferences),
]