tas = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.(___)
'''

kagit = '''
    _______
---'   ___)___
          ______)
          _______)
         _______)
---.__________)
'''

makas = '''
    _______
---'   ___)___
          ______)
       __________)
      (____)
---.(___)
'''

#Write your code below this line 👇
import random
print("""
Taş kağıt makas oyununa hoş geldiniz. Amacınız vereceğimiz sayıları kullanarak seçim yapmak. Bilgisayar
Rastgele sonuç döndürecek ve yarışacaksınız. 3 olan kazanır""")

my_score = 0
pc_score = 0



while True:
  game_images = [tas, kagit, makas]
  user_choice = int(input("Hangisini seciyorsun? Tas için 0, kagıt için 1 yada makas icin 2 yaz. Çıkmak için '3'ya bas\n"))
  print(game_images[user_choice])

  computer_choice = random.randint(0, 2)
  print("Bilgisayarın secimi:")
  print(game_images[computer_choice])

  if user_choice == 3:
    break
  elif user_choice == 0 and computer_choice == 0:
    my_score += 0
    pc_score += 0
    print(f"Skorun: {my_score}\n pc skoru: {pc_score}")
  elif user_choice == 1 and computer_choice == 0:
    my_score += 1
    print(f"Skorun: {my_score}\n pc skoru: {pc_score}")
  elif user_choice == 0 and computer_choice == 1:
    pc_score += 1
    print(f"Skorun: {my_score}\n pc skoru: {pc_score}")
  elif user_choice == 1 and computer_choice == 1:
    my_score += 0
    pc_score += 0
    print(f"Skorun: {my_score}\n pc skoru: {pc_score}")
  elif user_choice == 2 and computer_choice == 0:
    pc_score += 1
    print(f"Skorun: {my_score}\n pc skoru: {pc_score}")
  elif user_choice == 2 and computer_choice == 1:
    my_score += 1
    print(f"Skorun: {my_score}\n pc skoru: {pc_score}")
  elif user_choice == 2 and computer_choice == 2:
    my_score += 0
    pc_score += 0
    print(f"Skorun: {my_score}\n pc skoru: {pc_score}")
  elif user_choice == 0 and computer_choice == 2:
    my_score += 1
    print(f"Skorun: {my_score}\n pc skoru: {pc_score}")
  elif user_choice == 1 and computer_choice == 2:
    pc_score += 1
    print(f"Skorun: {my_score}\n pc skoru: {pc_score}")
  else:
    print("Gecersiz bir sayı yazdınız, tekrar deneyiniz!", user_choice)

  if pc_score == 3:
    print("Kaybettin")
    break
  if my_score == 3:
    print("Tebrikler, Kazandın!")
    break