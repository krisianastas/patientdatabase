from django.shortcuts import render
from django.shortcuts import HttpResponse
from homepage.models import Formular

def home_screen_view(request):
    if 'search' in request.POST:
        try:
            search_id = request.POST.get('name', None)
            user = Formular.objects.get(name=search_id)
            context = {'user':user}
            return render(request, 'index.html', context)
        except Formular.DoesNotExist:
            return HttpResponse("Nuk gjendet një rekord me këtë emër.")  
    elif 'update' in request.POST:
        try:
            search_id = request.POST.get('name', None)
            user = Formular.objects.get(name=search_id)
            name=request.POST['name']
            email=request.POST['email']
            tel=request.POST['tel']
            mjeku=request.POST['mjeku']
            data=request.POST['data']
            price=request.POST['price']
            services=request.POST['services']
            Formular.objects.update(name=name,email=email,tel=tel,mjeku=mjeku,data=data,price=price,services=services)
            return HttpResponse("Rekordi u përditësua me sukses.")
        except:
            return HttpResponse("Ndodhi një gabim.") 
    elif 'create' in request.POST:
        try:
            name=request.POST['name']
            email=request.POST['email']
            tel=request.POST['tel']
            mjeku=request.POST['mjeku']
            data=request.POST['data']
            price=request.POST['price']
            services=request.POST['services']
            f = Formular.objects.create(name=name,email=email,tel=tel,mjeku=mjeku,data=data,price=price,services=services)
            f.save()
            return render(request, 'index.html')
        except:
            return HttpResponse("Ndodhi një gabim.")    
    elif 'delete' in request.POST:
        try:
            search_id = request.POST.get('name', None)
            user = Formular.objects.get(name=search_id) 
            user.delete()
            return HttpResponse("Rekordi u fshi me sukses.") 
        except:
            return HttpResponse("Ndodhi një gabim.")     
    elif 'manual' in request.POST:
        return render(request, 'manual.html')
    else:
        return render(request, 'index.html')