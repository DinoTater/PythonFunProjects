#Assignment: Assignment #7
#Description: Blackjack!  
#
#Author: Adam Berenter
#WSU ID: 011440727
#Completion Time: Approximately 4 hours
#
#In completing this program, I obtained help or worked with the following: No one
#

#import 'random'
from random import *

#Create list of all cards possible. Use a list of lists to make it easy to seperate number and suit.
def deck():
  spade_card_list = [[2,'spades'],[3,'spades'],[4,'spades'],[5,'spades'],[6,'spades'],[7,'spades'],[8,'spades'],[9,'spades'],[10,'spades'],['Jack','spades'],['Queen','spades'],['King','spades'],['Ace','spades']]
  heart_card_list = [[2,'hearts'],[3,'hearts'],[4,'hearts'],[5,'hearts'],[6,'hearts'],[7,'hearts'],[8,'hearts'],[9,'hearts'],[10,'hearts'],['Jack','hearts'],['Queen','hearts'],['King','hearts'],['Ace','hearts']]
  diamond_card_list = [[2,'diamonds'],[3,'diamonds'],[4,'diamonds'],[5,'diamonds'],[6,'diamonds'],[7,'diamonds'],[8,'diamonds'],[9,'diamonds'],[10,'diamonds'],['Jack','diamonds'],['Queen','diamonds'],['King','diamonds'],['Ace','diamonds']]
  club_card_list = [[2,'clubs'],[3,'clubs'],[4,'clubs'],[5,'clubs'],[6,'clubs'],[7,'clubs'],[8,'clubs'],[9,'clubs'],[10,'clubs'],['Jack','clubs'],['Queen','clubs'],['King','clubs'],['Ace','clubs']]
  card_list = spade_card_list + heart_card_list + diamond_card_list + club_card_list
  return card_list

#Set up game with user-specified number of decks and call get_next_card_value function to begin dealing.
def play_game():
  #Call card_list function to create a list of all cards in one deck
  card_list = deck()

  #Allow for multiple decks to be used. For each deck requested, add to the decks list using FOR loop.
  num_decks = input("With how many decks would you like to play? (Note: The more decks, the longer you can play.) ")
  for i in range(int(num_decks)-1):
    card_list = card_list + card_list

  #Call get_next_card_value function to begin play  
  get_next_card_value(0,card_list)
  

#get randomly generated card value between 2 and 11 for user
def get_next_card_value(score,card_list):

  #Draw a card using the odds function. Announce to the "table"
  number, suit = odds(card_list)
  if number == 8 or number == 'Ace':
    print("You are dealt an ", number, " of ", suit, ".", sep="")
  else:
    print("You are dealt a ", number, " of ", suit, ".", sep="")

  #Apply numerical value to face cards
  if number == 'Jack' or number == 'Queen' or number== 'King':
    number = 10
  elif number == 'Ace':
    number = 11
  number = int(number)

  #Add card amount to score for this round and analyze. If the score is over 21, bust.
  #If score is less than 21, player has option to hit or stand. If stand, call comp_next_card function
  #to deal to the dealer
  score = score + number
  if score > 21:
    print("Your score is ", score, ". Player busts. Player loses.")
    play_again(card_list)
  elif score < 21:
    print("Your score is ", score, ".", sep="")
    hit = input("Would you like to hit <h> or stand <s>?  ")
    if hit == "h":
      get_next_card_value(score,card_list)
    elif hit == 's':
      comp_next_card(score, 0, card_list)
    else:

      #Allow for errant key entry
      while hit != 'h' or hit != 's':
        hit = input("Incorrect entry. Please hit h for hit or s for stand: ")
        if hit == "h":
          get_next_card_value(score,card_list)
        elif hit == 's':
          comp_next_card(score, 0, card_list)
  else:
    print("Your score is ", score, ".", sep="")
    comp_next_card(score, 0, card_list)
  return score

#Deal to the dealer/computer.
def comp_next_card(score, comp_score, card_list):

  #Draw a card using the odds function. Announce to the "table"
  number, suit = odds(card_list)
  if number == 8 or number == 'Ace':
    print("Computer is dealt an ", number, " of ", suit, ".", sep="")
  else:
    print("Computer is dealt a ", number, " of ", suit, ".", sep="")

  #Apply numerical value to face cards
  if number == 'Jack' or number == 'Queen' or number== 'King':
    number = 10
  elif number == 'Ace':
    number = 11
  number = int(number)

  #add card amount to total score for the round
  comp_score = comp_score + number

  #Analyze computer score. If it is less than 17, comp must hit. If it is greater than 21, comp busts. Otherwise, return score
  #so it can be compared in the score_card function
  if comp_score < 17:
    print("Computer's score is ", comp_score, ". Computer must hit.", sep="")
    comp_next_card(score, comp_score,card_list)
  elif comp_score > 21:
    print("The computer's score is ", comp_score, ". Computer busts. Player wins!", sep="")
    play_again(card_list)
  else:
    print("Computer's score is ", comp_score, " and must stay.", sep="")
    score_card(score, comp_score, card_list)
  return comp_score

    
#Odds() function to apply real-life odds to drawing any card in the deck, no matter how many decks,
#using the previously defined card_list from the deck() function
def odds(card_list):

  #Draw random card. Seperate it into number and suit for use in play
  card = card_list[randint(1, len(card_list)-1)]
  number = card[0]
  suit = card[1]
  card_list.remove(card)
  return number, suit
  
#Who won? Compare scores to see who won. Then ask to play again with play_again function
def score_card(score, comp_score, card_list):
  if score > comp_score:
    print("Congratulations! You've beaten the computer ", score, " to ", comp_score, ".", sep="")
    play_again(card_list)
  elif score < comp_score:
    print("Sorry, you've lost, ", score, " to ", comp_score, ".", sep="")
    play_again(card_list)
  else:
    print("There was a push, ", score, " to ", comp_score, ".", sep="")
    play_again(card_list)

#Offer option to play again after winning or losing
#If yes, run starting with play_game()
def play_again(card_list):
  again = input("Would you like to play again (y/n)? ")
  if again == "y":
    get_next_card_value(0,card_list)
  else:
    end_game()
  
#Function to introduce the program
def main():

  #intro
  print("\t", "*" * 3, "Welcome to Simple Blackack", "*" * 3)
  print("\t", " " * 4, "a game by Adam Berenter")
  print()

  #Call play_game() function to get game started
  play_game()

#Function to officially end game
def end_game():
  print("\n", "*" * 6, "Thanks for playing Adam's Blackjack!", "*" * 6)
  return

#Automatically call main() to run program
main()
