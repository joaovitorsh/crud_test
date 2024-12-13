from django.db import models


class Post(models.Model):
    """Modelo que representa um post criado por um usuário."""

    username = models.CharField(max_length=255)
    created_datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self) -> str:
        """Representação legível do modelo."""
        return self.title
