from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Cliente
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='login')
def home(request):
    services = Cliente.objects.order_by('-id')
    limit_paginator = Paginator(services, 4)

    page_number = request.GET.get('page')
    services = limit_paginator.get_page(page_number)

    return render(request, 'service/home.html', {
        'services': services
    })

@login_required(redirect_field_name='login')
def view_customer(request, service_id):
    service = get_object_or_404(Cliente, id=service_id)
    return render(request, 'service/view_costumer.html', {
        'service': service
    })

@login_required(redirect_field_name='login')
def delete_customer(request, service_id):
    delete_customer = Cliente.objects.get(id=service_id)
    delete_customer.delete()
    messages.add_message(request, messages.SUCCESS, 'Cliente deletado com sucesso')
    return redirect('home')

@login_required(redirect_field_name='login')
def seach(request):
    termo = request.GET.get('termo')
    if termo is None or not termo:
        messages.add_message(request, messages.ERROR, 'Campo de busca não pode ficar vazio')
        return redirect('home')
    full_name = Concat('nome', Value(' '), 'sobrenome')
    services = Cliente.objects.annotate(
        name_full=full_name
    ).filter(
        name_full__icontains=termo
    )
    if termo != full_name:
        messages.add_message(request, messages.ERROR, 'Cliente não encontrado')
    limit_paginator = Paginator(services, 3)
    page_number = request.GET.get('page')
    services = limit_paginator.get_page(page_number)
    return render(request, 'service/seach.html', {
        'services': services
    })


