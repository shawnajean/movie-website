import media
import movie_api
import config
import site_generator

# This creates the movie array, fills it with information from a list on
# TheMovideDB via the API, and generates the website from that info.

movies = []
movie_api.get_movie_list(config.themoviedb_list_id, movies)
site_generator.open_movies_page(movies)
