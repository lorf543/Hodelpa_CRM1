from django import forms
from django.forms import ModelForm,MultiWidget,DateTimeField,SplitDateTimeWidget
from django.contrib.admin.widgets import AdminSplitDateTime,AdminDateWidget,AdminTimeWidget
from django.contrib.admin import widgets
from .models import Rooms,Gym

class DateInpunt(forms.DateInput):
    input_type = 'date'

class GymForm(ModelForm):

    class Meta:
        model = Gym

        fields = "__all__"

        labels = {
            'timestart':" Hora de Entrada",
            'timeend':" Hora de Salida",

        }

        widgets = {
            'habitacion':forms.TextInput(attrs={ 'class':"form-control","placeholder":"Indroducir el numeor de la habitacion qui ",'readonly' : False }),
            'nombre':forms.TextInput(attrs={ 'class':"form-control","placeholder":"Indroducir el nombre de la persona ",'readonly' : False }),
            
            'timestart':forms.TimeInput(attrs={'class':"form-control","placeholder":"Introducir hora 00:00 AM/PM "}),
            'timeend':forms.TimeInput(attrs={'class':"form-control","placeholder":"Introducir hora 00:00 AM/PM "}),
            'date':DateInpunt(),
        }


class RoomsForm(ModelForm):
    
    class Meta:
        model = Rooms
        fields = ("numero","estado","category","distinciones","piso",)

        widgets = {
            'numero':forms.TextInput(attrs={ 'class':"form-control","placeholder":" ",'readonly' : True }),
            'category':forms.TextInput(attrs={ 'class':"form-control","placeholder":" ",'readonly' : True }),
            'distinciones':forms.TextInput(attrs={ 'class':"form-control","placeholder":" ",'readonly' : True }),
            'piso':forms.TextInput(attrs={ 'class':"form-control","placeholder":" ",'readonly' : True }),
            'estado':forms.Select(attrs={ 'class':"form-control","placeholder":" ",}),
        }


class RoomForm(ModelForm):
    class Meta:
        model = Rooms
        fields = ("numero","estado","category","distinciones","piso",)

        widgets = {
            'numero':forms.TextInput(attrs={ 'class':"form-control","placeholder":" ",}),
            'category':forms.Select(attrs={ 'class':"form-control","placeholder":" ",}),
            'distinciones':forms.Select(attrs={ 'class':"form-control","placeholder":" ", }),
            'piso':forms.Select(attrs={ 'class':"form-control","placeholder":" ",}),
            'estado':forms.Select(attrs={ 'class':"form-control","placeholder":" ",}),
        }

