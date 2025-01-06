from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_principal, name='menu_principal'),
    path('platillo/<int:platillo_id>/', views.detalle_platillo, name='detalle_platillo'),
    path('platillo/<int:platillo_id>/editar/', views.editar_platillo, name='editar_platillo'),
    path('platillo/<int:platillo_id>/eliminar/', views.eliminar_platillo, name='eliminar_platillo'),
    path('agregar_platillo/', views.agregar_platillo, name='agregar_platillo'),
    path('platillo/<int:platillo_id>/comentario/', views.agregar_comentario, name='agregar_comentario'),
    path('platillo/<int:platillo_id>/comentario/<int:comentario_id>/editar/', views.editar_comentario, name='editar_comentario'),
    path('platillo/<int:platillo_id>/comentario/<int:comentario_id>/eliminar/', views.eliminar_comentario, name='eliminar_comentario'),
]
