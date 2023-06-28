from pytube import YouTube

def download_video(url, path):
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download(path)

# Use the function
download_video('https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'video')
