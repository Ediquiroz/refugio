from django.shortcuts import render
from django.http import HttpResponse
from apps.mascota.models import Mascota
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.mascota.form import MascotaForm

# Create your views here.
def index(request):
    return HttpResponse("Index de mascota")

# def mascota_list(request):
#     mascota=Mascota.objects.all()
#     contexto={'mascotas': mascota}
#     return render(request, 'mascota/mascota_list.html', contexto)

class MascotaList(ListView):
    model=Mascota
    template_name='mascota/mascota_list.html'

# def mascota_view(request):
#     if  request.method=='POST':
#         form = MascotaForm(request.POST)
#         if form.is_valid():
#            form.save()
#         return redirect('mascota: index')
#     else:
#         form=MascotaForm()
#     return render(request, 'mascota/mascota_form.html', {'form':form})

class MascotaCreate(CreateView):
    model= Mascota
    form_class = MascotaForm
    template_name='mascota/mascota_form.html'
    success_url = reverse_lazy('mascota_listar')

# def mascota_edit(request, id_mascota):
#     mascota=Mascota.objects.get(id=id_mascota)
#     if request.method=='GET':
#         form=MascotaForm(instance=mascota)
#     else:
#         form=MascotaForm(request.POST, instance=mascota)
#         if form.is_valid():
#             form.save()
#         return redirect('../listar')
#     return render(request, 'mascota/mascota_form.html', {'form':form})

class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota_listar')

# def mascota_delete(request, id_mascota):
#     mascota=Mascota.objects.get(id=id_mascota)
#     if request.method=='POST':
#         mascota.delete()
#         return redirect('mascota_listar')
#     return render(request, 'mascota/mascota_delete.html', {'mascota': mascota})

class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'mascota/mascota_delete.html'
    success_url = reverse_lazy('mascota_listar')
        