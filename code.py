# 連接雲端硬碟以儲存檔案
from google.colab import drive
drive.mount('/content/gdrive')

#安裝yolo
%%shell
git clone https://github.com/WongKinYiu/yolov7.git
cd yolov7
pip install -r requirements.txt

# 下載資料並解壓縮
!unzip -qq /content/gdrive/MyDrive/dataFaceDetect.zip

#執行程式
%%shell
cd /content/yolov7

python detect.py --img-size 640 --conf 0.25 --source '/content/testhuman.jpg'\
 --weight '/content/gdrive/MyDrive/Colab Notebooks/faceDetect10/weights/best.pt' --save-txt --device 0\
 --name faceDetect_test --project '/content/gdrive/MyDrive/Colab Notebooks'

#繼續訓練
%%shell
cd yolov7

python train.py --workers 1 --batch-size 8 --epochs 100 --img 640 640\
  --data '/content/dataFaceDetect/mydata.yaml' --weights '/content/gdrive/MyDrive/Colab Notebooks/faceDetect10/weights/best.pt' --device 0 --cfg 'cfg/training/yolov7.yaml'\
  --name faceDetect --hyp 'data/hyp.scratch.p5.yaml' --project '/content/gdrive/MyDrive/Colab Notebooks'\
  --resume '/content/gdrive/MyDrive/Colab Notebooks/faceDetect11/weights/last.pt'
