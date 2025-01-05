# Class untuk proses validasi dan input data
from main import Mahasiswa # type: ignore


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

