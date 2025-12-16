# 🧠 Kutu ve Şişe Nesne Tespiti  
## YOLOv8 (CNN) + PyQt5 Masaüstü Uygulaması

## 🖼 Proje Önizlemesi

<img width="1918" height="1018" alt="image" src="https://github.com/user-attachments/assets/da3526ec-dcbf-4e84-889a-30f4e43487c4" />


---

## 🎯 Projenin Amacı

Bu projede, derin öğrenme tabanlı nesne tespiti algoritmalarından YOLOv8 kullanılarak,
gerçek görüntüler üzerinde kutu ve şişe nesnelerinin tespit edilmesi amaçlanmıştır.

Proje kapsamında:
- İki sınıflı (kutu – şişe) özel bir görüntü veri seti oluşturulmuştur
- Görüntüler YOLO formatında etiketlenmiştir
- YOLOv8 modeli Google Colab ortamında eğitilmiştir
- Eğitilen model PyQt5 tabanlı bir masaüstü uygulamasına entegre edilmiştir

Tüm eğitim süreci ve model ayarları ipynb dosyasında açıklamalı şekilde gösterilmiştir.

---

## 1️⃣ Veri Seti Hazırlığı

### Sınıflar

Bu projede iki adet sınıf bulunmaktadır:
- kutu
- sise

### Veri Seti Özellikleri

- Görüntüler tarafımca oluşturulmuştur
- Dosya formatı: jpg
- Etiketleme işlemi LabelImg aracı kullanılarak yapılmıştır
- YOLO formatında .txt etiket dosyaları üretilmiştir

Sınıf indeksleri:
- 0 → kutu
- 1 → sise

### Veri Bölünmesi

Veri seti aşağıdaki şekilde ayrılmıştır:
- Train (Eğitim)
- Val (Doğrulama)

Bu ayrım, modelin genelleme yeteneğini ölçmek amacıyla yapılmıştır.

---

## 2️⃣ YOLO Formatı ve YAML Dosyası

Model eğitimi için data.yaml dosyası oluşturulmuştur.

Bu dosyada:
- Eğitim ve doğrulama veri yolları
- Sınıf sayısı
- Sınıf isimleri

tanımlanmıştır.

Bu yapı, YOLOv8 modelinin veri setini doğru şekilde okuyabilmesi için zorunludur.

---

## 3️⃣ Model Eğitimi (YOLOv8)

### Kullanılan Model

- Model: YOLOv8n (Nano)
- Framework: Ultralytics YOLOv8
- Eğitim ortamı: Google Colab (GPU)

### Eğitim Parametreleri

- Epoch: 50
- Görüntü boyutu: 640x640
- Batch size: 8

Eğitim kodu:

from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="/content/drive/MyDrive/dataset_yolo/data.yaml",
    epochs=50,
    imgsz=640,
    batch=8,
    device=0,
    name="kutu_sise_yolo"
)

### Eğitim Sonuçları

- Eğitim süresince loss değerlerinde düşüş gözlemlenmiştir
- Model, kutu ve şişe nesnelerini başarılı şekilde tespit edebilmiştir
- En iyi performansa sahip model ağırlıkları best.pt dosyası olarak kaydedilmiştir

---

## 4️⃣ PyQt5 Masaüstü Uygulaması

Eğitilen YOLOv8 modeli, PyQt5 kullanılarak geliştirilen bir masaüstü uygulamasına entegre edilmiştir.

### Uygulama Özellikleri

- Görüntü yükleme
- YOLOv8 ile nesne tespiti
- Bounding box çizimi
- Sonuç görüntüsünü kaydetme
- Kullanıcı dostu arayüz

### Kullanıcı Akışı

1. Kullanıcı görüntüyü seçer
2. Test Image butonuna basılır
3. Model görüntüyü analiz eder
4. Tespit edilen nesneler bounding box ile gösterilir

---

## 📁 Proje Dosya Yapısı

YOLO_GUI/
├── gui_app.py
├── Yolo_NesneTespiti.ipynb
├── best.pt
├── README.md

---

## ▶️ Uygulamayı Çalıştırma

Uygulama aşağıdaki komut ile çalıştırılır:

python gui_app.py

---

## 🛠️ Kullanılan Teknolojiler

- Python 3.10
- YOLOv8 (Ultralytics)
- PyTorch
- OpenCV
- PyQt5
- Google Colab (GPU)

---

## 📊 Genel Değerlendirme

Bu projede CNN tabanlı YOLOv8 algoritması kullanılarak iki sınıflı bir nesne tespit sistemi geliştirilmiştir.
Modelin PyQt5 tabanlı bir masaüstü arayüzü ile sunulması, projenin uygulama odaklı ve kullanıcı dostu olmasını sağlamıştır.

---

## 👤 Geliştirici

Nahit Furkan Öznamlı  
Okul No: 2212721020  

