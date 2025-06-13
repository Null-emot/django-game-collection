from django.contrib import admin
from .models import Genre, Game

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'game_count')
    search_fields = ('name',)
    
    def game_count(self, obj):
        return obj.games.count()
    game_count.short_description = "Кількість ігор"

class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'rating', 'display_genres')
    list_filter = ('genres', 'year')
    search_fields = ('title',)
    filter_horizontal = ('genres',)
    
    def display_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])
    display_genres.short_description = "Жанри"

admin.site.register(Genre, GenreAdmin)
admin.site.register(Game, GameAdmin)