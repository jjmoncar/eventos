from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User 
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, TemplateView, CreateView
from appEventos.models import noticia, recurso, evento
from appEventos.forms import NoticiaForm, RecursoForm, EventoForm, RegistroForm

class principal(TemplateView):
	template_name = 'template/principal.html'
	
class RegistrarUsuario(CreateView):
	model = User
	template_name = 'template/registrarUsuario.html'
	form_class = RegistroForm
	success_url = reverse_lazy('principal')

class Inicio(TemplateView):
	template_name = 'template/index.html'

class NoticiaCreate(CreateView):
	model = noticia
	template_name = 'template/noticia_form.html'
	form_class = NoticiaForm
	success_message = "Noticia Creada con Exito!"
	success_url = reverse_lazy('principal')

class RecursoCreate(CreateView):
	model = recurso
	template_name = 'template/recurso_form.html'
	form_class = RecursoForm
	success_message = "Recurso Creado con Exito!"
	success_url = reverse_lazy('principal')
	
class EventoCreate(CreateView):
	model = evento
	template_name = 'template/evento_form.html'
	form_class = EventoForm
	success_message = "Evento Creado con Exito!"
	success_url = reverse_lazy('principal')

class noticia_list(ListView):
	model = noticia
	template_name='template/noticia_listar.html'
	paginate_by = 2
