'''
# FPSが変化しても毎秒の加算数が変わらない関数

## できること
    - sleepでFPSを調整して、処理開始秒数から前回の処理終了時間を引いて、経過時間を表している
    - 経過秒数を毎秒の加速量(speed)に掛けて計算することでFPSに頼らない計算ができる

## 問題点
    このままではマイナスの計算ができないとか、まあいろいろ
'''
from time import time, sleep


def delay(pos, x, speed, fps):
    milli = lambda: round(time() * 1000)  # ミリ秒を返す関数
    sec = 0
    pos = -10
    tmp = 0  # print用
    ed = milli()
    while pos < x:
        st = milli()
        sec = (st - ed) / 1000  # 待ち時間を秒に直して代入
        tmp += sec
        pos += speed * sec
        print("pos:{:.2f} sec:{:.2f}".format(pos, tmp))  # formatで少数点第２まで表示
        ed = milli()
        sleep(fps)


if __name__ == '__main__':
    fps = 1 / 30
    pos = -10
    x = 10
    speed = 4
    delay(pos, x, speed, fps)
