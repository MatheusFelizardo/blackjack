import random
import art
import os
import subprocess

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
start_game = input("Let's start the game? y or n: ")
hands = {'player': [], 'dealer': []}
initialAmountOfCards = 2

def getRandomCard(user):
  hands[user].append(random.choice(cards))

def calculatePoints(user_hand):
  points = 0
  for card in user_hand:
    if (card == 'Jack' or card == 'Queen' or card == 'King'):
      points += 10
      continue
    if card == 'Ace' and 11 + points <= 21:
      points += 11
      continue
    elif card == 'Ace' and 11 + points > 21:
      points += 1
      continue
    points += int(card)

  return points

def checkWinner():
  player_points = calculatePoints(hands['player'])
  dealer_points = calculatePoints(hands['dealer'])

  if dealer_points > 21:
    print(f'You win! You: {player_points} points | Dealer: {dealer_points} points.')
  elif player_points > dealer_points and player_points <= 21:
    print(f'You win! You: {player_points} points | Dealer: {dealer_points} points.')
  elif player_points == dealer_points:
    print(f'You draw! You: {player_points} points | Dealer: {dealer_points} points.')
  else:
    print(f'You loose! You: {player_points} points | Dealer: {dealer_points} points.')

def startGame(): 
  print(f'{art.logo} \n')
  for card in range(initialAmountOfCards):
    getRandomCard('player')
    getRandomCard('dealer')
  print(f"Your's hand: {hands['player']}")
  print(f"Dealer hand's first card: {hands['dealer'][0]}")
  
  dealer_points = calculatePoints(hands['dealer'])
  while dealer_points < 17:
    getRandomCard('dealer')
    dealer_points = calculatePoints(hands['dealer'])
  
  keep_geting = True
  while keep_geting:
    want_get_other_cards = input('Do you want to get another card? y or n: ')
    if want_get_other_cards == 'y':
      getRandomCard('player')
      print(f"Your's hand: {hands['player']}")
      player_points = calculatePoints(hands['player'])
      if player_points > 21:
        keep_geting = False
  
    elif want_get_other_cards == 'n':
      keep_geting = False
    else:
      print('Please select a valid option. Type y for "yes" or n for "no".')
  
  print(f"Dealer's hand: {hands['dealer']}")
  print(f"Your's hand: {hands['player']}")
  checkWinner()

  restart = input('Do you want to start a new game? y or n:')
  if restart == 'y':
    clear()
    hands['player'] = []
    hands['dealer'] = []
    startGame()

if (start_game == 'y'):
  clear()
  startGame()
  
