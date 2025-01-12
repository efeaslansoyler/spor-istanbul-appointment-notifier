# Spor Istanbul Randevu Bildirici

Bu proje, Spor Istanbul'un web sitesindeki seans boşluklarını kontrol eden ve uygun bir seans bulunduğunda kullanıcıları SMS yoluyla bilgilendiren Python tabanlı bir Selenium otomasyon betiğidir. Betik, Linux, Windows ve macOS gibi çeşitli platformlarda çalışabilir ve manuel olarak veya otomatik olarak çalışacak şekilde planlanabilir.

## Özellikler

- Spor Istanbul web sitesine otomatik giriş.
- Dinamik seans kontrolü.
- Twilio üzerinden SMS bildirimi.
- Web sitesi hatalarına karşı yeniden deneme mekanizmaları.
- Birden fazla kullanıcıyı destekler.

## Ön Koşullar

- Python 3.8 veya üzeri
- Firefox tarayıcı ve Geckodriver
- SMS bildirimleri için bir Twilio hesabı

## Kurulum

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/efeaslansoyler/spor-istanbul-appointment-notifier.git
   cd spor-istanbul-appointment-notifier
   ```

2. Sanal ortam oluşturun:
   ```bash
   python3 -m venv venv  # Windows için: python -m venv venv
   source venv/bin/activate  # Windows için: .\venv\Scripts\activate
   ```

3. Gereksinimleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

4. Kullanıcıları yapılandırın:

   - `users_template.json` dosyasını `users.json` olarak kopyalayın.
   - `users.json` dosyasını düzenleyerek kullanıcı adı, şifre ve SMS bildirimleri için telefon numaranızı ekleyin.

## Örnek `users.json`

```json
[
  {
    "kullanici_adi": "kullanici_adiniz",
    "sifre": "sifreniz",
    "telefon_numarasi": "+901234567890"
  }
]
```

**Önemli:** Betiğin çalışması için `users_template.json` dosyasını `users.json` olarak yeniden adlandırmanız ve gerekli bilgileri doldurmanız gerekmektedir.

## Betiği Çalıştırma

### Manuel Olarak

Sanal ortamınızı etkinleştirin ve şu komutu çalıştırın:

```bash
python main.py
```

### Otomatik Olarak

#### Linux'ta (Cron Job)

1. Crontab düzenleyicisini açın:
   ```bash
   crontab -e
   ```

2. Betiği her 12 saatte bir çalıştırmak için aşağıdaki satırı ekleyin:
   ```bash
   0 */12 * * * /venv/yolu/bin/python /projenizin/yolu/main.py >> /projenizin/yolu/logs/cron.log 2>&1
   ```

3. Kaydedip çıkın.

#### Windows'ta (Görev Zamanlayıcı)

1. Görev Zamanlayıcı'yı açın ve yeni bir görev oluşturun.
2. Eylemi, `main.py` dosyasını işaret eden `python.exe` olarak ayarlayın.
3. Görevi her 12 saatte bir çalışacak şekilde planlayın.

#### macOS'ta (Launchd)

1. `~/Library/LaunchAgents/` dizininde bir `.plist` dosyası oluşturun.
2. Betiği her 12 saatte bir çalıştıracak talimatları ekleyin.
3. Plist dosyasını yüklemek için şu komutu kullanın:
   ```bash
   launchctl load ~/Library/LaunchAgents/betik_adiniz.plist
   ```

## Alternatif Barındırma Seçenekleri

- **Yerel Çalıştırma**: Betiği kişisel bilgisayarınızda manuel olarak çalıştırın.
- **Bulut Hizmetleri**: AWS, Google Cloud veya Heroku gibi bulut platformlarına dağıtın.
- **Raspberry Pi**: Betiği sürekli yerel çalıştırma için bir Raspberry Pi'ye kurun.

## Notlar

- `geckodriver`'ın sisteminizin `PATH`'inde olduğundan emin olun.
- Betik çıktısı ve hataları için logları takip edin.