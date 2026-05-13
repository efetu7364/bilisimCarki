"""
╔═══════════════════════════════════════════════════════════╗
║       BİLİŞİM BİLGİ ÇARKI - Eğlenceli Öğrenme Oyunu      ║
║                                                           ║
║   Bilişim konularında bilgini test etmek için tasarlandı  ║
╚═══════════════════════════════════════════════════════════╝
"""

import random
import time
import winsound
from typing import Dict, List, Tuple

# ANSI Renk Kodları - Renkli çıktı için
class Renkler:
    MAVI = '\033[94m'
    YEŞIL = '\033[92m'
    KIRMIZI = '\033[91m'
    SARI = '\033[93m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    BEYAZ = '\033[97m'
    SIYAH = '\033[90m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# ASCII ART ÇARK TASARIMI - Dönerken gösterilecek çarklar
CARK_FRAMES = [
    """
        ┌─────────────────┐
        │  ⟳  1  2  3  ⟳ │
        │ 12             │
        │                │
        │ 11      🎡      │
        │                │
        │ 10       9      │
        │  ⟲  8  7  6  ⟲ │
        └─────────────────┘
    """,
    """
        ┌─────────────────┐
        │  ⟳  3  4  5  ⟳ │
        │ 2              │
        │                │
        │ 1       🎡      │
        │                │
        │ 12      11      │
        │  ⟲  10 9  8  ⟲ │
        └─────────────────┘
    """,
    """
        ┌─────────────────┐
        │  ⟳  5  6  7  ⟳ │
        │ 4              │
        │                │
        │ 3       🎡      │
        │                │
        │ 2       1      │
        │  ⟲  12 11 10  ⟲ │
        └─────────────────┘
    """,
    """
        ┌─────────────────┐
        │  ⟳  7  8  9  ⟳ │
        │ 6              │
        │                │
        │ 5       🎡      │
        │                │
        │ 4       3      │
        │  ⟲  2  1  12  ⟲ │
        └─────────────────┘
    """,
    """
        ┌─────────────────┐
        │  ⟳  9  10 11 ⟳ │
        │ 8              │
        │                │
        │ 7       🎡      │
        │                │
        │ 6       5      │
        │  ⟲  4  3  2  ⟲ │
        └─────────────────┘
    """,
    """
        ┌─────────────────┐
        │  ⟳  11 12 1  ⟳ │
        │ 10             │
        │                │
        │ 9       🎡      │
        │                │
        │ 8       7      │
        │  ⟲  6  5  4  ⟲ │
        └─────────────────┘
    """,
]

# Bilişim Soruları Veri Tabanı - 9. Sınıf Teknoloji
SORULAR: List[Dict[str, str]] = [
    {
        "soru": "Bilgisayarın temel bileşenlerinden hangisi veri işleme görevini yerine getirir?",
        "cevaplar": ["CPU (İşlemci)", "Ekran", "Fare", "Ses kartı"],
        "dogru": "CPU (İşlemci)",
        "aciklama": "CPU (Merkezi İşlem Birimi), bilgisayarın beyni gibi çalışarak tüm hesaplamaları ve veri işlemlerini yerine getirir!"
    },
    {
        "soru": "İnternete bağlantıyı sağlayan ağ türü hangisidir?",
        "cevaplar": ["LAN (Yerel Ağ)", "PAN (Kişisel Ağ)", "WAN (Geniş Ağ)", "MAN (Metropolitan Ağ)"],
        "dogru": "WAN (Geniş Ağ)",
        "aciklama": "WAN, dünya çapında uzun mesafeleri kapsayan ağlardır. İnternet, WAN'ın en iyi örneğidir!"
    },
    {
        "soru": "Kişisel bilgisayarın (PC) ilk olarak ne zaman yaygınlaştığı kabul edilir?",
        "cevaplar": ["1970'ler", "1980'ler", "1990'lar", "2000'ler"],
        "dogru": "1980'ler",
        "aciklama": "1980'lerin başında, IBM'in PC'si piyasaya çıkmasıyla kişisel bilgisayarlar yaygınlaşmaya başladı!"
    },
    {
        "soru": "Bir dosyanın boyutu genellikle hangi birim ile ölçülür?",
        "cevaplar": ["Saniye", "Megabyte (MB) veya Gigabyte (GB)", "Amper", "Derece"],
        "dogru": "Megabyte (MB) veya Gigabyte (GB)",
        "aciklama": "Dijital dosyaların boyutu byte cinsinden ölçülür. 1 MB = 1024 KB, 1 GB = 1024 MB'dir!"
    },
    {
        "soru": "İnternet bağlantısını kurmak için hangi araç/cihaz kullanılır?",
        "cevaplar": ["Modem", "Yazıcı", "Projeksiyon cihazı", "Tarayıcı"],
        "dogru": "Modem",
        "aciklama": "Modem, bilgisayarınızı İnternet Servis Sağlayıcısı (ISS) aracılığıyla internete bağlar!"
    },
    {
        "soru": "Aşağıdakilerden hangisi bir işletim sistemidir?",
        "cevaplar": ["Windows", "Microsoft Word", "Google Chrome", "Adobe Photoshop"],
        "dogru": "Windows",
        "aciklama": "Windows, Microsoft tarafından geliştirilmiş ve en yaygın kullanılan işletim sistemlerinden biridir!"
    },
    {
        "soru": "Bilgisayarın rasgele erişim belleği (RAM) ne işe yarar?",
        "cevaplar": ["İnternet hızını artırır", "Açık olan programları ve verileri geçici olarak tutar", "Virüs koruyucu işlevi görür", "Ses sistemini kontrolü eder"],
        "dogru": "Açık olan programları ve verileri geçici olarak tutar",
        "aciklama": "RAM, bilgisayarınızın işlem hızını etkileyen geçici bellek türüdür. Bilgisayar kapatıldığında RAM temizlenir!"
    },
    {
        "soru": "Aşağıdakilerden hangisi bir yazılım örneğidir?",
        "cevaplar": ["Klavye", "İşlemci", "Microsoft Office", "Monitör"],
        "dogru": "Microsoft Office",
        "aciklama": "Yazılım, bilgisayarda çalışan programlarıdır. Donanım ise bilgisayarın fiziksel bileşenleridir!"
    },
    {
        "soru": "İnternette bir web sayfasını açmak için hangi yazılım kullanılır?",
        "cevaplar": ["Web tarayıcısı", "Metin editörü", "Çizimleme programı", "Hesap tablosu programı"],
        "dogru": "Web tarayıcısı",
        "aciklama": "Chrome, Firefox, Edge gibi web tarayıcıları internet sayfaları görüntülememizi sağlar!"
    },
    {
        "soru": "E-posta (elektronik posta) gönderirken kullanılan ağ hangisidir?",
        "cevaplar": ["Yerel Ağ (LAN)", "Geniş Ağ (WAN) ve İnternet", "Kişisel Ağ (PAN)", "Metropolitan Ağ (MAN)"],
        "dogru": "Geniş Ağ (WAN) ve İnternet",
        "aciklama": "E-postalar, İnternet üzerinden dünyanın herhangi bir yerine saniyeler içinde gönderilebilir!"
    },
    {
        "soru": "Bilgisayara fiziksel olarak bağlanan cihazlar (fare, klavye, etc.) hangi ada sahiptir?",
        "cevaplar": ["Yazılım", "Donanım", "Ağ", "Platform"],
        "dogru": "Donanım",
        "aciklama": "Donanım (Hardware), bilgisayarın fiziksel bileşenleridir. Yazılım (Software) ise programlardır!"
    },
    {
        "soru": "Bilgisayarda virüs nedir?",
        "cevaplar": ["Hastalık", "Kötü niyetli yazılım", "Ağ hızlandırıcısı", "Oyun programı"],
        "dogru": "Kötü niyetli yazılım",
        "aciklama": "Virüs, bilgisayarınıza zarar vermek amacıyla yazılan kötü niyetli programdır. Antivirüs yazılımı ile korunabilirsiniz!"
    },
    {
        "soru": "Aşağıdakilerden hangisi bir tarama cihazı değildir?",
        "cevaplar": ["Scanner (Tarayıcı)", "Yazıcı", "Kamera", "Mikrofon"],
        "dogru": "Yazıcı",
        "aciklama": "Yazıcı çıkış cihazıdır (bilgiyi kağıda yazdırır). Diğerleri giriş cihazı olarak tarama görevini yapabilir!"
    },
    {
        "soru": "İnternet haberleşmesinde kullanılan IP adresi kaç bölümden oluşur?",
        "cevaplar": ["2 bölüm", "3 bölüm", "4 bölüm", "5 bölüm"],
        "dogru": "4 bölüm",
        "aciklama": "IPv4 adresleri 4 bölümden oluşur (örneğin: 192.168.1.1). Her bölüm 0-255 arasında değer alabilir!"
    },
    {
        "soru": "Bilgisayar ağlarında veri iletiminin temel kurallarına ne denir?",
        "cevaplar": ["Sistem", "Protokol", "Arayüz", "Server"],
        "dogru": "Protokol",
        "aciklama": "Protokoller, ağ üzerinde veri iletişiminin nasıl yapılacağını belirleyen kurallarıdır (örneğin HTTP, TCP/IP)!"
    },
    {
        "soru": "Dijital ortamda güvenliğin en önemli unsuru hangisidir?",
        "cevaplar": ["Hızlı internet", "Güçlü şifre", "Yeni bilgisayar", "Kaliteli monitör"],
        "dogru": "Güçlü şifre",
        "aciklama": "Güçlü bir şifre (harf, sayı, sembol içeren), kişisel verilerinizi korumak için çok önemlidir!"
    },
]


class BilisimCark:
    """Bilişim Bilgi Çarkı Oyun Sınıfı"""
    
    def __init__(self):
        """Oyun başlatma"""
        self.skor = 0
        self.toplam_sorular = 0
        self.oyuncu_adi = ""
    
    def cark_animasyonu_goster(self):
        """Renkli çark animasyonu göster"""
        print(f"\n{Renkler.CYAN}{Renkler.BOLD}")
        print("╔═══════════════════════════════════════════════════════════╗")
        print("║                    ÇARKI DÖNDÜRMEK İÇİN                   ║")
        print("║              HERHANGI BİR TUŞA BASINIZ & ENTER            ║")
        print("╚═══════════════════════════════════════════════════════════╝")
        print(f"{Renkler.RESET}")
        
        # Kullanıcı girdisini bekle
        input(f"{Renkler.SARI}Çarkı döndürmek için ENTER'a bas...{Renkler.RESET}")
        
        # Çark döndürme animasyonu + ses efekti
        self.cark_dondurup_ses_cıkar()
    
    def cark_dondurup_ses_cıkar(self):
        """Çarkı döndür ve gerçekçi tırıltı sesi çıkar"""
        import sys
        
        # Çark döndürme animasyonu - Windows uyumlu versiyon
        toplam_frame = 8  # Toplam frame sayısı
        
        for frame_idx in range(toplam_frame):
            # Çark frame'i göster
            frame = CARK_FRAMES[frame_idx % len(CARK_FRAMES)]
            sys.stdout.write(f"\r{frame}")
            sys.stdout.flush()
            
            # Ses çıkar
            try:
                if frame_idx < 6:
                    winsound.Beep(500 - (frame_idx * 10), 25)
                else:
                    winsound.Beep(350, 35)
            except Exception:
                pass
            
            time.sleep(0.1)
        
        # Final frame'i göster
        sys.stdout.write(f"\r{CARK_FRAMES[0]}\n\n")
        sys.stdout.flush()
        
        # Çark durdu mesajı
        print(f"{Renkler.YEŞIL}✨ ÇARK DURDU! SORUNUZ GELİYOR...{Renkler.RESET}")
        time.sleep(0.3)
    
    def acilis_ekrani(self):
        """Oyun açılış ekranı"""
        print(f"\n{Renkler.MAGENTA}{Renkler.BOLD}")
        print("╔═══════════════════════════════════════════════════════════╗")
        print("║                                                           ║")
        print("║          🎡 BİLİŞİM BİLGİ ÇARKI'NA HOŞ GELDİN! 🎡       ║")
        print("║                                                           ║")
        print("║        Bilişim dünyasında ne kadar bilgili misin?         ║")
        print("║                                                           ║")
        print("╚═══════════════════════════════════════════════════════════╝")
        print(f"{Renkler.RESET}")
        
        # Oyuncu adı al
        self.oyuncu_adi = input(f"{Renkler.SARI}Lütfen adını gir: {Renkler.RESET}").strip() or "Oyuncu"
        print(f"\n{Renkler.YEŞIL}✓ Hoşgeldin, {self.oyuncu_adi}!{Renkler.RESET}\n")
    
    def rastgele_soru_sec(self) -> Dict[str, str]:
        """Rastgele bir soru seç"""
        return random.choice(SORULAR)
    
    def cevap_al(self, cevaplar: List[str]) -> str:
        """Kullanıcıdan cevap al"""
        print(f"\n{Renkler.BOLD}Lütfen cevabını seç (1-4):{Renkler.RESET}")
        
        for i, cevap in enumerate(cevaplar, 1):
            print(f"  {Renkler.CYAN}{i}. {cevap}{Renkler.RESET}")
        
        while True:
            try:
                secim = input(f"\n{Renkler.SARI}Seçimin (1-4): {Renkler.RESET}").strip()
                secim_num = int(secim)
                
                if 1 <= secim_num <= 4:
                    return cevaplar[secim_num - 1]
                else:
                    print(f"{Renkler.KIRMIZI}✗ Lütfen 1-4 arasında bir sayı gir!{Renkler.RESET}")
            except ValueError:
                print(f"{Renkler.KIRMIZI}✗ Geçerli bir sayı gir lütfen!{Renkler.RESET}")
    
    def kontrol_et_ve_geri_bildir(self, kullanici_cevabi: str, dogru_cevap: str, aciklama: str) -> bool:
        """Cevabı kontrol et ve geri bildirim ver"""
        print()
        
        # Cevap kartını karıştır - doğru cevapın konumunu rastgele yap
        if kullanici_cevabi == dogru_cevap:
            print(f"{Renkler.YEŞIL}{Renkler.BOLD}")
            print("╭─────────────────────────────────╮")
            print("│      🎉 DOĞRU CEVAP! 🎉        │")
            print("╰─────────────────────────────────╯")
            print(f"{Renkler.RESET}")
            self.skor += 10
            dogru = True
        else:
            print(f"{Renkler.KIRMIZI}{Renkler.BOLD}")
            print("╭─────────────────────────────────╮")
            print("│     ❌ YANLIŞ CEVAP! ❌         │")
            print("╰─────────────────────────────────╯")
            print(f"{Renkler.RESET}")
            dogru = False
        
        # Açıklamayı göster
        print(f"\n{Renkler.CYAN}💡 Bilgi: {aciklama}{Renkler.RESET}")
        print(f"{Renkler.SARI}Doğru cevap: {dogru_cevap}{Renkler.RESET}\n")
        
        return dogru
    
    def soru_sor(self):
        """Soru sor ve cevabı al"""
        import sys
        
        # Çark animasyonunu göster
        self.cark_animasyonu_goster()
        
        # Rastgele soru seç
        soru_bilgisi = self.rastgele_soru_sec()
        
        # Cevapları karıştır (çark etkisi için)
        cevaplar = soru_bilgisi["cevaplar"].copy()
        random.shuffle(cevaplar)
        
        # Buffer'ı temizle ve soruyu göster
        sys.stdout.flush()
        print(f"\n{Renkler.BOLD}{Renkler.MAVI}")
        print(f"❓ SORU {self.toplam_sorular + 1}: {soru_bilgisi['soru']}")
        print(f"{Renkler.RESET}")
        sys.stdout.flush()
        
        # Cevap al
        kullanici_cevabi = self.cevap_al(cevaplar)
        
        # Kontrol et ve geri bildir
        dogru = self.kontrol_et_ve_geri_bildir(
            kullanici_cevabi,
            soru_bilgisi["dogru"],
            soru_bilgisi["aciklama"]
        )
        
        self.toplam_sorular += 1
        return dogru
    
    def skor_ekrani(self):
        """Skor bilgisini göster"""
        print(f"\n{Renkler.BOLD}{Renkler.SARI}")
        print("╔═══════════════════════════════════════════════════════════╗")
        print(f"║          📊 OYUN BİTTİ - SKOR TABLOSU 📊               ║")
        print("╠═══════════════════════════════════════════════════════════╣")
        print(f"║  Oyuncu: {self.oyuncu_adi:<50} ║")
        print(f"║  Toplam Soru: {self.toplam_sorular:<42} ║")
        print(f"║  Doğru Cevap: {self.skor // 10:<42} ║")
        print(f"║  Başarı Oranı: {(self.skor // 10 / max(self.toplam_sorular, 1) * 100):.1f}%{' ' * 39} ║")
        print(f"║  Toplam Skor: {self.skor:<43} ║")
        
        # Performans değerlendirmesi
        oran = (self.skor // 10 / max(self.toplam_sorular, 1)) * 100
        if oran == 100:
            degerlendirme = "🏆 MÜKEMMEL - BİLİŞİM UZMANI!"
        elif oran >= 80:
            degerlendirme = "⭐ HARIKA - ÇOK İYİ BILGI SAHİBİ!"
        elif oran >= 60:
            degerlendirme = "👍 İYİ - DEVAMEdebilirsin!"
        else:
            degerlendirme = "📚 BAŞLA ÖĞRENMEYE - DAHA ÇALIŞ!"
        
        print(f"║  Değerlendirme: {degerlendirme:<41} ║")
        print("╚═══════════════════════════════════════════════════════════╝")
        print(f"{Renkler.RESET}\n")
    
    def oyna(self):
        """Ana oyun döngüsü"""
        self.acilis_ekrani()
        
        while True:
            # Soru sor
            self.soru_sor()
            
            # Devam etmek isteyip istenmediğini sor
            print(f"{Renkler.BOLD}{Renkler.MAGENTA}")
            devam = input("Bir soru daha oynamak ister misin? (E/H): ").strip().upper()
            print(f"{Renkler.RESET}")
            
            if devam != "E":
                break
        
        # Skor ekranını göster
        self.skor_ekrani()
        
        print(f"{Renkler.YEŞIL}{Renkler.BOLD}Oyun sonu! Bizi ziyaret ettiğin için teşekkürler! 🎓{Renkler.RESET}\n")


def main():
    """Ana program"""
    try:
        oyun = BilisimCark()
        oyun.oyna()
    except KeyboardInterrupt:
        print(f"\n\n{Renkler.KIRMIZI}Oyun iptal edildi. Hoşça kalın!{Renkler.RESET}\n")
    except Exception as e:
        print(f"{Renkler.KIRMIZI}Bir hata oluştu: {e}{Renkler.RESET}")


if __name__ == "__main__":
    main()
