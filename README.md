# OpenCVでカメラ画像を取得して処理する
## コード
- rgb.py
  - カラーの変更を行ったカメラ画像処理
  
- gaus.py
  - ガウシアンフィルタをカメラ画像に掛け合わせた処理
```python
    v = cv2.getTrackbarPos('value','title')
    print(v)
    blur = cv2.GaussianBlur(frame, (25, 25), v)
```

トラックバーで分散の値を変えて,その値を受け取り,フィルタで畳み込んでいる.
今回のカメラ画像の画素数が大きいためフィルタサイズを25×25に設定した.

以下のURLは実際に行った動画である.
https://youtu.be/hIfXzRfP4Fg




- gamma.py
  - ガンマ変換をカメラ画像で行う処理

## 実行環境
- python 3.6.5
- opencv 3.4.1
- MacOS 10.13.5
