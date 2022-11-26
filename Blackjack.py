нimport random
import os
clear = lambda: os.system('cls')
from art import logo 

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
  
def calculate_score(cards):  
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21: 
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over, you lose."
  elif user_score == computer_score:
    return "It's a draw"
  elif computer_score == 0:
    return "Lose! Opponents has a Blackjack."
  elif user_score == 0:
    return "Win! You have a Blackjack!"
  elif user_score > 21:
    return "You went over! You lose."
  elif computer_score > 21:
    return "Opponent went over! You win!"
  elif user_score > computer_score:
    return "You win!"
  else: 
    return "You lose."

def blackjack():
  user_cards = []
  computer_cards = []
  game_over = False
  
  for i in range(0,2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21: 
      game_over = True
      
    else:
      another_card = input("Type 'y' to get another card, type 'n' to pass:\n")
      while another_card != 'y' and another_card != 'n':
        another_card = input("Please type correct answer - 'y' or 'n':\n")
      if another_card == 'y':
        user_cards.append(deal_card())
      else:
        game_over = True
        
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
        
  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

print(logo)
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  blackjack()

       
