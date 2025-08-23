actual_price=float(input("please enter the actual amount"))
selling_price=float(input("please enter the selling amount"))                   
if(selling_price  > actual_price):
  profit=selling_price-actual_price
  print("profit made is", profit)
else:
  print("you are at loss")