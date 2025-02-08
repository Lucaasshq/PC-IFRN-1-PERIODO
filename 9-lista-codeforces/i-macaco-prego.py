import sys
input = sys.stdin.read
data = input().strip().split("\n")

test_number = 1
i = 0

while i < len(data):
    N = int(data[i].strip())
    if N == 0:
        break
    
    # Inicializar os limites
    x_inter, y_inter = -10000, 10000
    u_inter, v_inter = 10000, -10000
    
    for j in range(1, N + 1):
        X, Y, U, V = map(int, data[i + j].strip().split())
        x_inter = max(x_inter, X)
        y_inter = min(y_inter, Y)
        u_inter = min(u_inter, U)
        v_inter = max(v_inter, V)
    
    print(f"Teste {test_number}")
    
    if x_inter <= u_inter and v_inter <= y_inter:
        print(f"{x_inter} {y_inter} {u_inter} {v_inter}")
    else:
        print("nenhum")
    
    print("")
    
    test_number += 1
    i += N + 1