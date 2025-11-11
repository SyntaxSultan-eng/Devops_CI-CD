from django.db import models

class Counter(models.Model):
    
    def __str__(self):
        return f"Counter: {self.value}"
