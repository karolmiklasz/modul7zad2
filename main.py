import random

class MediaLibrary:
    def __init__(self):
        self.media_collection = []
    
    def add_media(self, media):
        self.media_collection.append(media)
    
class Media:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre 
        self.play_count = 0
    
    def play(self):
        self.play_count += 1
    
    def __str__(self):
        return f"{self.title} ({self.year})"
    
class Movie(Media):
    def __init__(self, title, year, genre):
        super().__init__(title, year, genre)

class Series(Media):
    def __init__(self, title, year, genre, season=1, episode=1):
        super().__init__(title, year, genre)
        self.season = season
        self.episode = episode

    def play(self):
        super().play()
        self.episode += 1
        if self.episode > 10:
            self.episode = 1
            self.season += 1
    
    def __str__(self):
        season_str = str(self.season).zfill(2)
        episode_str = str(self.episode).zfill(2)
        return f"{self.title} S{season_str}E{episode_str}"
    
def get_movies(media_library):
    movies = [media for media in media_library.media_collection if isinstance(media, Movie)]
    return sorted(movies, key=lambda x: x.title)

def get_series(media_library):
    series = [media for media in media_library.media_collection if isinstance(media, Series)]
    return sorted(series, key=lambda x: x.title)

def search(media_library, title):
    return [media for media in media_library.media_collection if title.lower() in media.title.lower()]

def generate_views(media_library):
    random_media = random.choice(media_library.media_collection)
    random_views = random.randint(1, 100)
    for _ in range(random_views):
        random_media.play()

def generate_views_multiple_times(media_library, n=10):
    for _ in range(n):
        generate_views(media_library)

def top_titles(media_library, num_titles, content_type=None):
    if content_type == 'movies':
        sorted_media = get_movies(media_library)
    elif content_type == 'series':
        sorted_media = get_series(media_library)
    else:
        sorted_media = media_library.media_collection

    sorted_media.sort(key=lambda x: x.play_count, reverse=True)
    return sorted_media[:num_titles]

# Example:
library = MediaLibrary()

movie1 = Movie("Pulp Fiction", 1994, "Crime")
movie2 = Movie("The Godfather", 1972, "Drama")
series1 = Series("Breaking Bad", 2008, "Drama")

library.add_media(movie1)
library.add_media(movie2)
library.add_media(series1)

movie1.play()
movie2.play()
series1.play()
series1.play()

generate_views_multiple_times(library)

print("Top 2 Movies:")
top_movies = top_titles(library, 2, content_type='movies')
for movie in top_movies:
    print(movie, f"({movie.play_count} views)")

print("\nTop 2 Series:")
top_series = top_titles(library, 2, content_type='series')
for series in top_series:
    print(series, f"({series.play_count} views)")

print("\nAll Media in Library:")
for media in library.media_collection:
    print(media, f"({media.play_count} views)")

search_result = search(library, "The")
print("\nSearch Results:")
for result in search_result:
    print(result)
    