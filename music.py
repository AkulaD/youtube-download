import yt_dlp
import os

def DownloadAudio(link):
    # Tentukan direktori tujuan
    output_folder = os.path.join(os.getcwd(), "audio")  # Folder 'audio' di lokasi skrip
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Buat folder jika belum ada

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        # Tentukan template output
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

link = input("Enter the YouTube video URL: ")
DownloadAudio(link)

