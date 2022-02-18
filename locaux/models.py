from django.db import models


# Create your models here.
class local(models.Model):
    local_choices = {
        ("TP", "TP"),
        ("Cour", "Cour"),
        ("Reunion", "Reunion"),
        ("Sport", "Sport"),
        ("Bureau", "Bureau")
    }
    libelle = models.CharField(max_length=160)
    etat = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, blank=True)
    nb_post = models.IntegerField()
    nb_heure = models.IntegerField()
    type = models.CharField(max_length=10, choices=local_choices, default="Cour")
    description = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.libelle
