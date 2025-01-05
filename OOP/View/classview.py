# Class untuk menampilkan hasil dalam bentuk tabel
class MahasiswaView:
    @staticmethod
    def tampilkan(mahasiswa_list):
        print("=" * 40)
        print(f"{'Nama':<15}{'NIM':<15}{'Nilai':<10}")
        print("=" * 40)
        for mhs in mahasiswa_list:
            print(f"{mhs.nama:<15}{mhs.nim:<15}{mhs.nilai:<10}")
        print("=" * 40)