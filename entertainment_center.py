import media
import movie_api
import config
import fresh_tomatoes

movies = []
movie_api.get_movie_list(config.themoviedb_list_id, movies)

print(movies)
