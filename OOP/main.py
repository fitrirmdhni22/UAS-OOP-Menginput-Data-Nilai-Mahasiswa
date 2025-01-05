# Class untuk menyimpan data mahasiswa
class Mahasiswa:
    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai

# Class untuk proses validasi dan input data
class ProsesInput:
    @staticmethod
    def input_data():
        mahasiswa_list = []
        while True:
            try:
                nama = input("Masukkan Nama Mahasiswa: ")
                nim = input("Masukkan NIM: ")
                nilai = float(input("Masukkan Nilai: "))
                if nilai < 0 or nilai > 100:
                    raise ValueError("Nilai harus antara 0-100.")
                mahasiswa_list.append(Mahasiswa(nama, nim, nilai))
            except ValueError as e:
                print(f"Input tidak valid: {e}")
            
            lanjut = input("Ingin menambahkan mahasiswa lagi? (y/n): ")
            if lanjut.lower() != 'y':
                break
        return mahasiswa_list

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

# Main program
if __name__ == "__main__":
    data_mahasiswa = ProsesInput.input_data()
    print("\nData Mahasiswa:")
    MahasiswaView.tampilkan(data_mahasiswa)