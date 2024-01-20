from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

print("Açık arttırma programına hoşgeldiniz!")
print("Teklif vermeye hazırlanın!")
  

bids={}
bidding_finished=False

def find_highest_bidder(bidding_record):
  highest_bid=0
  winner=""
  for bidder in bidding_record:
    bid_amount=bidding_record[bidder]
    if bid_amount>highest_bid:
      highest_bid=bid_amount
      winner=bidder
  print(f"Kazanan {winner} verdiği teklif ${highest_bid}")

while not bidding_finished:
  name = input("İsminiz?: ")
  price = int(input("Teklifiniz nedir?: $"))
  bids[name] = price
  should_continue = input("Teklif verecek başka katılımcı bulunmaktamıdır? Seçim 'evet' yada 'hayır'.\n")
  if should_continue == "hayır":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "evet":
    clear()

