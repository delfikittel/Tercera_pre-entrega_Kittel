from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    # vista que se muestra apenas entras
    return render(request, 'Timeline/home.html')


def timeline(request):

    return render(request, 'Timeline/create.html')



# users
def usersFormulario(request):
    if request.method == 'POST':

        user = Users(
            name = request.POST['userName'],
            password = request.POST['userPass'],
            email = request.POST['userEmail']
        )
        
        user.save()
        return render(request, 'Timeline/home.html')
    
    return render(request, 'Timeline/usersFormulario.html')

def usersSearch(request):
    return render(request, 'Timeline/home.html')

def usersResults(request):
    if request.GET['name']:

        name = request.GET['name']
        users = Users.objects.filter(name__icontains = name)

        return render(request, 'Timeline/home.html', {'users': users, 'name': name})
        
    
    else:
        respuesta = 'No enviaste datos.'

    return HttpResponse(respuesta)

# events

def eventsFormulario(request):
    if request.method == 'POST':

        event = Events(
            name = request.POST['name'],
            descript = request.POST['eventDescript'],
            date = request.POST['eventDate'],
        )

        event.save()
        return render(request, 'Timeline/home.html')
    
    return render(request, 'Timeline/eventsFormulario.html') 

def eventsSearch(request):
    return render(request, 'Timeline/home.html')

def eventsResults(request):
    if request.GET['name']:

        name = request.GET['name']

        event = Events.objects.filter(name__icontains = name)

        return render(request, 'Timeline/home.html', {'event': event, 'name': name})
    

    else:
        respuesta = 'No enviaste datos.'

    return HttpResponse(respuesta)



def daySearch(request):
    return render(request, 'Timeline/home.html')



def dayResults(request):

    if request.GET['eventDate']:
        eventDate = request.GET['eventDate']

        fechas = Events.objects.filter(date__icontains = eventDate)

        return render(request, 'Timeline/home.html', {'fechas': fechas, 'eventDate': eventDate})

    else:
        respuesta = 'No enviaste datos.'

    return HttpResponse(respuesta)


# Periods

def periodsFormulario(request):
    if request.method == 'POST':

        event = Periods(
            name = request.POST['periodName'],
            descript = request.POST['periodDescript'],
            date1 = request.POST['periodDate1'],
            date2 = request.POST['periodDate2'],
        )

        event.save()
        return render(request, 'Timeline/home.html')
    
    return render(request, 'Timeline/periodsFormulario.html') 



def periodsSearch(request):
    return render(request, 'Timeline/home.html')

def periodsResults(request):
    if request.GET['periodName']:

        periodName = request.GET['periodName']

        period = Periods.objects.filter(name__icontains = periodName)

        return render(request, 'Timeline/home.html', {'period': period, 'periodName': periodName})
    

    else:
        respuesta = 'No enviaste datos.'

    return HttpResponse(respuesta)