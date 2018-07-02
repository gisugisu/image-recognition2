# OpenCVでカメラ画像を取得して処理する
## コード
- rgb.py
  - カラーの変更を行ったカメラ画像処理
```python
cv2.createTrackbar('R', # name of value
                   'title', # win name
                   0, # min
                   100, # max
                   myfunc) # callback func

cv2.createTrackbar('G', # name of value
                   'title', # win name
                   0, # min
                   100, # max
                   myfunc) # callback func

cv2.createTrackbar('B', # name of value
                   'title', # win name
                   0, # min
                   100, # max
                   myfunc) # callback func
```


```python
R = cv2.getTrackbarPos('R','title') / 100
G = cv2.getTrackbarPos('G','title') / 100
B = cv2.getTrackbarPos('B', 'title') / 100

frame = frame/255
frame[:,:,0]*=B
frame[:,:,1]*=G
frame[:,:,2]*=R

cv2.imshow('title', frame)  # show in the win
```
                   
  
- gaus.py
  - ガウシアンフィルタをカメラ画像に掛け合わせた処理
```python
    v = cv2.getTrackbarPos('value','title')
    print(v)
    blur = cv2.GaussianBlur(frame, (25, 25), v)
```

トラックバーで分散の値を変えて,その値を受け取り,フィルタで畳み込んでいる.
今回のカメラ画像の画素数が大きいためフィルタサイズを25×25に設定した.


参考文献：http://lang.sist.chukyo-u.ac.jp/classes/OpenCV/py_tutorials/py_imgproc/py_filtering/py_filtering.html


以下のURLは実際に行った動画である.
https://youtu.be/hIfXzRfP4Fg




- gamma.py
  - ガンマ変換をカメラ画像で行う処理
  
```python
 v = cv2.getTrackbarPos('value', 'title')*0.5  # of the win
	gamma=v
	print(gamma)
	gamma=gamma+0.001
	look_up_table = np.zeros((256, 1), np.uint8)
	for i in range(256):
		look_up_table[i] = 255 * pow(float(i) / 255, 1.0 / gamma)
		
	frame = cv2.LUT(frame, look_up_table)
```


トラックバーでガンマの値を変えて,その値を受け取っている.
ルックアップテーブルを用いてカメラ画像のそれぞれの輝度値について,トラックバーから受け取ったガンマ値を計算に適応させる.
この時ガンマの値が0の場合,ガンマの値で割ることになるのでガンマ値に0.001という微小な数を足し合わせて0で割ることを避けている.


参考文献：http://peaceandhilightandpython.hatenablog.com/entry/2016/02/05/004445


以下のURLは実際に行った動画である.
https://youtu.be/lnugWyAm7eQ




## 実行環境
- python 3.6.5
- opencv 3.4.1
- MacOS 10.13.5
