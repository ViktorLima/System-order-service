from django.contrib.auth.models import User
from django.shortcuts import render
from accounts.models import Profile
from django.contrib import messages


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')


def register(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        registration = request.POST.get('registration')
        list_of_registration = (user, password, password2, name, last_name, registration, email)
        for fields_form in list_of_registration:
            if not fields_form:
                messages.add_message(request, messages.ERROR, 'Os campos não podem ficar vazios')
            elif password != password2:
                messages.add_message(request, messages.INFO, 'Senha não conferem')
            else:
                user = User.objects.create_user(username=user, email=email, password=password)
                id_usuario = User.objects.get(username=user)
                perfil = Profile(user=id_usuario, registration=registration)
                perfil.save()
                user.save()
                messages.add_message(request, messages.SUCCESS, 'Usuario Cadastrado')
                return render(request, 'accounts/login.html')

    return render(request, 'accounts/register.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
