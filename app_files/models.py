from django.db import models
from app_user.models import CustomUser
from app_mapa.models import Map


class SourceFiles(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to='media/files/%Y/%m/%d/', blank=True, null=True)
    map = models.ForeignKey(Map, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    accessed = models.BooleanField(default=False)
    when_was_accessed = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Arquivos para elaboração dos Mapas'