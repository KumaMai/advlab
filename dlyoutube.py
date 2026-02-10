# pip install yt_dlp
# คำสั่งสำหรับติดตั้งไลบรารี yt_dlp (รันใน Terminal / CMD ก่อนใช้งาน)

import yt_dlp
# นำเข้าไลบรารี yt_dlp สำหรับดาวน์โหลดวิดีโอจาก YouTube

def download_youtube_video(url, save_path="."):
    """
    ฟังก์ชันสำหรับดาวน์โหลดวิดีโอจาก YouTube
    
    Parameters:
    url (str)       : ลิงก์วิดีโอ YouTube
    save_path (str) : โฟลเดอร์ที่ใช้บันทึกไฟล์ (ค่าเริ่มต้นคือโฟลเดอร์ปัจจุบัน)
    """

    # กำหนดตัวเลือกในการดาวน์โหลด
    ydl_opts = {
        # ตั้งชื่อไฟล์เป็นชื่อวิดีโอ และใช้นามสกุลตามประเภทไฟล์
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',

        # ดาวน์โหลดวิดีโอในคุณภาพดีที่สุดที่มี
        'format': 'best'
    }

    # สร้างอ็อบเจกต์ YoutubeDL พร้อมตัวเลือกที่กำหนด
    # ใช้ with เพื่อให้ระบบจัดการทรัพยากรให้อัตโนมัติ
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # เริ่มดาวน์โหลดวิดีโอจาก URL ที่ระบุ
        # ต้องใส่เป็น list แม้จะมีแค่ 1 URL
        ydl.download([url])

# รับลิงก์วิดีโอจากผู้ใช้ผ่านคีย์บอร์ด
video_url = input("Enter the YouTube video URL: ")

# เรียกใช้ฟังก์ชันดาวน์โหลด
# บันทึกไฟล์ไว้ในโฟลเดอร์ปัจจุบัน
download_youtube_video(video_url, save_path=".")
