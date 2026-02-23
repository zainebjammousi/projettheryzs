from django.db import models

class NOMS(models.Model):
    nom = models.CharField(max_length=20)

    class Meta:
        verbose_name = "NOMS"
        ordering = ['id']

    def __str__(self):
        return str(self.id)+": "+self.nom
