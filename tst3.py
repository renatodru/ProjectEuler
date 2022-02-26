longueurchaine = []                                
                                                   
for n in range(1, 10000):                           
    count = 0                                      
    q, r = divmod(1, n)                            
    restes = []                                    
    while r not in restes :                        
        restes.append(r)                           
        q, r = divmod(r*10, n)                     
        count += 1                                 
    print(count)
    longueurchaine.append(count)                   
                                                   
print(longueurchaine.index(max(longueurchaine))+1) 