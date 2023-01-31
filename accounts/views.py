from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from accounts.models import Profile
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .models import FormCustomer
from .models import Cliente


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    user = request.POST.get('user')
    password = request.POST.get('password')

    user_confirmation = auth.authenticate(request, username=user, password=password)
    if not user:
        messages.error(request, 'Usuario ou senha inválidos')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user_confirmation)
        return redirect('dashboard')
        messages.success(request, 'BEM VINDO')
def logout(request):
    auth.logout(request)
    return redirect('login')


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
                user = User.objects.create_user(username=user, email=email, password=password, last_name=last_name, first_name=name)
                id_usuario = User.objects.get(username=user)
                perfil = Profile(user=id_usuario, registration=registration)
                perfil.save()
                user.save()
                messages.add_message(request, messages.SUCCESS, 'Usuario Cadastrado')
                return render(request, 'accounts/login.html')

    return render(request, 'accounts/register.html')

@login_required(redirect_field_name='login')
def dashboard(request):
    counter = Cliente.objects.all().count()
    profiles = User.objects.all().count()
    return render(request, 'accounts/dashboard.html', {'counter': counter, 'profiles': profiles})


@login_required(redirect_field_name='login')
def registerofcostumer(request):
    if request.method != 'POST':
        form = FormCustomer()
        return render(request, 'accounts/cadastro.html', {'form': form})

    form = FormCustomer(request.POST)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar formulario')
        form = FormCustomer(request.POST)
        return render(request, 'accounts/cadastro.html', {'form': form})


    form.save()
    messages.success(request, f'Cliente {request.POST.get("nome")} cadastrado com sucesso')
    return redirect('home')

