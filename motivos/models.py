from django.db import models

class Bilhete(models.Model):
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mensagem
