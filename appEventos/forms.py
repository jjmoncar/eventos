from django import forms
from appEventos.models import noticia
from appEventos.models import recurso
from appEventos.models import evento
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NoticiaForm(forms.ModelForm):
	
	class Meta:
		model = noticia
		
		fields = [
			'id_noticias',
			'titulo',
			'sub_titulo',
			'descripcion',
			'imagen',
			'video',
			'tags',
			'autor',
			'valoracion',
			'fecha',
		]
		labels = {
			'id_noticias': 'id',
			'titulo': 'Titulo',
			'sub_titulo': 'Sub Titulo',
			'descripcion': 'Descripcion',
			'imagen': 'Imagen',
			'video': 'Video',
			'tags': 'Tags',
			'autor': 'Autor',
			'valoracion': 'Valoracion',
			'fecha': 'Fecha',
		}

class RecursoForm(forms.ModelForm):
	
	class Meta:
		model = recurso
		
		fields = [
			'id_recurso',
			'titulo',
			'sub_titulo',
			'descripcion',
			'imagen',
			'video',
			'tags',
			'autor',
			'valoracion',
		]
		labels = {
			'id_recurso': 'id',
			'titulo': 'Titulo',
			'sub_titulo': 'Sub Titulo',
			'descripcion': 'Descripcion',
			'imagen': 'Imagen',
			'video': 'Video',
			'tags': 'Tags',
			'autor': 'Autor',
			'valoracion': 'Valoracion',
		}
		
class EventoForm(forms.ModelForm):
	
	class Meta:
		model = evento
		
		fields = [
			'id_evento',
			'titulo',
			'sub_titulo',
			'descripcion',
			'imagen',
			'video',
			'tags',
			'autor',
			'valoracion',
		]
		labels = {
			'id_evento': 'id',
			'titulo': 'Titulo',
			'sub_titulo': 'Sub Titulo',
			'descripcion': 'Descripcion',
			'imagen': 'Imagen',
			'video': 'Video',
			'tags': 'Tags',
			'autor': 'Autor',
			'valoracion': 'Valoracion',
		}
			
class RegistroForm(UserCreationForm):
	
	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
			]
		labels = {
				'username': 'Usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellido',
				'email': 'Correo',
			}
