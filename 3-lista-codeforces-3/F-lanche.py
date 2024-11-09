codigo, quantidade = input().split(" ")
codigo = int(codigo)
quantidade = int(quantidade)

precos = {
  1: 4.00,
  2: 4.50,
  3: 5.00,
  4: 2.00,
  5: 1.50
}

if codigo in precos:
  total = precos[codigo] * quantidade
  print(f"Total: R$ {total:.2f}")
else:
  print("Código inválido")