def isBalanced(s):
  if len(s) % 2 != 0:
    return 'NO'
  
  stack = []
  closing = ['}', ']', ')']
  pairs = {'}':'{', ']':'[', ')':'('}
  
  for bracket in s:
    if bracket in closing:
      if not stack or stack.pop() != pairs.get(bracket):
        return 'NO'
    else:
      stack.append(bracket)
      
  return 'YES' if not stack else 'NO'