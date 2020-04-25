from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

def home(request):
    return render(request, 'products/home.html')

@login_required     #if user is not loggedin it will send to login page
def create(request):
    if request.method=='POST':
        if request.POST['titles'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.titles=request.POST['titles']
            product.body= request.POST['body']
            if request.POST['url'].startswith('https://') or request.POST['url'].startswith('https://'):
                product.url= request.POST['url']
            else:
                product.url= 'https://' + request.POST['url']
            product.icon=request.FILES['icon']
            product.image=request.FILES['image']
            product.pub_date= timezone.datetime.now()
            product.hunter=request.user
            product.save()
            return redirect('home')

        else:
            return render(request, 'products/create.html', {'error':'All fields required'})

    return render(request, 'products/create.html')
