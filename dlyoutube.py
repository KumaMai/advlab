import yt_dlp

def download_youtube(url):
    ydl_opts = {
        'format': 'best',     # ดาวน์โหลดคุณภาพดีที่สุด
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
