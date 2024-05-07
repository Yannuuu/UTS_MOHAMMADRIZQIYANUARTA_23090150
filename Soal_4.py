def operasi():
    while True: 
        a = float(input('Masukan Berat badan '))
        b = float(input('Masukan tinggi badan '))
        hasil = a/(b**2)
        if hasil < 18.5:
         print(f'berat badan = {a}')
         print(f'tinggi badan = {b}')
         print(f'nilai bmi  = {hasil}')
         print('berat badan kurang')
         break
        elif 18.5 <= hasil < 24.9:
          print(f'berat badan = {a}')
          print(f'tinggi badan = {b}')
          print(f'nilai bmi  = {hasil}')
          print('berat badan normal')
          break
        elif 25 <= hasil < 29.9:
          print(f'berat badan = {a}')
          print(f'tinggi badan = {b}')
          print(f'nilai bmi  = {hasil}')
          print('kelebihan berat badan')
          break
        elif  hasil >= 30:
          print(f'berat badan = {a}')
          print(f'tinggi badan = {b}')
          print(f'nilai bmi  = {hasil}')
          print('obesitas')
          break


operasi()
    
