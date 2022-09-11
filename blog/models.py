
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)


class Post(models.Model):
    DRAFT = 'DRAFT'
    PUBLISHED = 'PUBLISHED'
    HIDDEN = 'HIDDEN'
    READY = 'READY'
    STATUS_CHOICES = (
        (DRAFT, 'BORRADOR'),
        (PUBLISHED, 'PUBLICADO'),
        (HIDDEN, 'OCULTO'),
        (READY, 'LISTO'),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("Título", max_length=255)
    summary = models.TextField("Resumen")
    content = models.TextField("Contenido")
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("Fecha de última edición", auto_now=True)
    published = models.DateTimeField("Fecha de publicación", auto_now_add=True, null=True, blank=True)
    status = models.CharField("Estado", choices=STATUS_CHOICES, max_length=15, default=DRAFT)

    categories = models.ManyToManyField(Category, related_name="posts")

    def publish(self, *args, **kwargs):
        self.published = timezone.now()
        self.save()

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField("Comentario")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, related_name="comments")
    comments = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies')
