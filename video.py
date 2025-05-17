import yt_dlp
import os

def Download(link):
    # Tentukan folder untuk menyimpan file video
    output_folder = os.path.join(os.getcwd(), 'video')  # Folder 'video' di lokasi skrip
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Membuat folder jika belum adahttps://www.youtube.com/watch?v=pcwpWT4Xtv0

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Resolusi video terbaik
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),  # Simpan di folder 'video'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

link = input("Enter the YouTube video URL: ")
Download(link)
