import yt_dlp

def download_youtube(url):
    print("\nเลือกระดับความชัดของวิดีโอ")
    print("1) 360p")
    print("2) 480p")
    print("3) 720p (HD)")
    print("4) 1080p (Full HD)")
    print("5) คุณภาพสูงสุด")

    choice = input("กรุณาเลือก (1-5): ")

    format_map = {
        "1": "bestvideo[height<=360]+bestaudio/best[height<=360]",
        "2": "bestvideo[height<=480]+bestaudio/best[height<=480]",
        "3": "bestvideo[height<=720]+bestaudio/best[height<=720]",
        "4": "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
        "5": "best"
    }

    ydl_opts = {
        'format': format_map.get(choice, 'best'),
        'merge_output_format': 'mp4',
        'outtmpl': '%(title)s.%(ext)s'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("กำลังดาวน์โหลด...")
            ydl.download([url])
            print("ดาวน์โหลดเสร็จสิ้น")
    except Exception as e:
        print("เกิดข้อผิดพลาด:", e)


if __name__ == "__main__":
    url = input("กรุณาใส่ URL ของ YouTube: ")
    download_youtube(url)
