elements = [1,5,6,5,1,2,3]
 
uniqueList = []
duplicate_elements = []
 
for i in elements:
    if i not in uniqueList:
        uniqueList.append(i)
    elif i not in duplicate_elements:
        duplicate_elements.append(i)
 
print(duplicate_elements)