from moviepy.editor import *

file_path = "test.mp4"#トリミングしたい動画のパス

X_start= 200#切り出しのスタートｘ座標

Y_start = 0#切り出しのスタートy座標

X_length = 1700#X_startからの切り出す長さ

Y_length = 1440#Y_startからの切り出す長さ

save_path = "trimming.mp4"#保存先のパス

video = (VideoFileClip(file_path).crop(x1=X_start,y1=Y_start,x2=X_length,y2=Y_length))#トリミング実行

video.write_videofile(save_path,fps=29) #保存