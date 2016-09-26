from django import forms
from appEventos.models import noticia, recurso, evento
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
			'fecha',
			'estatus',
			'valoracion',
		]
		labels = {
			'id_noticias': 'Id',
			'titulo': 'Titulo',
			'sub_titulo': 'Sub Titulo',
			'descripcion': 'Descripcion',
			'imagen': 'Imagen',
			'video': 'Video',
			'tags': 'Tags',
			'autor': 'Autor',
			'fecha': 'Fecha',
			'estatus': 'Estatus',
			'valoracion': 'Valoracion',
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
			'estatus',
			'valoracion',
			'tipo',
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
			'estatus': 'Estatus',
			'valoracion': 'Valoracion',
			'tipo': 'Tipo',
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
			'estatus',
			'valoracion',
			'fecha',
			'coordenada1',
			'coordenada2',
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
			'estatus': 'Estatus',
			'valoracion': 'Valoracion',
			'fecha': 'Fecha',
			'coordenada1': 'Coordenada 1',
			'coordenada2': 'Coordenada 2',
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
