from django.db import models


class LocomotivePart(models.Model):
    parent = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        verbose_name='Родительская схема',
        null=True,
        blank=True,
        related_name='children'
    )
    schema_id = models.CharField(max_length=100, verbose_name='Чертежный номер')
    russian_name = models.CharField(max_length=100, verbose_name='Название на русском')
    chinese_name = models.CharField(max_length=100, verbose_name='Название на китайском', null=True, blank=True)
    quantity = models.CharField(max_length=100, verbose_name='Количество', null=True, blank=True)
    description = models.CharField(max_length=500, verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return str(self.pk)
