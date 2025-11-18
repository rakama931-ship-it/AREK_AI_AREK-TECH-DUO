# Program Kuis Arek Jatim Cerdas - FESTIKA JATIM 2025
# Dibuat sederhana untuk CLI (Command Line / Terminal)
# AREK TECH DUO

print("============================================")
print("     Selamat Datang di Kuis Arek Jatim!")
print("    Uji pengetahuanmu tentang Jawa Timur")
print("============================================\n")

nama = input("Masukkan nama kamu: ")
print(f"\nHalo {nama}! Siap-siap menjawab ya!\n")
print("Tiap jawaban benar bernilai 20 poin.\n")

score = 0

# Daftar Soal (pertanyaan, pilihan, jawaban)
soal = [
    {
        "tanya": "1. Ibukota Provinsi Jawa Timur adalah?",
        "pilihan": ["a. Surabaya", "b. Malang", "c. Kediri"],
        "jawaban": "a"
    },
    {
        "tanya": "2. Makanan khas Surabaya berikut ini adalah?",
        "pilihan": ["a. Rawon", "b. Soto Lamongan", "c. Pecel Madiun"],
        "jawaban": "a"
    },
    {
        "tanya": "3. Kota yang dikenal sebagai Kota Pendidikan?",
        "pilihan": ["a. Banyuwangi", "b. Malang", "c. Surabaya"],
        "jawaban": "b"
    },
    {
        "tanya": "4. Gunung tertinggi di Jawa Timur?",
        "pilihan": ["a. Arjuno", "b. Semeru", "c. Bromo"],
        "jawaban": "b"
    },
    {
        "tanya": "5. Tari tradisional khas jawa timur?",
        "pilihan": ["a. Tari Remo", "b. Tari piring", "c. Tari Saman"],
        "jawaban": "a"
    }
]

for s in soal:
    print(s["tanya"])
    for p in s["pilihan"]:
        print(p)
    
    jawaban = input("Jawaban kamu (a/b/c): ").lower()

    while jawaban not in ["a", "b", "c"]:
        jawaban = input("Input salah, masukkan a/b/c saja: ").lower()

    if jawaban == s["jawaban"]:
        print("✅ Benar!\n")
        score += 20
    else:
        print(f"❌ Salah! Jawaban benar adalah {s['jawaban']}\n")

print("============================================")
print("Kuis Selesai!")
print(f"Skor akhir kamu: {score}/100")

if score == 100:
    print("Keren! Kamu calon juara Arek Jatim! 💪🔥")
elif score >= 80:
    print("Mantap! Pengetahuanmu tentang Jawa Timur bagus 👍")
else:
    print("Tetep semangat belajar tentang Jawa Timur ya! 🙂")

print("============================================")
