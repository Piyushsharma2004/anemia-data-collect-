from django.shortcuts import render, redirect
from . models import Allimage
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'test_image.html')

def collect(request,patient):
    # print(request.GET)
    # print(patient)
    # patient_id = request.GET.get('patient')
    # print(patient_id)
    context = {'patient_id' : patient}
    return render(request, "test_image.html", context)

def send(request):
    if request.method == "POST":
        patient_id = request.POST['patient_id']
        # usrName = request.POST['username']
        eye = request.POST['eye']
        palm = request.POST['palm']
        nails = request.POST['nails']
        full = request.POST['full']

        allimage_instance = Allimage(patient_id=patient_id)
        
        # Save the image data to the model instance
        allimage_instance.save_image_from_data(eye, "eye")
        allimage_instance.save_image_from_data(palm, "palm")
        allimage_instance.save_image_from_data(nails, "nails")
        allimage_instance.save_image_from_data(full, "full")
        # Save the model instance
        allimage_instance.save()
    return redirect('barcode')

def barcode(request):   
    if request.method == "POST":
        patient_id = request.POST['barcode']
        print(patient_id)
        return redirect('collect', patient_id)
        # return redirect(reverse("collect"),"?patient={patient_id}")
        # return redirect(reverse('collect')+"?q"+patient_id)
    return render(request, "patient.html")