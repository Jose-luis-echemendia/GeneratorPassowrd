from django.db import models

# Create your models here.


class Password(models.Model):
    """_summary_ 3comillas para generar documentacion

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    password = models.CharField(max_length=26, primary_key=True)

    def __str__(self) -> str:
        return Password

    class Meta:
        db_table = 'Password'
        managed = True
        verbose_name = 'Password'
        verbose_name_plural = 'Passwords'
