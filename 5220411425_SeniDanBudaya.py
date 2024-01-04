from datetime import datetime

class SeniDanBudaya:
    def __init__(self, nama, jenis, tahun_pembuatan):
        self._nama = nama
        self._jenis = jenis
        self._tahun_pembuatan = tahun_pembuatan  # Akses modifier protected

    def get_nama(self):
        return self._nama

    def get_jenis(self):
        return self._jenis

    def get_tahun_pembuatan(self):
        return self._tahun_pembuatan

    def hitung_umur(self):
        tahun_sekarang = datetime.now().year
        return tahun_sekarang - self._tahun_pembuatan

    def deskripsi(self):
        print(f"Sebuah karya seni dan budaya {self._jenis} dengan nama '{self._nama}'.")
        print(f"Tahun Pembuatan: {self._tahun_pembuatan}")
        print(f"Umur: {self.hitung_umur()} tahun\n")

class Lukisan(SeniDanBudaya):
    def __init__(self, nama, teknik, gaya, tahun_pembuatan):
        super().__init__(nama, "Lukisan", tahun_pembuatan)
        self.__teknik = teknik  # Akses modifier private
        self.gaya = gaya

    def get_teknik(self):
        return self.__teknik

    def deskripsi_lukisan(self):
        super().deskripsi()
        print(f"Lukisan '{self._nama}' menggunakan teknik {self.__teknik} dengan gaya {self.gaya}.")

class Tarian(SeniDanBudaya):
    def __init__(self, nama, gerakan, asal, tahun_pembuatan):
        super().__init__(nama, "Tarian", tahun_pembuatan)
        self.gerakan = gerakan
        self.__asal = asal  # Akses modifier private

    def get_asal(self):
        return self.__asal

    def deskripsi_tarian(self):
        super().deskripsi()
        print(f"Tarian '{self._nama}' berasal dari {self.__asal} dengan gerakan khas {self.gerakan}.")
        
class LukisanModern(Lukisan):
    def __init__(self, nama, teknik, gaya, tahun_pembuatan, media, tema):
        super().__init__(nama, teknik, gaya, tahun_pembuatan)
        self.media = media
        self.tema = tema

    def deskripsi_lukisan_modern(self):
        super().deskripsi_lukisan()
        print(f"Medium Lukisan: {self.media}")
        print(f"Tema Lukisan Modern: {self.tema}\n")

# Contoh penggunaan program
def input_lukisan():
    nama = input("Masukkan nama lukisan: ")
    teknik = input("Masukkan teknik lukisan: ")
    gaya = input("Masukkan gaya lukisan: ")
    tahun_pembuatan = int(input("Masukkan tahun pembuatan lukisan: "))
    return Lukisan(nama, teknik, gaya, tahun_pembuatan)

def input_tarian():
    nama = input("Masukkan nama tarian: ")
    gerakan = input("Masukkan gerakan tarian: ")
    asal = input("Masukkan asal tarian: ")
    tahun_pembuatan = int(input("Masukkan tahun pembuatan tarian: "))
    return Tarian(nama, gerakan, asal, tahun_pembuatan)

def input_lukisan_modern():
    lukisan = input_lukisan()
    media = input("Masukkan media lukisan modern: ")
    tema = input("Masukkan tema lukisan modern: ")
    return LukisanModern(lukisan.get_nama(), lukisan.get_teknik(), lukisan.gaya, lukisan.get_tahun_pembuatan(), media, tema)

# Program Utama
if __name__ == "__main__":
    data_lukisan = []
    data_tarian = []
    data_lukisan_modern = []

    while True:
        print("\nMenu:")
        print("1. Input Data Lukisan")
        print("2. Input Data Tarian")
        print("3. Input Data Lukisan Modern")
        print("4. Tampilkan Informasi LUKISAN ")
        print("5. Tampilkan Informasi TARIAN ")
        print("6. Tampilkan Informasi LUKISAN MODERN")
        print("7. Keluar")

        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == "1":
            lukisan = input_lukisan()
            data_lukisan.append(lukisan)
            print("Data Lukisan berhasil diinput.")

        elif pilihan == "2":
            tarian = input_tarian()
            data_tarian.append(tarian)
            print("Data Tarian berhasil diinput.")
        elif pilihan == "3":
            lukisan_modern = input_lukisan_modern()
            data_lukisan_modern.append(lukisan_modern)
            print("Data Lukisan Modern berhasil diinput.")

        elif pilihan == "4":
            for karya_seni in data_lukisan:
                karya_seni.deskripsi()
        elif pilihan == "5":
            for karya_sen in data_tarian:
                karya_sen.deskripsi()
        elif pilihan == "6":
            for karya_seni in data_lukisan_modern:
                karya_seni.deskripsi_lukisan_modern()

        elif pilihan == "7":
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")

