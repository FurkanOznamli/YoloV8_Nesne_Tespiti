# 🧠 Kutu ve Şişe Nesne Tespiti  
## YOLOv8 (CNN) + PyQt5 Masaüstü Uygulaması

## 🖼 Proje Önizlemesi

(👉 Buraya PyQt5 arayüzünün ekran görüntüsünü ekleyebilirsin)

---

## 🎯 Projenin Amacı

Bu projede, derin öğrenme tabanlı nesne tespiti algoritmalarından **YOLOv8** kullanılarak,
gerçek görüntüler üzerinde **kutu** ve **şişe** nesnelerinin tespit edilmesi amaçlanmıştır.

Proje kapsamında:

1️⃣ İki sınıflı (kutu – şişe) özel bir görüntü veri seti oluşturuldu  
2️⃣ Görüntüler YOLO formatında etiketlendi  
3️⃣ YOLOv8 modeli Google Colab ortamında eğitildi  
4️⃣ Eğitilen model, **PyQt5 tabanlı bir masaüstü arayüzüne** entegre edildi  

Tüm eğitim süreci ve model parametreleri `.ipynb` dosyasında açıklamalı şekilde gösterilmiştir.

---

## 1️⃣ Veri Seti Hazırlığı

📌 **Sınıflar**

Bu projede iki sınıf bulunmaktadır:

- `kutu`
- `sise`

📌 **Veri Seti Özellikleri**

- Görüntüler tarafımca çekilmiştir
- Dosya formatı: `jpg`
- Etiketleme işlemi **LabelImg** aracı kullanılarak yapılmıştır
- YOLO formatında `.txt` etiket dosyaları oluşturulmuştur
- Sınıf indeksleri:
  - `0 → kutu`
  - `1 → sise`

📌 **Veri Bölünmesi**

Veri seti aşağıdaki şekilde ayrılmıştır:

- **Train (Eğitim)**
- **Val (Doğrulama)**

Bu ayrım, modelin ezber yapmadan genelleme yeteneğini ölçmek için yapılmıştır.

---

## 2️⃣ YOLO Formatı ve YAML Dosyası

Model eğitimi için `data.yaml` dosyası oluşturulmuştur.

Bu dosyada:
- Eğitim ve doğrulama veri yolları
- Sınıf sayısı
- Sınıf isimleri

tanımlanmıştır.

Bu yapı, YOLOv8’in veri setini doğru şekilde okuyabilmesi için zorunludur.

---

## 3️⃣ Model Eğitimi (YOLOv8)

📌 **Kullanılan Model**

- Model: **YOLOv8n (Nano)**
- Framework: **Ultralytics YOLOv8**
- Eğitim ortamı: **Google Colab (GPU)**

📌 **Eğitim Parametreleri**

- Epoch: **50**
- Image size: **640 × 640**
- Batch size: **8**

```python
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
📌 Eğitim Sonuçları

Epoch ilerledikçe loss değerlerinde düşüş gözlemlenmiştir

Modelin nesneleri doğru konumlandırabildiği görülmüştür

En iyi performansa sahip ağırlıklar best.pt olarak kaydedilmiştir

(👉 Buraya training grafikleri eklenebilir)

4️⃣ PyQt5 Masaüstü Uygulaması
Eğitilen YOLOv8 modeli, PyQt5 kullanılarak geliştirilen bir GUI uygulamasına entegre edilmiştir.

📌 Uygulama Özellikleri

Görüntü yükleme

YOLOv8 ile nesne tespiti

Bounding box çizimi

Tespit edilen görüntüyü kaydetme

Kullanıcı dostu arayüz

📌 Kullanıcı Akışı

1️⃣ Görsel seçilir
2️⃣ “Test Image” butonu ile model çalıştırılır
3️⃣ Kutu ve şişeler tespit edilir
4️⃣ Sonuç görseli ekranda gösterilir

📁 Proje Dosya Yapısı
bash
Kodu kopyala
YOLO_GUI/
├── gui_app.py               # PyQt5 GUI uygulaması
├── Yolo_NesneTespiti.ipynb  # Model eğitimi (Colab)
├── best.pt                  # Eğitilmiş YOLOv8 modeli
├── README.md                # Proje açıklaması
▶️ Uygulamayı Çalıştırma
Gerekli kütüphaneler kurulduktan sonra aşağıdaki komut ile uygulama çalıştırılabilir:

bash
Kodu kopyala
python gui_app.py
🛠️ Kullanılan Teknolojiler
Python 3.10

YOLOv8 (Ultralytics)

PyTorch

OpenCV

PyQt5

Google Colab (GPU)

📊 Genel Değerlendirme
Bu projede, CNN tabanlı YOLOv8 algoritması kullanılarak iki sınıflı bir nesne tespit sistemi başarıyla geliştirilmiştir.
Modelin PyQt5 tabanlı bir masaüstü arayüzü ile sunulması, projenin uygulama odaklı ve kullanıcı dostu olmasını sağlamıştır.

Proje, hem derin öğrenme hem de yazılım geliştirme süreçlerini birlikte içeren kapsamlı bir çalışmadır.

👤 Geliştirici
Nahit Furkan Öznamlı
