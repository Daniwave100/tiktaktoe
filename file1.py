import random
def playerMove(choices, a1, a2, a3, b1, b2, b3, c1, c2, c3):
      if ((a1 == "X") and (a2 == "X") and (a3 == "X")):
            print("You win!")
      elif ((b1 == "X") and (b2 == "X") and (b3 == "X")):
            print("You win!")
      elif ((c1 == "X") and (c2 == "X") and (c3 == "X")):
            print("You win!")
      elif ((a1 == "X") and (b1 == "X") and (c1 == "X")):
            print("You win!")
      elif ((a3 == "X") and (b3 == "X") and (c3 == "X")):
            print("You win!")
      elif ((a1 == "X") and (b2 == "X") and (c3 == "X")):
            print("You win!")
      elif ((a1 == "X") and (b2 == "X") and (c3 == "X")):
            print("You win!")

      elif ((a1 == "O") and (a2 == "O") and (a3 == "O")):
            print("You lose!")
      elif ((b1 == "O") and (b2 == "O") and (b3 == "O")):
            print("You lose!")
      elif ((c1 == "O") and (c2 == "O") and (c3 == "O")):
            print("You lose!")
      elif ((a1 == "O") and (b1 == "O") and (c1 == "O")):
            print("You lose!")
      elif ((a3 == "O") and (b3 == "O") and (c3 == "O")):
            print("You lose!")
      elif ((a1 == "O") and (b2 == "O") and (c3 == "O")):
            print("You lose!")
      elif ((a1 == "O") and (b2 == "O") and (c3 == "O")):
            print("You lose!")

      else:
            playerMove = input("Enter a move: ")
            choices.remove(playerMove)
            if playerMove == "a1":
                  a1 = "X"
            elif playerMove == "a2":
                  a2 = "X"
            elif playerMove == "a3":
                  a3 = "X"
            elif playerMove == "b1":
                  b1 = "X"
            elif playerMove == "b2":
                  b2 = "X"
            elif playerMove == "b3":
                  b3 = "X"
            elif playerMove == "c1":
                  c1 = "X"
            elif playerMove == "c2":
                  c2 = "X"
            elif playerMove == "c3":
                  c3 = "X"
            else:
                  print("Error.")

            print(f"  "
                  f"a|b|c\n"
                  f"1 {a1}|{b1}|{c1}\n"
                  f"2 {a2}|{b2}|{c2}\n"
                  f"3 {a3}|{b3}|{c3}\n")

            botMove(choices, a1, a2, a3, b1, b2, b3, c1, c2, c3)

def botMove(choices, a1, a2, a3, b1, b2, b3, c1, c2, c3):
      if ((a1 == "X") and (a2 == "X") and (a3 == "X")):
            print("you win")
      elif ((b1 == "X") and (b2 == "X") and (b3 == "X")):
            print("You win!")
      elif ((c1 == "X") and (c2 == "X") and (c3 == "X")):
            print("You win!")
      elif ((a1 == "X") and (b1 == "X") and (c1 == "X")):
            print("You win!")
      elif ((a3 == "X") and (b3 == "X") and (c3 == "X")):
            print("You win!")
      elif ((a1 == "X") and (b2 == "X") and (c3 == "X")):
            print("You win!")
      elif ((a1 == "X") and (b2 == "X") and (c3 == "X")):
            print("You win!")

      elif ((a1 == "O") and (a2 == "O") and (a3 == "O")):
            print("You lose!")
      elif ((b1 == "O") and (b2 == "O") and (b3 == "O")):
            print("You lose!")
      elif ((c1 == "O") and (c2 == "O") and (c3 == "O")):
            print("You lose!")
      elif ((a1 == "O") and (b1 == "O") and (c1 == "O")):
            print("You lose!")
      elif ((a3 == "O") and (b3 == "O") and (c3 == "O")):
            print("You lose!")
      elif ((a1 == "O") and (b2 == "O") and (c3 == "O")):
            print("You lose!")
      elif ((a1 == "O") and (b2 == "O") and (c3 == "O")):
            print("You lose!")

      else:
            botMoveIndex = random.randint(0, (len(choices) - 1))
            botMove = choices[botMoveIndex]
            choices.remove(botMove)
            if botMove == "a1":
                  a1 = "O"
            elif botMove == "a2":
                  a2 = "O"
            elif botMove == "a3":
                  a3 = "O"
            elif botMove == "b1":
                  b1 = "O"
            elif botMove == "b2":
                  b2 = "O"
            elif botMove == "b3":
                  b3 = "O"
            elif botMove == "c1":
                  c1 = "O"
            elif botMove == "c2":
                  c2 = "O"
            elif botMove == "c3":
                  c3 = "O"
            else:
                  print("Error on botMove")

            print(f"  "
                  f"a|b|c\n"
                  f"1 {a1}|{b1}|{c1}\n"
                  f"2 {a2}|{b2}|{c2}\n"
                  f"3 {a3}|{b3}|{c3}\n")

            playerMove(choices, a1, a2, a3, b1, b2, b3, c1, c2, c3)





def main():

      print("Welcome to Tic Tac Toe!\n")
      print("You will be playing against the computer.")
      print("The program will randomly choose who goes first.")
      print("To choose where you would like to place an X, input the letter column followed by number row. Ex: a2\n")
      begin = input("Enter \"y\" to begin: ")

      while begin != "y":
            begin = input("Command not understood. Enter \"y\" to begin: ")

      a1 = "-"
      a2 = "-"
      a3 = "-"

      b1 = "-"
      b2 = "-"
      b3 = "-"

      c1 = "-"
      c2 = "-"
      c3 = "-"

      print(f"  "
            f"a|b|c\n"
            f"1 {a1}|{b1}|{c1}\n"
            f"2 {a2}|{b2}|{c2}\n"
            f"3 {a3}|{b3}|{c3}\n")

      choices = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]

      firstMove = random.randint(0, 1)

      # while a1 != X and a2 != x and a3 != x etc.
      if firstMove == 0:
            playerMove(choices, a1, a2, a3, b1, b2, b3, c1, c2, c3)

      else:
            botMove(choices, a1, a2, a3, b1, b2, b3, c1, c2, c3)
            # bot move first


main()

x = 1
