# ⚔️ BATTLE TIME ⚔️
import os
import random
import time

def clear():
  os.system('clear')

def wait(seconds):
  time.sleep(seconds)

def rollDice(side):
  result = random.randint(1,side)
  return result

def health():
  healthStat = ((rollDice(6)*rollDice(12))/2)+10
  return healthStat

def strength():
  strengthStat = ((rollDice(6)*rollDice(8))/2)+12
  return strengthStat

def battle():
  clear()
  print("⚔️ BATTLE TIME ⚔️")
  print()
  print("Name your Legend:")
  name = input()
  print()
  print("Character Type (Human, Elf, Wizard, Orc):")
  type = input()
  print()
  print(name)
  health1 = health()
  strength1 = strength()
  print("HEALTH:", health1)
  print("STRENGTH:", strength1)
  print()
  print("Who are they battling?")
  print()
  print("Name your Legend:")
  name2 = input()
  print()
  print("Character Type (Human, Elf, Wizard, Orc):")
  type2 = input()
  print()
  print(name2)
  health2 = health()
  strength2 = strength()
  print("HEALTH:", health2)
  print("STRENGTH:", strength2)
  print()
  print("⚔️ BATTLE TIME ⚔️")
  print()
  print("The battle begins!")
  print()
  counter = 1
  while True:
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    if roll1 > roll2:
      print(name, "wins the first blow")
      print(name2, "takes a hit, with", strength2, "damage")
      print()
      print(name)
      print("HEALTH:", health1)
      print()
      print(name2)
      print("HEALTH:", health2)
      print()
      health2 -= strength1  # Deduct damage from the second character's health
      if health1 <= 0:
        print("Oh no", name, "has died!")
        print()
        print(name2, "destroyed", name, "in", counter, "rounds!")
        break
      elif health2 <= 0:
        print("Oh no", name2, "has died!")
        print()
        print(name, "destroyed", name2, "in", counter, "rounds!")
        break
      else:
        print("And they're both standing for the next round!")
        counter += 1
        wait(2)
        clear()
        continue

    elif roll2 > roll1:
      print(name2, "wins the first blow")
      print(name, "takes a hit, with", strength2, "damage")
      print()
      print(name)
      print("HEALTH:", health1)
      print()
      print(name2)
      print("HEALTH:", health2)
      print()
      health1 -= strength2  # Deduct damage from the first character's health
      if health1 <= 0:
        print("Oh no", name, "has died!")
        print()
        print(name2, "destroyed", name, "in", counter, "rounds!")
        break
      elif health2 <= 0:
        print("Oh no", name2, "has died!")
        print()
        print(name, "destroyed", name2, "in", counter, "rounds!")
        break
      else:
        print("And they're both standing for the next round!")
        counter += 1
        wait(2)
        clear()
        continue

    else:
      print("It's a draw!")
      counter += 1
      wait(2)
      clear()
      continue

battle()
