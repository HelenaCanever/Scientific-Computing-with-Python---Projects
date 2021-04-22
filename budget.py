class Category:
  def __init__(self, category):
    self.category = category
    self.ledger = []


  def deposit(self,amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
    #The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.

  def withdraw(self,amount, description=""):
    if self.check_funds(amount) == True:
      amount = amount*-1
      self.ledger.append({"amount": amount, "description": description})
      return True
    else:
      return False
    #the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.

  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance = balance + item["amount"]
    return balance

    #returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
  def transfer(self, amount, other_cat):
    if self.check_funds(amount) == True:
      other_cat.deposit(amount, "Transfer from " + self.category)
      self.withdraw(amount, "Transfer to " + other_cat.category)
      return True
    else:
      return False

    #add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
  def check_funds(self,amount):
    if self.get_balance() < amount:
      return False
    else:
      return True
    #It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
  def __str__(self):
    header = "*"*(15-(len(self.category))//2) + self.category + "*"*(15-(len(self.category)//2))

    movements = []

    for item in self.ledger:
      movements.append(item["description"][:(30-len(str("{:.2f}".format(item["amount"])))-1)])
      movements.append(" "*(30-len(str("{:.2f}".format(item["amount"])))-len(item["description"][:(30-len(str("{:.2f}".format(item["amount"])))-1)])))
      movements.append(str("{:.2f}".format(item["amount"])))
      movements.append("\n")
    #movements = movements[:-1]
    #formatted_float = "{:.2f}".format(a_float)
    total = "Total: " + str(self.get_balance())

    display = header + "\n" + "".join(movements) + total

    return display

def create_spend_chart(categories=[]):
 #calculate the total withdrawn amount per each category. Then calculate the total withdrawn amount.
  #calculate the percentage over total per each category and round up to 0 decimals.

  values = []
  keys = []
  for category in categories:
    cat_total = 0
    for item in category.ledger:
      if item["amount"] < 0:
        cat_total = cat_total + (item["amount"]*-1)
    values.append(cat_total)
    keys.append(category.category)

    #d[category.category] = d.get(category.category,0) + cat_total


  total_total = 0

  for value in values:
    total_total = total_total + value

  relative_values = []
  for value in values:
    val_rel = (value/total_total)*100
    val_rel = round(val_rel)
    relative_values.append(val_rel)


  #define a header
  header = "Percentage spent by category\n"

  #make a list from 0 to 100 at 10 increments
  #processively make lines
  lines = []
  l = [100,90,80,70,60,50,40,30,20,10,00]

  for n in l:
    if n==100:
      lines.append(""+ str(n) + "|")
      for val_rel in relative_values:
        if val_rel >= n:
          lines.append(" o ")
        else:
          lines.append("   ")
      #lines.append("\n")
    elif n>=10:
      lines.append(" " + str(n) + "|")
      for val_rel in relative_values:
        if val_rel >= n:
          lines.append(" o ")
        else:
          lines.append("   ")
      #lines.append("\n")
    else:
      lines.append("  " + str(n) + "|")
      for val_rel in relative_values:
        if val_rel >= n:
          lines.append(" o ")
        else:
          lines.append("   ")
      #lines.append("\n")
    lines.append(" \n")

  #draw lines at bottom
  #dashes = ""
  dashes = " "*4 + "---"*(len(relative_values))+"-\n"
  # go through category names and print letters
  big_word = 0
  for key in keys:
    if len(key)>big_word:
      big_word = len(key)

  bottom= []
  w = list(range(big_word))

  for n in w:
    bottom.append(" "*5)
    for key in keys:
      try:
        bottom.append(key[n])
        bottom.append("  ")
      except:
        bottom.append("   ")
    bottom.append("\n")
  bottom = bottom[:-1]

  histogram = header + "".join(lines) + dashes + "".join(bottom)



  return histogram
