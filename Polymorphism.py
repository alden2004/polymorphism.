from abc import ABC, abstractmethod
from typing import List, Union

class AlatElektronik(ABC):
    nama = ""
    daya = 100
    fitur = []

    @abstractmethod
    def aktifkan(self):
        """Metode abstrak untuk mengaktifkan alat"""
        pass

    def hitung_konsumsi_daya(self, jam: int) -> int:
        """Menghitung konsumsi daya berdasarkan jam penggunaan."""
        return self.daya * jam

    def tambah_fitur(self, fitur: Union[str, List[str]] = None):
        """Menambah fitur dengan overloading sederhana."""
        if fitur is None:
            print("Tidak ada fitur tambahan")
            return

        if isinstance(fitur, str):
            self.fitur.append(fitur)
        elif isinstance(fitur, list):
            self.fitur.extend(fitur)

    def __str__(self):
        """Representasi string dari alat elektronik."""
        return f"{self.nama} (Daya: {self.daya}W)"


class Televisi(AlatElektronik):
    nama = "Televisi"
    
    @classmethod
    def create(cls, daya: int = 100, ukuran: str = "32 inch"):
        """Metode untuk membuat instance Televisi."""
        instance = cls
        instance.daya = daya
        instance.ukuran = ukuran
        return instance

    def aktifkan(self):
        """Implementasi metode aktifkan untuk Televisi."""
        print(f"{self.nama} ukuran {self.ukuran} telah dihidupkan.")

    def hitung_konsumsi_daya(self, jam: int) -> int:
        """Override metode hitung_konsumsi_daya."""
        return super().hitung_konsumsi_daya(jam) + (20 * jam)  # Tambahan daya untuk speaker


class Kulkas(AlatElektronik):
    nama = "Kulkas"
    
    @classmethod
    def create(cls, daya: int = 150, tipe: str = "2 Pintu"):
        """Metode untuk membuat instance Kulkas."""
        instance = cls
        instance.daya = daya
        instance.tipe = tipe
        return instance

    def aktifkan(self):
        """Implementasi metode aktifkan untuk Kulkas."""
        print(f"{self.nama} tipe {self.tipe} telah dihidupkan.")


# Demonstrasi Polymorfisme
def operasikan_alat(alat: List[AlatElektronik], jam: int):
    """Fungsi yang menunjukkan polymorfisme."""
    for perangkat in alat:
        print(f"\n--- Mengoperasikan {perangkat.nama} ---")
        perangkat.aktifkan()
        print(f"Fitur: {perangkat.fitur}")
        print(f"Total Konsumsi Daya: {perangkat.hitung_konsumsi_daya(jam)} watt-jam")


# Contoh penggunaan
def main():
    # Membuat berbagai alat elektronik
    tv = Televisi.create()
    kulkas = Kulkas.create()

    # Menambah fitur
    tv.tambah_fitur(["Smart TV", "4K Resolution"])
    kulkas.tambah_fitur(["Ice Maker", "Energy Efficient"])

    # Operasikan alat dengan polymorfisme
    operasikan_alat([tv, kulkas], jam=5)

if __name__ == "__main__":
    main()