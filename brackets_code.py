def solution(S):
  string = S
  stack = []
  # check if the string is empty if so it is a proper nest
  if len(string) == 0:
    return 1
  
  # To loop through each character in the string
  for symbol in string:
    # If the symbol is an 'opening' symbol then add it to the stack
    if symbol == '(' or symbol == '[' or symbol =='{':
      stack.append(symbol)
    else:
      # This condition would be met if the first element of our string was a 'closing' symbol, meaning that the string is not properly nested
      if len(stack) == 0:
        return 0
      # Variable to hold the last 'opening' symbol in the stack.                 
      topOfTheStack = stack[-1]

      # These conditions check the last 'opening' symbol (Which is stored in the 'topOfTheStack' variable) and the current 'closing' symbol.
      # If the two symbols correspond, then we want to remove the top 'opening' symbol from the 'stack'
      if symbol == ')' and topOfTheStack == '(':
        stack.pop()

      elif symbol == ']' and topOfTheStack == '[':
        stack.pop()

      elif symbol == '}' and topOfTheStack == '{':
        stack.pop()
      
      # If the symbols do not correspond, the we have a mismatch in symbols and return a 0
      else:
        return 0
  # If the stack is empty, that means every 'opening' symbol in the stack had a corresponding and matching 'closing' symbol.
  # Which would mean that the string was properly nested, in that case we return a 1.
  if (len(stack) == 0):
    return 1 

  # If the program makes it this far, then we know that the stack is not empty, which means we had a 'opening' & 'closing' symbol mismatch.
  # In which case we return 0   
  return 0

  # This solution has a time complexity of O(n) because we are using a loop to step through each element in the string
