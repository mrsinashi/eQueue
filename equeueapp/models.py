from django.db import models

class Cabinet(models.Model):
    cabinetid = models.IntegerField(db_index=True, help_text='Номер кабинета')
    name = models.CharField(max_length=48, db_index=True, help_text='Название кабинета')

    def __str__(self):
        return "{0} - {1}".format(self.cabinetid, self.name)

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'

class Queue(models.Model):
    queueid = models.IntegerField(blank=True, db_index=True, help_text='Номер очереди')
    cabinetid = models.ForeignKey(Cabinet, help_text="Кабинет", on_delete=models.PROTECT)
    priority = models.IntegerField(default='0', db_index=True, help_text='Приоритет в очереди')

    def display_cabinet(self):
        return ', '.join([cabinetid.name for cabinetid in self.cabinetid.all()[:3]])
        display_cabinet.short_description = 'Cabinet'

    def __str__(self):
        return "{0}. {1} [{2}]".format(self.queueid, self.cabinetid, self.priority)

    class Meta:
        verbose_name = 'Очередь'
        verbose_name_plural = 'Очереди'