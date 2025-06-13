from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator  # Додано імпорт

class Genre(models.Model):
    """Модель жанру гри"""
    name = models.CharField(max_length=100, unique=True, verbose_name="Назва жанру")
    
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанри"
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Game(models.Model):
    """Модель відеогри"""
    title = models.CharField(max_length=200, verbose_name="Назва гри")
    year = models.PositiveIntegerField(verbose_name="Рік випуску")
    rating = models.FloatField(
        verbose_name="Рейтинг",
        help_text="Вкажіть рейтинг від 0 до 10",
        validators=[MinValueValidator(0), MaxValueValidator(10)]  # Тепер працюватиме
    )
    genres = models.ManyToManyField(Genre, related_name='games', verbose_name="Жанри")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата додавання")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")
    
    class Meta:
        verbose_name = "Гра"
        verbose_name_plural = "Ігри"
        ordering = ['-rating', 'title']
        unique_together = ['title', 'year']
    
    def __str__(self):
        return f"{self.title} ({self.year})"