from .models import *
from django.shortcuts import render, redirect
from .forms import PatientForm
from django.shortcuts import HttpResponse

def shto_pacient(request):
    form = PatientForm
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shto_pacient')
    context = {'form':form}
    return render(request, 'index.html', context)

def print_databazen(request):
    form = Patient.objects.all()
    context = {'form':form}
    return render(request, 'database.html', context)

def kerko_databazen(request):
    if 'search' in request.POST:
        search_id = request.POST.get('emri', None)
        form = Patient.objects.filter(emri=search_id)
        context = {'form':form}
        return render(request, 'database.html', context)
    return render(request, 'search.html')

def editRecord(request, pk):
    patient_id = Patient.objects.get(id=pk)
    form = PatientForm(instance=patient_id)  
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient_id)
        if form.is_valid():
            form.save()
            return redirect('databaza')
    context = {'form':form}
    return render(request, 'edit_record.html', context)

def deleteRecord(request, pk):
    patient_data = Patient.objects.get(id=pk)
    patient_data.delete()
    return redirect('databaza')