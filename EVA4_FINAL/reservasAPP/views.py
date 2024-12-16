from django.shortcuts import render

#IMPORTACIONES PARA API REST CON CLASES
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Reserva
from .serializers import ReservaSerializer
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import ReservaRegistroForms


#VISTA INDEX
def index(request):
    return render(request, 'reservasAPP/index.html')


#VISTA PARA EL LISTADO DE LAS RESERVAS (CRUD)
def reservasData(request):
    reservas = Reserva.objects.all()
    data = {'reservas': reservas}
    return render(request, 'reservasAPP/reservas.html', data)

#VISTA PARA AGREGAR UNA RESERVA DESDE EL LISTADO
def reservaRegistro(request):
    form = ReservaRegistroForms()

    if request.method == 'POST':
        form = ReservaRegistroForms(request.POST)
        if form.is_valid():
            reserva = form.save()
            return HttpResponseRedirect(reverse('reservasData'))
    data = {'form': form,
            'titulo':'Agregar Reserva'
            } #Paso el formulario a la plantilla
    return render(request, 'reservasAPP/añadir_reserva.html', data)

#VISTA PARA EDITAR UNA RESERVA DESDE EL LISTADO
def editarReserva(request, id):
    #Buscar la reserva dentro de la base de datos con el id
    reserva = Reserva.objects.get(id=id)
    form = ReservaRegistroForms(instance=reserva)

    if request.method == 'POST':
        form = ReservaRegistroForms(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('reservasData'))
    data = {'form': form,
            'titulo': 'Editar Reserva'} #Paso el formulario a la plantilla
    return render(request, 'reservasAPP/añadir_reserva.html', data)

#VISTA PARA ELIMINAR UNA RESERVA DESDE EL LISTADO
def eliminarReservas(request, id):
    #Buscar el reserva dentro de la base de datos con el id
    reserva = Reserva.objects.get(id=id)
    reserva.delete()
    return HttpResponseRedirect(reverse('reservasData'))



#API REST RESERVAS CON CLASES
class ReservaListCreateView(APIView):
    def get(self, request):
        reservas = Reserva.objects.all().order_by('fecha_reserva','hora')
        serializer = ReservaSerializer(reservas, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ReservaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ReservaDetail(APIView):
    def get_object(self, pk):
        try:
            reserva = Reserva.objects.get(pk=pk)
        except Reserva.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        reserva = Reserva.objects.get(pk=pk)
        serializer = ReservaSerializer(reserva)
        return Response(serializer.data)
    
    def put(self, request, pk):
        reserva = Reserva.objects.get(pk=pk)
        serializer = ReservaSerializer(reserva, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        reserva = Reserva.objects.get(pk=pk)
        reserva.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
