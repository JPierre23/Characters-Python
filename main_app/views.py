from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Character, Weapon
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import BattlesForm

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
    battles_form=BattlesForm()
    return render(request,'character/detail.html',{
        'character':character,
        'battles_form':battles_form,
        },)

def add_battle(request,character_id):
    form = BattlesForm(request.POST)
    if form.is_valid():
        new_Battle = form.save(commit=False)
        new_Battle.character_id=character_id
        new_Battle.save()
    return redirect('detail',character_id=character_id)

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
