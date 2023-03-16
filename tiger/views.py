from django.shortcuts import render

# Create your views here.
def tiger1(request):
    return render(request,'tiger1.html')

def tiger2(request):
    return render(request,'tiger2.html')