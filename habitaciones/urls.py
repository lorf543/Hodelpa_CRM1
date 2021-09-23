from django.urls import path
from . import views

urlpatterns = [

    path('landing',views.inicio,name='inicio'),

    path('',views.home,name='home'),
    path('updateestatus/<str:pk>',views.updatestatus,name='update'),
    path('ocupadas/',views.listadoocupado,name='ocupadas'),
    path('limpias/',views.listadolimpio,name='limpias'),
    path('sucias/',views.listadosucio,name='sucias'),

    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),

    path('gym/',views.gym,name='gym'),
    path('gym-create/',views.gymcreate,name='gym-create'),
    path('gym-create/<str:pk>',views.gymdelete,name='gym-delete'),

    path('rooms-create',views.RoomsCreate,name='rooms-create'),

    path ('buscar',views.datasearch,name='buscar')
]
