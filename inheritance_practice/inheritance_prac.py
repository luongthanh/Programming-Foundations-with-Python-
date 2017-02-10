import webbrowser 

class Video():
	def __init__(self, video_title, video_trailer, video_episode):
		self.title=video_title 
		self.trailer_youtube_url=video_trailer
		self.episode=video_episode 
	def show_trailer(self):
			webbrowser.open(self.trailer_youtube_url) 
	
class Movie(Video):
	def __init__(self, movie_title, movie_trailer, movie_description, movie_poster, movie_episode):
		Video.__init__(self, movie_title, movie_trailer, movie_episode) 
		self.storyline= movie_description
		self.poster_image_url=movie_poster
film1= Movie(movie_title="title1",movie_trailer="https://www.youtube.com/watch?v=FC6biTjEyZw",movie_episode=10, movie_description= "des1", 
	movie_poster="https://upload.wikimedia.org/wikipedia/en/8/86/Posternotebook.jpg")
film1.show_trailer()

# class TVshow
class TVshow(Video):
	def __init__(self, TVshow_title, TVshow_trailer, TVshow_episode):
		Video.__init__(self, TVshow_title, TVshow_trailer, TVshow_episode) 
		#self.description=description 
TVshow1= TVshow(TVshow_trailer="https://www.youtube.com/watch?v=92SgWpDYjlo", 
	TVshow_title ="des2", TVshow_episode=12)
TVshow1.show_trailer() 

