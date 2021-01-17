print("Day_3 Find the trs")

road = input("Where do you want to go? Left or Right: ").lower()

if road == "left":
  lake = input("You came a lake. Wuold you like yo 'wait' for a boat or 'swim' across: ").lower()
  if lake == "wait":
    door = input("You have arrived a house and there are 3 colors doors to open. Red, Yellow or Blue ?: ").lower()
    if door =="red":
      print("GAME OVER - Burned by fire")
    elif door == "blue":
      print("GAME OVER - Eaten by beasts")
    elif door =="yellow":
      print("You WIN!")
    else:
      print("GAME OVER")
  else:
    print("GAME OVER - Attacked by trout")   
