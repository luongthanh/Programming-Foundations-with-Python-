import fresh_tomatoes 
import class_Movie

Dear_John=class_Movie.Movie("Dear John",
	"Story about youth, love, and destiny." ,
	"https://upload.wikimedia.org/wikipedia/en/3/35/Dear_John_film_poster.jpg", 
	"https://www.youtube.com/watch?v=bJ9lRqSGI24")
#print(romantic_story.title)
#romantic_story.show_trailer()


Lord_Rings= class_Movie.Movie("The Lord of the Rings", 
	"Story about youth, love, and destiny.", 
	"https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",
	"https://www.youtube.com/watch?v=r5X-hFf6Bwo")

flipped= class_Movie.Movie("Flipped",
	"Flipped is a 2010 American romantic comedy-drama film directed by Rob Reiner and based on Wendelin Van Draanen's novel of the same name.",
	"https://upload.wikimedia.org/wikipedia/en/3/3a/Flipped_poster.jpg",
	"https://www.youtube.com/watch?v=92SgWpDYjlo")
Lalaland= class_Movie.Movie("Lalaland",
	"La La Land is a 2016 American musical drama written and directed by Damien Chazelle and starring Ryan Gosling and Emma Stone as a musician and an aspiring actress who meet and fall in love in Los Angeles. The film's title refers both to the city of Los Angeles and to the idiom for being out of touch with reality.",
	"https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
	"https://www.youtube.com/watch?v=0pdqf4P9MB8")
Stocks= class_Movie.Movie("Stocks",
	"Storks is a 2016 American 3D computer-animated adventure buddy comedy film produced by Warner Animation Group, RatPac-Dune Entertainment[1] and Stoller Global Solutions. ",
	"https://upload.wikimedia.org/wikipedia/vi/6/60/Storks_%28film%29_poster.jpg",
	"https://www.youtube.com/watch?v=ZVzL94jZNdU")
Star_wars= class_Movie.Movie("Star Wars",
	"Star Wars is a 1977 American epic space opera film written and directed by George Lucas. The first installment in the Star Wars film series, it stars Mark Hamill, Harrison Ford, Carrie Fisher, Peter Cushing, and Alec Guinness. David Prowse, James Earl Jones, Anthony Daniels, Kenny Baker, and Peter Mayhew co-star in supporting roles.",
	"https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
	"https://www.youtube.com/watch?v=sGbxmsDFVnE")
movies=[Dear_John, Lord_Rings, flipped, Lalaland, Stocks, Star_wars]
#print(class_Movie.Movie.array)
fresh_tomatoes.open_movies_page(movies)
#print(class_Movie.Movie.__doc__)
#print(class_Movie.Movie.__module__)
#print(class_Movie.Movie.__name__)
