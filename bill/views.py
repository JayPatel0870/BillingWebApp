from .models import Owner, Customer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def index(request):
    customer = Customer.objects.all()
    return render(request, 'index.html', {'customer': customer})


def print(request):
    customer_id = request.GET.get('customer_id')
    customer = Customer.objects.get(pk=customer_id)
    owner = Owner.objects.all()
    product = request.GET.get('product', '')
    weight = request.GET.get('weight', '')
    gst = request.GET.get('gst', '')
    rate = request.GET.get('rate', '')
    return render(request, 'print.html', {'owner': owner, 'customer': [customer], 'product': product, 'weight':weight, 'gst':gst, 'rate':rate})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or homepage
            return redirect('index')  # Replace 'home' with the name of your homepage URL pattern
        else:
            # Return an invalid login message or render the login page again with an error
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
