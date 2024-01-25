def coke_machine():
  import sys

  print("Welcome to the Coke Machine!")
  price=50
  balance=price

  while True:
    coin = int(input("Insert Coin: ").strip())
    
    match coin:
      case 5|10|25:
        balance -=coin
        if balance > 0:
          print(f"Amount Due: {balance}")
        
        elif balance < 0:
          print(f"Change Owed: {-1*balance}")
          sys.exit()
        else: 
          print(f"Change Owed: {0}")
          sys.exit()
          
      case _:
        print(f"Amount Due: {balance}")


coke_machine()
       
