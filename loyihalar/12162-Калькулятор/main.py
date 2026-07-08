def qoshish(birinchi_son, ikkinchi_son):
    """Ikki sonni qo'shadi."""
    return birinchi_son + ikkinchi_son


def ayirish(birinchi_son, ikkinchi_son):
    """Ikkinchi sonni birinchi sondan ayiradi."""
    return birinchi_son - ikkinchi_son


def kopaytirish(birinchi_son, ikkinchi_son):
    """Ikki sonni ko'paytiradi."""
    return birinchi_son * ikkinchi_son


def bolish(birinchi_son, ikkinchi_son):
    """Ikki sonni bo'ladi."""
    if ikkinchi_son == 0:
        return "Xatolik: 0 ga bo'lish mumkin emas!"
    return birinchi_son / ikkinchi_son


amallar = {
    "1": ("Qo'shish", qoshish),
    "2": ("Ayirish", ayirish),
    "3": ("Ko'paytirish", kopaytirish),
    "4": ("Bo'lish", bolish),
}


def menyuni_korsat():
    """Asosiy menyuni chiqaradi."""
    print("\n===== KALKULYATOR =====")
    for kalit, qiymat in amallar.items():
        print(f"{kalit}. {qiymat[0]}")
    print("0. Chiqish")


def son_kiritish(xabar):
    """Foydalanuvchidan son qabul qiladi."""
    while True:
        try:
            return float(input(xabar))
        except ValueError:
            print("Xatolik! Faqat son kiriting.")


def asosiy():
    """Dasturning asosiy qismi."""
    while True:
        menyuni_korsat()

        tanlov = input("Amalni tanlang: ")

        if tanlov == "0":
            print("Dastur yakunlandi.")
            break

        if tanlov not in amallar:
            print("Noto'g'ri tanlov!")
            continue

        birinchi_son = son_kiritish("Birinchi sonni kiriting: ")
        ikkinchi_son = son_kiritish("Ikkinchi sonni kiriting: ")

        natija = amallar[tanlov][1](birinchi_son, ikkinchi_son)

        print(f"Natija: {natija}")


if __name__ == "__main__":
    asosiy()