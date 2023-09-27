from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('home/', home, name = 'home'),
    path('create/', timeline, name = 'createtimeline'),
    
    #formularios
    path('usersFormulario/', usersFormulario, name= 'usersFormulario' ),
    path('usersSearch/', usersSearch, name = 'usersSearch'),
    path('usersResults/', usersResults, name = 'usersResults'), 

    path('eventsFormulario/', eventsFormulario, name = 'eventsFormulario'),
    path('eventsSearch/', eventsSearch, name = 'eventsearch'),
    path('eventsResults/', eventsResults, name = 'eventResults'),
    path('daySearch/', daySearch, name = 'daySearch'),
    path('dayResults/', dayResults, name = 'dayResults'),

    path('periodsFormulario/', periodsFormulario, name = 'periodsFormulario'),
    path('periodsSearch/', periodsSearch, name = 'periodsSearch'),
    path('periodsResults/', periodsResults, name = 'periodsResults'),
    ]