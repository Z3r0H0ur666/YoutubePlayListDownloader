from pytube import Playlist

print("""\033[91m
   _   _       _ _  _____ ___      _ ____  
 | \ | |     | | |/ ____/ _ \    | |___ \ 
 |  \| |_   _| | | |   | | | | __| | __) |
 | . ` | | | | | | |   | | | |/ _` ||__ < 
 | |\  | |_| | | | |___| |_| | (_| |___) |
 |_| \_|\__,_|_|_|\_____\___/ \__,_|____/ 
                                          
                                          \033[00m
				\033[93mv.1.2
				By NullC0d3\033[00m
""")
p = input("Enter the url of the playlist")

print(f'Downloading: {p.title}')

for video in p.videos:
    print(video.title)
    st = video.streams.get_highest_resolution()
    st.download()
    #video.streams.first().download()
