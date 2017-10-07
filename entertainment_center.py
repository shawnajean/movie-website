import media
import movie_api
import config
import site_generator

movies = []
movie_api.get_movie_list(config.themoviedb_list_id, movies)

site_generator.open_movies_page(movies)
