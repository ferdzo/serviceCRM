from django.db import models
from django.contrib.auth.models import UserManager
from nanoid import generate

def generate_nanoid():
    return generate(size=12)

class Insert(models.Model):
    ticket_id = models.CharField(max_length=12, default=generate_nanoid, unique=True, editable=False)
    name = models.CharField(max_length=50, verbose_name="Име")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    description = models.CharField(max_length=300, verbose_name="Опис")
    note= models.CharField(max_length=100, default=None, blank=True, null=True, verbose_name="Забелешка")
    date = models.DateField("Датум")
    done = models.BooleanField(default=False, verbose_name="Завршено")
    
    STATUS_CHOICES = [
        ('RECEIVED', 'Примено'),
        ('DIAGNOSING', 'Дијагностика'),
        ('WAITING_PARTS', 'Чека делови'),
        ('READY', 'Готово за подигање'),
        ('COMPLETED', 'Завршено'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='RECEIVED', verbose_name="Статус")
    
    date_close = models.DateField("Датум затворање", null=True, blank=True)
    repair = models.CharField(default=None, blank=True, null=True,max_length=300, verbose_name="Поправка")
    plateno = models.CharField(max_length=10, default=None, blank=True, null=True, verbose_name="Плаќање/Рег.")

    def save(self, *args, **kwargs):
        from django.utils import timezone
        
        # Sync done and status fields
        if self.status == 'COMPLETED':
            self.done = True
            if not self.date_close:
                self.date_close = timezone.now().date()
        elif self.done:
            self.status = 'COMPLETED'
            if not self.date_close:
                self.date_close = timezone.now().date()
        else:
            self.done = False
            
        super(Insert, self).save(*args, **kwargs)

    def __str__(self):
        return "Ime: " + self.name + " Telefonski broj: " + self.phone + "\nDefekt: " + self.description + "\nDatum: \n"

    def isDone(self):
        return self.done

class TicketLog(models.Model):
    ticket = models.ForeignKey(Insert, on_delete=models.CASCADE, related_name='logs')
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=50)
    details = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.ticket.ticket_id} - {self.action} at {self.timestamp}"
