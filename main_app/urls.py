from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('character/create/', views.CharacterCreate.as_view(), name='character_create'),
  path('character/', views.character_index, name='character'),
  path('character/<int:character_id>/', views.character_detail, name='detail'),
  path('character/<int:pk>/update/', views.CharacterUpdate.as_view(), name='character_update'),
  path('character/<int:pk>/delete/', views.CharacterDelete.as_view(), name='character_delete'),
  path('character/<int:character_id>/add_battle', views.add_battle,name='add_feeding'),
  path('weapon/create/', views.WeaponCreate.as_view(), name='weapon_create'),
  path('weapon/', views.weapon_index, name='weapon'),
  path('weapon/<int:weapon_id>/', views.weapon_detail, name='weapon_detail'),
  path('weapon/<int:pk>/update/', views.WeaponUpdate.as_view(), name='weapon_update'),
  path('weapon/<int:pk>/delete/', views.WeaponDelete.as_view(), name='weapon_delete')
]