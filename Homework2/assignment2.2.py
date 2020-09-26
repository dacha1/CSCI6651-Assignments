s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
result = [0] * len(s)
ls = list(s)
print(ls)
for i in range(len(s)):
    result[indices[i]] = ls[i]
print(''.join(result))    




    
    
    
    
        
