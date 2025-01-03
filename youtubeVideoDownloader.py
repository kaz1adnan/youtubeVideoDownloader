import yt_dlp

def videoDownloader(url, savePath):

    options = {
        "outtmpl": f"{savePath}/%(title)s.%(ext)s",
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
    }
    ydl = yt_dlp.YoutubeDL(options)

    try:
        ydl.download(url)
        print("Download Successfully!")

    except Exception as e:
        print(e)

link = "https://www.youtube.com/watch?v=ls5BFzuxGw4"
location = r"F:\PyDownloads"

videoDownloader(link, location)