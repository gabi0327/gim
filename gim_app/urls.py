from django.urls import path
from. import views,views_usuario


urlpatterns = [
    

    path('admin/', views.admin, name='admin'),
    path('login/', views.login_view, name='login'),

    path('registrar_admin/', views_usuario.registrar_admin, name='registrar_admin'),
    path('mostrar_usuarios/', views_usuario.mostrar_usuarios, name='mostrar_usuarios'),
    path('eliminar_usuario/', views_usuario.eliminar_usuario, name='eliminar_usuario'),





 



]