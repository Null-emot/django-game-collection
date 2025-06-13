import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

from games.models import Genre, Game

def create_genres():
    genres = [
        "RPG", "Action", "Adventure", "Strategy", 
        "FPS", "Puzzle", "Sports", "Simulation"
    ]
    for name in genres:
        Genre.objects.get_or_create(name=name)
    print("Створено жанри:", Genre.objects.count())

def create_games():
    games_data = [
        {
            "title": "The Witcher 3: Wild Hunt",
            "year": 2015,
            "rating": 9.7,
            "genres": ["RPG", "Action", "Adventure"]
        },
        {
            "title": "Portal 2",
            "year": 2011,
            "rating": 9.5,
            "genres": ["Puzzle", "Adventure"]
        },
        {
            "title": "Red Dead Redemption 2",
            "year": 2018,
            "rating": 9.8,
            "genres": ["Action", "Adventure"]
        }
    ]
    
    for game_data in games_data:
        game, created = Game.objects.get_or_create(
            title=game_data['title'],
            year=game_data['year'],
            defaults={'rating': game_data['rating']}
        )
        
        for genre_name in game_data['genres']:
            genre = Genre.objects.get(name=genre_name)
            game.genres.add(genre)
        
        print(f"{'Створено' if created else 'Оновлено'}: {game}")

if __name__ == "__main__":
    create_genres()
    create_games()