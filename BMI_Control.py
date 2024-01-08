weight = float(input("Kilonuzu giriniz: "))
height = float(input("Boyunuzu giriniz: "))
BMI = weight / (height * height)
if BMI < 18.5:
  print(f"Senin BMI scorun {BMI}, zayıfsın")
elif BMI >= 18.5 and BMI < 25:
  print(f"Senin BMI scorun {BMI}, normal kilodasın")
elif BMI >= 25 and BMI < 30:
  print(f"Senin BMI scorun {BMI}, hafif kilolusun.")
elif BMI >= 30:
  print(f"Senin BMI scorun {BMI}, obezsin.")
else:
  print(f"Senin BMI scorun {BMI}, klinik olarak obezsin.")
  