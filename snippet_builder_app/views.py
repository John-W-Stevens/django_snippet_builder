from django.shortcuts import render, redirect
from . import models
# Create your views here.

def snippet_builder(request):
    # POST request
    if request.POST:
        # process error message
        if request.POST["content"] == "":
            return redirect("/snippet_builder")
        error_message = models.ErrorMessage.objects.create(content=request.POST["content"])
        if request.POST["name"]:
            error_message.author = request.POST["name"]
        if request.POST["email"]:
            error_message.email = request.POST["email"]
        error_message.save()
        return redirect("/snippet_builder")
    # GET request
    return render(request, "snippet_builder.html")

def index(request):
    return render(request, "index.html")