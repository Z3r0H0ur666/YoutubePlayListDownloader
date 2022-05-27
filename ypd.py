from pytube import Playlist
p = Playlist('https://www.youtube.com/playlist?list=PLpXus3JSQYPAGM2yGak01xZD7tuKXB3gQ')

print(f'Downloading: {p.title}')

for video in p.videos:
    print(video.title)
    st = video.streams.get_highest_resolution()
    st.download()
    #video.streams.first().download()
