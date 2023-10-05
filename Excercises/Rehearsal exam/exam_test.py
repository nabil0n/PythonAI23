
enkronor = 0
tvakronor = 0
femkronor = 0
tiokronor = 0
tjugolappar = 0
femtiolappar = 0
hundralappar = 0
tvahundralappar = 0
femhundralappar = 0
tusenlappar = 0
def money_counter(n):
    
    if len(str(n)) == 1:
        if int(n) > 5:
            femkronor += 1
            money_counter(int(n)-5)
            
        elif 5 > int(n) >= 2:
            tvakronor += 1
            money_counter(int(n)-2)
        
        elif 2 > int(n) > 0:
            enkronor += 1
            money_counter(int(n)-1)
    
    elif len(str(n)) == 2:
        if int(n) > 49:
            femtiolappar += 1
            money_counter(int(n)-50)
        
        elif 50 > int(n) >= 20:
            tjugolappar += 1
            money_counter(int(n)-20)
        
        elif 20 > int(n) >= 10:
            tiokronor += 1
            money_counter(int(n)-10)
    
    

print(money_counter("69"))