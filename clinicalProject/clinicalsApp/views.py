from django.shortcuts import render, redirect

from .forms import ClinicalDataForm
from .models import  Patient,ClinicalData
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

class PatientListView(ListView):
    model=Patient


class PatientCreateView(CreateView):
    model=Patient
    success_url=reverse_lazy('clinicalsApp:PatientListView')
    fields=('firstName','lastName','age')

class PatientUpdateView(UpdateView):
    model = Patient
    success_url = reverse_lazy('clinicalsApp:PatientListView')
    fields = ('firstName', 'lastName', 'age')

class PatientDeleteView(DeleteView):
    model=Patient
    success_url = reverse_lazy('clinicalsApp:PatientListView')

def addClinicalData(request,**kwargs):
    form=ClinicalDataForm()
    patient=Patient.objects.get(id=kwargs['pk'])
    if request.method=='POST':
        form=ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'clinicalsApp/clinicalDataForm.html',{'form':form,'patient':patient})

def analyze(request,**kwargs):
    data=ClinicalData.objects.filter(patient_id=kwargs['pk'])
    responseData=[]
    for eachEntry in data:
        if eachEntry.componentName == "hw":
            heightAndWeight=eachEntry.componentValue.split("/")
            if(len(heightAndWeight)>1):
                height=float(heightAndWeight[0])* 0.436
                bmi=float(heightAndWeight[1]) /(height*height)
                bmiEntry=ClinicalData()
                bmiEntry.componentName="BMI"
                bmiEntry.componentValue=bmi
                responseData.append(bmiEntry)
        responseData.append(eachEntry)
    return render(request,'clinicalsApp/getReport.html',{'data':responseData})



