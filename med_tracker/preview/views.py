from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from preview.models import Equipment

def home(request):
    model = request.GET.get('model', '')
    return render(request,'home.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user.password == None:
            # If email matches but password does not
            messages.error(request, 'Contrasena invalida.')
            return redirect('sign_in')
        elif user is not None:
            # Redirect to a success page
            return redirect('equipments')
        else:
            # Return an error message
            messages.error(request, 'No existe el mail ingresado.')
            return redirect('sign_in')
    return render(request, 'sign_in.html')

def equipments(request):
    equipments = Equipment.objects.all()
    return render(request,'equipments.html', {'equipments': equipments})