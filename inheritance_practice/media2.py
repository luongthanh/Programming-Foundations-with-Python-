import Inheritance_2 
import fresh_tomatoes2
Dear_John=Inheritance_2.Movie(movie_title="title1",
	movie_trailer="https://www.youtube.com/watch?v=FC6biTjEyZw",
	movie_episode=10, 
	movie_description= "des1", 
	movie_poster="https://upload.wikimedia.org/wikipedia/en/8/86/Posternotebook.jpg" )
	
Stocks= Inheritance_2.TVshow(TVshow_trailer="https://www.youtube.com/watch?v=92SgWpDYjlo", 
	TVshow_title ="des2", TVshow_episode=12, TVshow_poster="https://upload.wikimedia.org/wikipedia/en/3/3a/Flipped_poster.jpg")

movies=[Dear_John, Stocks]
fresh_tomatoes2.open_movies_page(movies)
fresh_tomatoes2.open_TVshow_page(TVshows) 

