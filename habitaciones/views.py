from django.shortcuts import render,redirect,Http404,get_object_or_404
from .models import *
from .forms import *

from django.contrib import messages
from django.db.models import Q

from django.views.generic import ListView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth import logout as dj_logout

from django.contrib.auth.decorators import login_required
from .decorators import *



from django.core.paginator import Paginator
# Create your views here.

#Login_____________

def inicio (request):
    context={}
    return render(request,'inicio.html',context)
@unauthenticated_user
def login(request):
	
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate (request, username=username, password=password)
			
		if user is not None:
			dj_login(request,user)
			return redirect('home')
		else:
			messages.info(request,'username or password is incorrent')

	context = {}
	return render (request, 'user/login.html',context)

@login_required(login_url='inicio')
def logout(request):
    dj_logout(request)

    return redirect('home')

#status rooms counting status__________________________________

@login_required(login_url='inicio')

def home (request):
    total_havitaciones = Rooms.objects.all()

    limpias = total_havitaciones.filter(estado='Libre').count()
    ocupadas = total_havitaciones.filter(estado='Ocupado').count()
    sucias = total_havitaciones.filter(estado='Sucia').count()
    
    page = request.GET.get('page',1)
    try:
        paginator = Paginator(total_havitaciones,5)
        total_havitaciones = paginator.page(page)
    except:
        raise Http404

    context = {
        "entity":total_havitaciones,
        "limpias":limpias,
        "ocupadas":ocupadas,
        "sucias":sucias,
        "paginator":paginator,
    }
    return render(request,'habitaciones/home.html',context)

@login_required(login_url='inicio')
def updatestatus(request,pk):

    estatus = Rooms.objects.get(id=pk)
    form = RoomsForm(instance=estatus)

    if request.method == 'POST':
        form = RoomsForm(request.POST,instance=estatus)
        if form.is_valid():
            form.save()
            messages.success(request,'Modifcado Correctamente')
            return redirect ("/")

    context = {"form":form,
    "estatus":estatus}
    return render(request,'habitaciones/updatestatus.html',context)

@login_required(login_url='inicio')
def listadoocupado(request):
    total_havitaciones = Rooms.objects.all()
    

    context = {
    "total_havitaciones":total_havitaciones,
    }
    return render(request,'habitaciones/listado_ocupado.html',context)

@login_required(login_url='inicio')
def listadolimpio(request):
    total_havitaciones = Rooms.objects.all()
    

    context = {
    "total_havitaciones":total_havitaciones,
    }
    return render(request,'habitaciones/listado_limpias.html',context)

@login_required(login_url='inicio')
def listadosucio(request):
    total_havitaciones = Rooms.objects.all()
    

    context = {
    "total_havitaciones":total_havitaciones,
    }
    return render(request,'habitaciones/listado_sucias.html',context)

#Habitaciones CRUD__________________________________
@login_required(login_url='inicio')
@allowed_users(allowed_roles=['admin','recepcion'])
def RoomsCreate(request):
    form = RoomForm

    if request.method == 'POST':
        form = GymForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("gym")


    context={"form":form}
    return render (request,'habitaciones/create-rooms.html',context)

@login_required(login_url='inicio')
@allowed_users(allowed_roles=['admin','recepcion'])
def roomsdelete(request,pk):
    room = get_object_or_404(Rooms,id=pk)
    room.delete()
    messages.success(request,'Borrado Correctamente')
    return redirect(to='home')


#Gym CRUD____________________________________________

@login_required(login_url='inicio')
@allowed_users(allowed_roles=['admin','recepcion'])
def gym (request):

  
    todo = Gym.objects.all()
    context = {"todo":todo,
    }     
    
    return render (request,'gym/gym.html',context)

@login_required(login_url='inicio')
@allowed_users(allowed_roles=['admin','recepcion'])
def gymcreate (request):

    form = GymForm

    if request.method == 'POST':
        form = GymForm(request.POST)
        if form.is_valid():
            messages.success(request,"Agendado Correctamente")
            form.save()
            return redirect("gym")


    context={"form":form}
    return render (request,'gym/create.html',context)

@login_required(login_url='inicio')
@allowed_users(allowed_roles=['admin','recepcion'])
def gymdelete (request,pk):

    gym = get_object_or_404(Gym, id=pk)
    gym.delete()
    messages.success(request,'Borrado Correctamente')
    return redirect(to='gym')
    # gym=Gym.objects.get(id=pk)

    # if request.method == 'POST':
    #         gym.delete()
    #         messages.success(request,'Eliminado Correctamente')
    #         return redirect('gym')
 
    # context={}
    # return render (request,'gym/delete.html',context)



#Searh ____________________

def datasearch(request):
    
    if request.method == 'POST':
        searched = request.POST['searched']
        loopkup = (Q (estado__icontains=searched) | Q(category__icontains=searched) )
        rooms = Rooms.objects.filter(loopkup)
        return render (request,'habitaciones/busqueda.html',{'searched':searched,'rooms':rooms,})
    else:
        return render (request,'habitaciones/busqueda.html')