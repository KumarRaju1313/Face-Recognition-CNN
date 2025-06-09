import yt_dlp

def download_stream_in_720p(url, output_path):
    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',  # Limits the quality to 720p
        'outtmpl': output_path,
        'noplaylist': True,
        'quiet': False,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=mwN6l3O1MNI"
    output_path = "output_parking1.mp4"
    download_stream_in_720p(url, output_path)




