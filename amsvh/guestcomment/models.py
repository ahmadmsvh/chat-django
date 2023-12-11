from django.db import models

class Guest(models.Model):
    first_name = models.CharField(null=False, max_length=40)
    last_name = models.CharField(null=False, max_length=40)
    comment = models.TextField(null=False, max_length=400)

    def name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return f"{self.first_name} {self.last_name} : \"{self.comment}\""