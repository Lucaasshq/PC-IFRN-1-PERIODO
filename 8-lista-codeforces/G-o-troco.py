T = int(input())  

for _ in range(T):
    D, N = map(int, input().split())  
    precos = list(map(float, input().split())) 

    trocoMaximo = 0.0  

    
    for preco in precos:
       
        quantidade = int(D // preco)  
        troco = D - (quantidade * preco)  
        trocoMaximo = max(trocoMaximo, troco)  

    
    print(f"{trocoMaximo:.2f}")
