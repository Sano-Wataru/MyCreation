import numpy as np
import cv2
import os 
from PIL import Image

#プログラム実行用関数
def main():
    #引数をファイルから受け取る
    try:
        f = open('movie_to_animation_input.txt', 'r')
    except:
        print("Error")
        return

    datalist = f.readlines()
    for i in range(len(datalist)):
        datalist[i] = datalist[i].rstrip('\n')

    f.close()

    save_all_frames(datalist[0], datalist[1], datalist[2], datalist[3], \
                    datalist[4], datalist[5], datalist[6], datalist[7])

#imgname: 出力後の画像名
#w,h: 画像１ブロックあたりの縦横サイズ
#frame_width,frame_height: 画像の縦横フレーム数
def save_all_frames(video_path, dir_path, imgname, ext, w, h, frame_width, \
                    frame_height):
    cap = cv2.VideoCapture(video_path)

    #例外処理
    if not cap.isOpened():
        print("Capture_Error")
        return

    frame_width,frame_height = int(frame_width),int(frame_height)
    #何フレーム毎に読み込むか
    frame_count = \
        int(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) / \
        frame_height/frame_width)
    #リサイズ後の画像サイズ（出力画像一フレーム当たりのサイズ）
    W,H = int(w),int(h)
    #出力用行列の用意
    img_out = np.zeros((H*frame_height,W*frame_width,3),int)
    #キャプチャ範囲指定用
    nx,ny = 0,0
    #取得フレーム用
    fc = 0
    #フラグ変数
    check = False

    #保存先ディレクトリ作成
    os.makedirs(dir_path, exist_ok=True)

    for y in range(frame_height):
        for x in range(frame_width):
            #一フレーム読み込む
            #フレームカウント毎に書き出し処理へ移行
            while(fc < frame_count):
                ret, frame = cap.read()
                #最初の一回は通す
                if(check == False):
                    check = True
                    break
                #画像がなくなったらループを抜ける１
                if(ret == False):
                    break
                fc += 1
            #画像がなくなったらループを抜ける２
            if(ret == False):
                break
            fc = 0

            #一時ファイルパス
            temp_path = os.path.join(dir_path, imgname + '_temp') + '.' + ext
            #一時ファイルの書き出し
            cv2.imwrite(temp_path, frame)
            
            #画像のリサイズ
            img = Image.open(temp_path)
            img_resized = img.resize((int(w), int(h)))
            img_resized.save(temp_path, quality=100)

            #リサイズ画像の読み出し
            img = cv2.imread(temp_path)

            #出力画像に書き込み
            img_out[ny:H+ny,nx:W+nx] = img[0:H,0:W]
            nx += W
        #画像がなくなったらループを抜ける３
        if(ret == False):
            break
        #縦を一つ進め横は左に戻す
        nx = 0
        ny += H
        
    os.remove(temp_path)
    img_path = os.path.join(dir_path, imgname + '.' + ext)
    cv2.imwrite(img_path, img_out)

main()