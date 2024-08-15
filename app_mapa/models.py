from django.db import models, IntegrityError
from django.db.models.signals import pre_save
from django.dispatch import receiver
from app_user.models import CustomUser
from app_fazenda.models import Farm


class Map(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255,blank=True, null=True)
    lat = models.CharField(max_length=50, blank=True, null=True)
    long = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    main_map_selected = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Mapas"
        # Restrição única no banco de dados para farm e main_map_selected
        unique_together = ('farm', 'main_map_selected')

@receiver(pre_save, sender=Map)
def ensure_single_main_map_selected(sender, instance, **kwargs):
    if instance.main_map_selected:
        # Verifica se já existe algum outro Map com main_map_selected=True para o mesmo farm
        if Map.objects.filter(farm=instance.farm, main_map_selected=True).exists():
            # Se existir, lança uma exceção ou define como False
            instance.main_map_selected = False  # Pode definir como False ou lançar uma exceção
            # Exemplo de lançar exceção:
            raise IntegrityError('Somente um mapa pode ser o principal por fazenda, por favor redefina suas configurações!')