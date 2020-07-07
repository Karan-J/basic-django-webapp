from django.shortcuts import render

# Create your views here.
def surat(request):
    return render(request,'surat.html')

def mumbai(request):
    return render(request,'mumbai.html')

def delhi(request):
    return render(request,'delhi.html')

def space(request):
    return render(request,'space.html')

def lonavala(request):
    return render(request,'lonavala.html')
