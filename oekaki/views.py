from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from oekaki.models import Art
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    imgs = Art.objects.all()
    return render(request, "index.html", {"imgs": imgs})

@csrf_exempt
def imgpost(request):
    if request.method == "POST":
        a = request.POST["postimg"]
        theart = Art(imgbase64 = a)
        theart.save()
        return HttpResponse("SUCCESS")

    return render(request, "imgpost.html")