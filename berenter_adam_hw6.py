#Assignment: Assignment #6
#Description: Craps!  
#
#Author: Adam Berenter
#WSU ID: 011440727
#Completion Time: Approximately 5 hours
#
#In completing this program, I obtained help or worked with the following: No one
#

#import 'random'
from random import *

#Game intro: Welcome user and find out how much user is willing to lose
def intro():
  print("*" * 20, "Welcome to the game of Simple Craps!", "*" * 20)
  print()
  print("*" * 25, "7's and 11's are winners!", "*" * 26)
  print("*" * 15, "2's, 3's and 12's are donations to the casino!", "*" * 15)
  print()
  print("\t", "You'll find this to be the best place to lose your money!")
  print("\t", "\t", "Tell us how much you'd like to lose...")
  print()
  print()

  #Create starting bankroll
  bank = int(input("How much do you have to gamble? "))

  #Compensate for invalid bank amounts
  if bank <= 0:
      print("Casinos don't allow poor people.")
      game_over()
  else:
    #run game. Seperate from intro to allow coverage for invalid
    #user input in original bankroll
    play_game(bank)
  return
    

#Roll two dice, get random number between 1 and 6 for each
def roll():
  x = randint(1,6)
  y = randint(1,6)
  return x, y

#Create function that uses roll of two 'dice' generated from roll() function
#Include results function
def play_game(bank):

  #Make sure there is money in the bank after replay() is run.
  #Allow option to add to bank.
  if bank == 0:
    add = int(input("You have run out of money. Enter amount you would like to add to your bank: "))

    #If added amount is invalid:
    while add <= 0:
      add = int(input("Enter a positive betting amount: "))
      bank = add
    else:
      bank = add

  #Find out how much the user wants to bet after reminding
  #them of bankroll
  if bank > 0:
      print("You have $", bank, " left in your bank.", sep="")
      bet = int(input("Enter your bet: "))
      if bet > bank or bet <= 0:
        bet = invalid(bet, bank)        

  #Add the dice results and return results to user using results function
  x,y = roll()
  z = x + y
  x = number(x)
  y = number(y)
  print("You rolled a ", x, " and a ", y, " for a result of ", z, ".", sep="")
  results(bank, bet, z)
  
#Include coverage for when bet is invalid (bet more than bank or less than zero)
#This should loop if the user is a rapscallion and continues to enter invalid amounts
def invalid(bet, bank):
  if bet > bank:
    bet = int(input("Enter a bet below bank amount: "))
    if bet > bank or bet <= 0:
      bet = invalid(bet, bank)
        
  if bet <= 0:
    bet = int(input("Enter a positive betting amount: "))
    if bet > bank or bet <= 0:
      bet = invalid(bet, bank)
  return bet


#Create function to turn numerical dice results into literal numbers
def number(x):
  if x == 1:
    x = "one"
  if x == 2:
    x = "two"
  if x == 3:
    x = "three"
  if x == 4:
    x = "four"
  if x == 5:
    x = "five"
  if x == 6:
    x = "six"
  return x

#Create results from dice roll; win (total of 7, 11)
#lose: (total of 2, 3, 12)
#draw: (any other result)
#Include replay function with each result to
#allow player to roll again if they choose
def results(bank, bet, z):
  if z == 7:
    print ("You win! You've gained $", bet, sep="")
    bank = bank + bet
    print ("You have $", bank, " remaining with which to bet.", sep="")
    replay(bank)
  elif z == 11:
    print ("You win! You've gained $", bet, sep="")
    bank = bank + bet
    print ("You have $", bank, " remaining with which to bet.", sep="")
    replay(bank)
  elif z == 2:
    print ("You lose... too bad, so sad.")
    bank = bank - bet
    print ("You have $", bank, " remaining with which to bet.", sep="")
    replay(bank)
  elif z == 3:
    print ("You lose... too bad, so sad.")
    bank = bank - bet
    print ("You have $", bank, " remaining with which to bet.", sep="")
    replay(bank)
  elif z == 12:
    print ("You lose... too bad, so sad.")
    bank = bank - bet
    print ("You have $", bank, " remaining with which to bet.", sep="")
    replay(bank)
  else:
    print ("Push. Boring.")
    print ("You have $", bank, " remaining with which to bet.", sep="")
    replay(bank)

#Function that asks user if they would like to play again
#If yes, run play_game function.
#If no, bid farewell. Tell user bank amount and use game_over function to say bye!
def replay(bank):
  again = input("Play again? (y/n): ")
  if again == "y":
    play_game(bank)
  elif again == "n":
    if bank == 0:
      print()
      print("Thanks for giving your money to the casino.")
      game_over()
    else:
      print()
      print("Congratulations, you left with $", bank, sep = "")
      game_over()

  #For random, invalid responses:
  else:
    print("You have entered an invalid response. Let's try that again...")
    replay(bank)

#End the game with a friendly farewell
def game_over():
  print("\n", "\n", "\t", "*" * 20, "HAVE A NICE DAY", "*" * 20)

#Call the intro function, which will call the play_game function
def main():
  intro()

#Call the main function
main()
