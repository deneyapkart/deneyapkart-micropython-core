# Deneyap Kart MicroPython Core
Güçlü işlemcisi, dayanıklı tasarımı ve esnek giriş/çıkış pinleri ile Türkiye'de tasarlanıp üretilen Deneyap Kart; Elektronik Programlama, Nesnelerin İnterneti (IoT) ve Yapay Zeka alanlarında başlangıç seviyesinden endüstriyel uygulamalara kadar her seviyede proje geliştirilmesine imkan tanır.

Kart hakkında detaylı bilgiye erişmek için, lütfen [Deneyap Kart Teknik Rehberi'ni](https://docs.deneyapkart.org/#deneyap-kart) ve [Deneyap Kart Resmi İnternet Sitesi'ni](https://deneyapkart.org) ziyaret ediniz. 

## İçindekiler
- [Yükleme Talimatları](#yükleme-talimatları)
- [Sorun Giderme](#sorun-giderme)
- [Deneyap Kart Pin Diyagramı](#deneyap-kart-pin-diyagramı)

### Yükleme Talimatları
JSON index dosyası: `https://raw.githubusercontent.com/deneyapkart/deneyapkart-arduino-core/master/package_deneyapkart_index.json`

- [Python 3](https://www.python.org/downloads/)'ü yükleyin.
- Python 3 kurulumundan sonra, Terminal (Komut Satırı) açın ve en son sürüm **esptool** aracını pip3 ile yükleyin:
  `pip3 install esptool`
- En son sürüm [Deneyap Kart MicroPython binary](https://github.com/deneyapkart/deneyapkart-micropython-core/releases/download/1.0.0/deneyapkart_micropython_v1.0.0.bin) dosyasını indirin.
- Deneyap Kart'ın bağlı olduğu Seri Port İsmini (**PORT**) bulun. Bu işlem için Arduino IDE'de **Ayarlar > Port** sekmesine bakabilirsiniz.
- MicroPython binary dosyasını yüklemeden önce, Deneyap Kart'ın belleği aşağıda komumt ile silinmelidir (**PORT** ismini bir üst satırda bulduğunuz isim ile değiştirin):
```python
esptool --chip esp32 --port <PORT> erase_flash
```
- Bellek silme işleminden sonra, Deneyap Kart'a MicroPython binary dosyasını aşağıdaki komut ile yükleyin (**PORT** ve **DIR** yerine ilgili bilgileri yazın):
```python
esptool --chip esp32 --port <PORT> --baud 460800 write_flash -z 0x1000 <DIR (Deneyap Kart MicroPython binary dosya yolu)>
```
- Örnek uygulamalar için [bu dosyayı](https://github.com/deneyapkart/deneyapkart-micropython-core/releases/download/1.0.0/micropython_examples.rar) indirin.

### Sorun Giderme
Herhangi bir hata/sorun bildirmeden önce, lütfen karşılaşılan benzer bir hata/sorun olup olmadığını araştırın. Araştırmanız neticesinde; benzer bir sorunla karşılaşan başka biri olmadığına emin olduğunuz takdirde, [örnek hata bildirme şablonunu](../../.github/ISSUE_TEMPLATE/bug_report_tr.md) kullanarak bildirimde bulunabilirsiniz.  

### Deneyap Kart Pin Diyagramı
![PinoutTR](DeneyapKartPinout_mpv1.0.png)
