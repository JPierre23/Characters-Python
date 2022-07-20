from django.shortcuts import render
from django.http import HttpResponse
from .models import Character, Weapon
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def character_index(request):
    characters = Character.objects.all()
    return render(request, 'character/index.html',{'characters':characters})

def character_detail(request,character_id):
    character= Character.objects.get(id=character_id)
    return render(request,'character/detail.html',{'character':character})

class CharacterCreate(CreateView):
    model=Character
    fields='__all__'
    # success_url='/character/'

class CharacterUpdate(UpdateView):
    model= Character
    fields=['description','status','power_level']

class CharacterDelete(DeleteView):
    model=Character
    success_url='/character/'

def weapon_index(request):
    weapons = Weapon.objects.all()
    return render(request, 'weapon/index.html',{'weapons':weapons})

def weapon_detail(request,weapon_id):
    weapon= Weapon.objects.get(id=weapon_id)
    return render(request,'weapon/detail.html',{'weapon':weapon})

class WeaponCreate(CreateView):
    model=Weapon
    fields='__all__'

class WeaponUpdate(UpdateView):
    model=Weapon
    fields={'type','description'}

class WeaponDelete(DeleteView):
    model=Weapon
    success_url='/weapon/'
