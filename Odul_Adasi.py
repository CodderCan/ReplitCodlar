print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
secim1= input('Bir yol ayrımına geldin. Hangi yolu seçeceksin? "Sağ" veya "Sol" yaz.\n').lower()
if secim1 == "sol":
  secim2= input('Bir göle geldin. Gölün ortasında bir ada var. Bir tekne beklemek için "bekle" yaz. Yüzerek geçmek için "yüz" yaz. \n').lower()
  if secim2 == "bekle":
    secim3= input("Adaya zarar görmeden ulaşırsınız. 3 kapılı bir ev var. Bir kırmızı, bir sarı ve bir mavi. Hangi rengi seçersiniz? \n")
    if secim3== "kırmızı":
      print("Ev yanıyor. Oyun bitti.")
    elif secim3== "sarı":
      print("Hazine sandığı buldunuz. Tebrikler!")
    elif secim3 == "mavi":
      print("Evde canavar var.. Oyun bitti.")
    else:
      print("Var olmayan bir ev sectin. Oyun bitti.")
  else:
      print("Kızgın bir köpekbalığı saldırısına uğruyorsun.. Oyun bitti.")
else:
    print("Bir deliğe düştün. Oyun bitti.")
    
      