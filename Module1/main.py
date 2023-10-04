n = int(input("Enter the end number : ")) 
oddsum = 0 
for i in range(1, n+1): 
  if i % 2 != 0: 
    oddsum += i 
print(" Sum all the odd numbers",oddsum) 
