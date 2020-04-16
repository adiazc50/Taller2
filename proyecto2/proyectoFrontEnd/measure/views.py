from django.shortcuts import render,  HttpResponse
 
# Create your views here.
def measure(request):
    return render(request, "measure/measure.html")