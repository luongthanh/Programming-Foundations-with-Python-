
import webbrowser 

class Movie():
	"""This is a test for __doc__ """
	#array=["G","H","K"]
	def __init__(self, movie_title, movie_description, movie_poster, movie_trailer):
		self.title= movie_title
		self.storyline= movie_description
		self.poster_image_url=movie_poster
		self.trailer_youtube_url=movie_trailer
	def show_trailer(self):
			webbrowser.open(self.trailer_youtube_url) 

#toy_story=media.Movie("The note book","this is a romantic love story" ,"https://www.google.com.vn/search?q=the+notebook+poster&rlz=1C5CHFA_enVN695VN695&tbm=isch&imgil=XvCNfBfxigxPcM%253A%253B6GQQQu1FnC-ITM%253Bhttp%25253A%25252F%25252Fwww.joblo.com%25252Fmovie-posters%25252F2004%25252Fthe-notebook&source=iu&pf=m&fir=XvCNfBfxigxPcM%253A%252C6GQQQu1FnC-ITM%252C_&usg=__telUrlLV0XBqi_HJkKPWN6jLsaU%3D&biw=1364&bih=690&ved=0ahUKEwjkje7DoPvRAhVLkZQKHU-YBKQQyjcILA&ei=zk6YWOTuEsui0gTPsJKgCg#imgrc=XvCNfBfxigxPcM:",
 #"https://www.youtube.com/watch?v=rYMjdp1tggU")
#print(toy_story.title)