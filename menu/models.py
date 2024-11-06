from django.db import models
from django.utils.translation import gettext_lazy as _

class Menu(models.Model):
    name = models.CharField(max_length=200, verbose_name="Назва")
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url = models.CharField(max_length=200, blank=True, verbose_name="URL")

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Вкладене меню"

    def __str__(self):
        return self.name
