from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class noticia(models.Model):
	id_noticias = models.CharField(max_length=12, unique=True, primary_key=True)
	titulo = models.CharField(max_length=120, null=False, blank=False)
	sub_titulo = models.CharField(max_length=120, null=False, blank=False)
	descripcion = models.TextField(max_length=2000, null=False, blank=False)
	imagen = models.ImageField(upload_to='imagenesNoticia/%Y/%m/%d', verbose_name='Imagen')
	video = models.FileField(upload_to='videosNoticia/%Y/%m/%d', verbose_name='Video')
	tags = models.CharField(max_length=60)
	autor = models.CharField(max_length=60)
	fecha = models.DateField(null=False, blank=False)
	estatus = models.BooleanField()
	valoracion = models.IntegerField(null=False,blank=False)

	def __str__(self):
		return self.id_noticias

class recurso(models.Model):
	id_recurso = models.CharField(max_length=12, unique=True, primary_key=True)
	titulo = models.CharField(max_length=120, null=False, blank=False)
	sub_titulo = models.CharField(max_length=120, null=False, blank=False)
	descripcion = models.TextField(max_length=2000, null=False, blank=False)
	imagen = models.ImageField(upload_to='imagenesRecurso/%Y/%m/%d')
	video = models.FileField(upload_to='videosRecurso/%Y/%m/%d')
	tags = models.CharField(max_length=60)
	autor = models.CharField(max_length=60)
	estatus = models.BooleanField()
	valoracion = models.IntegerField(null=False,blank=False)
	tipo = models.CharField(max_length=60)
	
	def __str__(self):
		return self.id_recurso

class evento(models.Model):
	id_evento = models.CharField(max_length=12, unique=True, primary_key=True)
	titulo = models.CharField(max_length=120, null=False, blank=False)
	sub_titulo = models.CharField(max_length=120, null=False, blank=False)
	descripcion = models.TextField(max_length=2000, null=False, blank=False)
	imagen = models.ImageField(upload_to='imagenesEvento/%Y/%m/%d')
	video = models.FileField(upload_to='videosEvento/%Y/%m/%d')
	tags = models.CharField(max_length=60)
	autor = models.CharField(max_length=60)
	estatus = models.BooleanField()
	valoracion = models.IntegerField()
	fecha = models.DateField(null=False, blank=False)
	coordenada1 = models.CharField(max_length=60)
	coordenada2 = models.CharField(max_length=60)

	def __str__(self):
		return self.id_evento

class comentario(models.Model):
	id_comentario = models.CharField(max_length=12, unique=True, primary_key=True)
	comentario = models.TextField(max_length=600)
	fecha = models.DateField(null=False, blank=False)
	id_noticias = models.ForeignKey('noticia', null=True, blank=True)
	id_recursos = models.ForeignKey('recurso', null=True, blank=True)
	id_eventos = models.ForeignKey('evento', null=True, blank=True)
	
	def __str__(self):
		return self.id_comentario
