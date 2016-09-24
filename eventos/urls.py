"""eventos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from appEventos.views import principal, NoticiaCreate, RecursoCreate, EventoCreate, Inicio, RegistrarUsuario, noticia_list, NoticiaUpdate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Inicio.as_view(), name='Inicio'),
    url(r'^accounts/login/', login, {'template_name':'template/inicio.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^principal/', login_required(principal.as_view()), name='principal'),
    url(r'^nuevaNoticia/', login_required(NoticiaCreate.as_view()), name='nuevaNoticia'),
    url(r'^noticiaListar/', login_required(noticia_list.as_view()), name='noticiaListar'),
    url(r'^noticiaEditar/(?P<pk>[0-9]+)/$', login_required(NoticiaUpdate.as_view()), name='noticiaEditar'),
    url(r'^nuevoRecurso/', login_required(RecursoCreate.as_view()), name='nuevoRecurso'),
    url(r'^nuevoEvento/', login_required(EventoCreate.as_view()), name='nuevoEvento'),
    url(r'^registrarUsuario/', login_required(RegistrarUsuario.as_view()), name='registrarUsuario'),
    url(r'^reset/password_reset', password_reset, {'template_name':'template/registration/password_reset_form.html',
		'email_template_name':'template/registration/password_reset_email.html'}, name='password_reset'),	
	url(r'^reset/password_reset_done', password_reset_done, {'template_name':'template/registration/password_reset_done.html'}, 
		name='password_reset_done'),
	url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, {'template_name':'template/registration/password_reset_confirm.html'}, 
		name='password_reset_confirm'),
	url(r'^reset/done', password_reset_complete, {'template_name':'template/registration/password_reset_complete.html'}, 
		name='password_reset_complete'),
]
