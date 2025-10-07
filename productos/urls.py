from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.lista_productos, name='lista'),
    path('nuevo/', views.crear_producto, name='crear'),
    path('<int:pk>/', views.detalle_producto, name='detalle'),
    path('<int:pk>/editar/', views.editar_producto, name='editar'),
    path('<int:pk>/borrar/', views.borrar_producto, name='borrar'),
]