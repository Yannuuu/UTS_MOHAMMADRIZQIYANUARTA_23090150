def hitung_BMI(berat, tinggi):
    bmi = berat / (tinggi ** 2)
    return bmi
def interpretasi_bmi(bmi):
    """Fungsi untuk memberikan interpretasi berdasarkan nilai BMI."""
    if bmi < 18.5:
        return "Berat badan kurang"
    elif 18.5 <= bmi < 24.9:
        return "Berat badan normal"
    elif 25 >= bmi < 29.9:
        return "Kelebihan berat badan"
    else:
        return "Obesitas"
    
