# Face-and-Name-Recognition-in-Real-Time

OpenCV ile yüz tanıma

## Proje Nasıl Çalışıyor?
3 betikten oluşan bu projede;
1. betikte yüz taraması yapılıp kişilerin ayrı ayrı yüz fotoğrafları çekilir ve "dataset" klasöründe toplanır.
2. betikte toplanan fotoğraflar ile veri kümemizin eğitimi yapılır.
3. betikte ise yüz tanıması gerçekleşir.

## Kod İçeriği
### 1.Betik:<br/>
•Görüntüleri webcam üzerinden elde edeceğiz. Görüntülerimizin eni 640, yüksekliği 480 piksel olarak tanımlandı.(6 ve 7. satır)<br/>
•Yüz sınıflandırıcısı 8. satırda bulunmaktadır.<br/>
•ID, ad, soyad, tcno kısmından aldığımız veriler ise veritabanına veri ekliyormuş ve çekiyormuş gibi simule etmek amacıyla txt dosyasına kayıt yapmaktadır.<br/>
•While döngüsünde webcam yüzü algılanan kişinin fotoğraflarını çeker ve kayıt yeri ise dataset klasörüdür.<br/>
•While dongüsü içerisindeki *count* değeri ne kadar ise kaydedilen fotoğraf sayısı o kadar olur ve bu değer artıkça eğitim oranı da artar. Yüz tanıma işleminde kesinlik artar.<br/>

### 2.Betik:<br/>
•Veri setinin eğitimi yapılıp bu betik çalıştıktan sonra oluşacak olan *trainer.yml* dosyasına kaydedilir.<br/>

### 3.Betik:<br/>
•Yüz tanıma nesnemiz *recognizer*‘a *trainer.yml* dosyası aracılığıyla eğitilmiş verisetimizi yüklüyoruz.<br/>
•Canlı kamera görüntülerindeki yüzleri de yine haarcascade_frontalface_default.xml filtresi aracılığıyla yakalayacağız. Filtre değişkenimiz faceCascade.<br/>
•Txt dosyasından isin verilerini çekiyoruz.(isimler fotoğraflar ile eşleşiyor)<br/>
•*recognizer.predict()* metodu *id* ve *confidence* değerlerini döndürüyor. id kişi numarası; confidence ise yapılan saptamanın tahmini doğruluk oranıdır.<br/>

### [Orijinal Projenin Reposu](https://github.com/Mjrovai/OpenCV-Face-Recognition)


