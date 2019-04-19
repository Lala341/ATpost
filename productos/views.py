from .models import Producto, Venta
from django.shortcuts import render, redirect
from .forms import  ProductoForm, VentaForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.http import HttpResponse
import json
# Create your views here.
from django.contrib.auth.decorators import login_required
import social_django


def index(request):
    template='index.html'
    ventas= Venta.objects.all()
    jsondata = serializers.serialize('json',ventas)
    context={
		'results':ventas,
		'jsondata':jsondata,
	}
    return render(request,template,context)

def productos(request):
	template='Producto/productos.html'
	results=Producto.objects.all()
	jsondata = serializers.serialize('json',results)
	context={
		'results':results,
		'jsondata':jsondata,
	}
	return render(request,template,context)

def getdata(request):

    ventas= Venta.objects.all()
    jsondata = serializers.serialize('json',ventas)
    return HttpResponse(jsondata)

def base_layout(request):
	template='base.html'
	return render(request,template)

def ProductoList(request):
    queryset = Producto.objects.all()
    context = {
        'producto_list': queryset
    }
    return render(request, 'Producto/productos.html', context)

def ProductoCreate(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            producto.save()
            messages.add_message(request, messages.SUCCESS, 'Producto create successful')
            return HttpResponseRedirect(reverse('productoList'))
        else:
            print(form.errors)
    else:
        form = ProductoForm()

    context = {
        'form': form,
    }

    return render(request, 'Producto/productoCreate.html', context)

def ProductoUpdate(request,pk):
    producto= Producto.objects.get(id=pk)
    if request.method == 'GET':
        form= ProductoForm(instance=producto)
    else:
        form= ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Producto update successful')
            return HttpResponseRedirect(reverse('productoList'))

    context = {
        'form': form,
    }

    return render(request, 'Producto/productoUpdate.html', context)

def VentaList(request):
    queryset = Venta.objects.all()
    context = {
        'venta_list': queryset
    }
    return render(request, 'Venta/ventas.html', context)

def VentaCreate(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save()
            venta.save()
            messages.add_message(request, messages.SUCCESS, 'Venta create successful')
            return HttpResponseRedirect(reverse('ventaCreate'))
        else:
            print(form.errors)
    else:
        form = VentaForm()

    context = {
        'form': form,
    }

    return render(request, 'Venta/ventaCreate.html', context)




@login_required
def dashboard(request):
    user = request.user
    auth0user = user.social_auth.get(provider='auth0')
    userdata = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture']
    }

    return render(request, 'dashboard.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4)
    })

def logout(request):
    log_out(request)
    return_to = urlencode({'returnTo': request.build_absolute_uri('/')})
    logout_url = 'https://%s/v2/logout?client_id=%s&%s' % \
                 (settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
    return HttpResponseRedirect(logout_url)

def getRole(request):
    user = request.user
    auth0user = user.social_auth.get(provider="auth0")
    accessToken = auth0user.extra_data['access_token']
    url = "https://isis2503-ivan-alfonso.auth0.com/userinfo"
    headers = {'authorization': 'Bearer ' + accessToken}
    resp = requests.get(url, headers=headers)
    userinfo = resp.json()
    role= userinfo['https://isis2503-ivan-alfonso:auth0:com/role']
    return (role)
