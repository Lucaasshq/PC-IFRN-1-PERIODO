
N = int(input())


for _ in range(N):
    C = float(input()) 
    dias = 0
    
   
    while C > 1:
        C /= 2  
        dias += 1 
    

    print(f"{dias} dias")
