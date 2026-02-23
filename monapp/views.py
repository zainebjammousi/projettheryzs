from django.shortcuts import render

from monapp.models import NOMS

# Create your views here.
def accueil(request):
    mon_nom = "Xavier"
    NOMS.objects.create(nom=mon_nom) # ajout direct dans la BDD
    noms = NOMS.objects.all()
    for nom in noms:
        print(nom.nom)
    return render(request, 'accueil.html',
                {'mon_nom':mon_nom,}
    )