
senhaUsuario = 9842
senha = int(input())

while(senha != senhaUsuario):
    print("Senha Invalida!")
    senha = int(input())

    if (senha == senhaUsuario):
        print("Acesso Permitido.")

