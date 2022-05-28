import cv2
import sys
from moviepy.editor import *

def main():
    try:
        f = open('movie_trimming_input.txt', 'r')
    except:
        print("Error")
        return

    datalist = f.readlines()
    for i in range(len(datalist)):
        datalist[i] = datalist[i].rstrip('\n')

    f.close()

    movie_trimming(datalist[0], datalist[1], datalist[2], datalist[3])

def movie_trimming(video_path, trim_video_path, start, end):
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print('Capture_Error')
        return
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_num = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    print("総フレーム数：%d" % frame_num)
    print("フレームレート：%f\n" % fps)

    video = VideoFileClip(video_path).subclip(start, end)
    video.write_videofile(trim_video_path, fps)

    cap = cv2.VideoCapture(trim_video_path)
    print("\n処理後総フレーム数：%d" % cap.get(cv2.CAP_PROP_FRAME_COUNT))

main()