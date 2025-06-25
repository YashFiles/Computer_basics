#num = 5
#queen = 1
#black = 11
#white = 11


#def lose_condition():

  # thoughts
''' let's consider a situation where we have a carrom board. So carrom board
      contains coins (white , black , and queen). Let's say we have 11 of white
      and black and a queen. '''

class CoinColor:
  def __init__(self,amount):
    self.amount = amount
  
Black = CoinColor(11)
White = CoinColor(11)
Red = CoinColor(1)

print(Black.amount,White.amount,Red.amount)
#print(Black.amount)

# Program is working now I want to store data.
# In this case I want to store the Coins' color and amount.
#options - array , hashmap , dictionary etc
theCoin = {
    "black" : CoinColor(11),
    "white" : CoinColor(11),
    "red" : CoinColor(1)
}
print(theCoin)

# the basic last step is creating a graphical ui for the program.
# the ui basically takes input from the user and either save data, or show an 
# output.

# in this program let's take input from the user and store the coincolors and 
# their amount

# remembering the gui is not feasible so just use ai
