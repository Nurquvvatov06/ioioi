from datetime import datetime

# Ma'lumotlar bazasi
raqamlar = [
    {"id": 1, "raqam": "AA123BB", "narx": 500, "holat": "sotilmagan"},
    {"id": 2, "raqam": "CC456DD", "narx": 700, "holat": "sotilmagan"},
]

foydalanuvchilar = [
    {"id": 1, "ism": "Ali", "manzil": "Toshkent", "xaridlar": []},
    {"id": 2, "ism": "Laylo", "manzil": "Samarqand", "xaridlar": []},
]

sotuvlar = []

# 1. Raqamni qo'shish
def raqam_qosh():
    id = len(raqamlar) + 1
    raqam = input("Yangi raqamni kiriting: ")
    narx = float(input("Raqam narxini kiriting: "))
    raqamlar.append({"id": id, "raqam": raqam, "narx": narx, "holat": "sotilmagan"})
    print(f"Raqam '{raqam}' tizimga muvaffaqiyatli qo'shildi!")

# 2. Raqamlarni ko'rish
def raqam_royxati():
    print("\nSotilmagan raqamlar ro'yxati:")
    for raqam in raqamlar:
        if raqam["holat"] == "sotilmagan":
            print(f"ID: {raqam['id']}, Raqam: {raqam['raqam']}, Narx: ${raqam['narx']}")
    print("\n")

# 3. Raqamni sotish
def raqamni_sotish():
    raqam_id = int(input("Sotiladigan raqam ID sini kiriting: "))
    foydalanuvchi_id = int(input("Foydalanuvchi ID sini kiriting: "))
    
    raqam = next((r for r in raqamlar if r["id"] == raqam_id and r["holat"] == "sotilmagan"), None)
    foydalanuvchi = next((f for f in foydalanuvchilar if f["id"] == foydalanuvchi_id), None)
    
    if raqam and foydalanuvchi:
        raqam["holat"] = "sotilgan"
        foydalanuvchi["xaridlar"].append(raqam["raqam"])
        sotuvlar.append({
            "id": len(sotuvlar) + 1,
            "raqam": raqam["raqam"],
            "foydalanuvchi_id": foydalanuvchi["id"],
            "sana": datetime.now().strftime("%Y-%m-%d")
        })
        print(f"Raqam '{raqam['raqam']}' foydalanuvchi {foydalanuvchi['ism']} ga sotildi.")
    else:
        print("Xato: Raqam yoki foydalanuvchi topilmadi.")

# 4. Xarid tarixini ko'rish
def xarid_tarixi():
    foydalanuvchi_id = int(input("Foydalanuvchi ID sini kiriting: "))
    foydalanuvchi = next((f for f in foydalanuvchilar if f["id"] == foydalanuvchi_id), None)
    
    if foydalanuvchi:
        print(f"\nFoydalanuvchi '{foydalanuvchi['ism']}' xaridlari:")
        for raqam in foydalanuvchi["xaridlar"]:
            print(f"- {raqam}")
    else:
        print("Xato: Foydalanuvchi topilmadi.")

# Asosiy menyu
def menyu():
    while True:
        print("\nAvtomobil Raqamlari Sotish Dasturi")
        print("1. Yangi raqam qo'shish")
        print("2. Sotilmagan raqamlarni ko'rish")
        print("3. Raqamni sotish")
        print("4. Xarid tarixini ko'rish")
        print("5. Dasturdan chiqish")
        tanlov = input("Tanlovni kiriting (1-5): ")
        
        if tanlov == "1":
            raqam_qosh()
        elif tanlov == "2":
            raqam_royxati()
        elif tanlov == "3":
            raqamni_sotish()
        elif tanlov == "4":
            xarid_tarixi()
        elif tanlov == "5":
            print("Dasturdan chiqilmoqda...")
            break
        else:
            print("Noto'g'ri tanlov, qaytadan urinib ko'ring!")

# Dasturni ishga tushirish
menyu()
