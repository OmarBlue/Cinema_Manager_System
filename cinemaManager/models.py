from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator 

class LogMessage(models.Model):
    title = models.CharField(max_length=300)
    age_rating  = models.CharField(max_length=30, default='')
    duration = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(400)], default=0)
    description = models.CharField(max_length=350, default='')
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.title}' logged on {date.strftime('%A, %d %B, %Y at %X')}"
    