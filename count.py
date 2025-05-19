def criar_contador(inicio=0):
    atual = inicio
    def proximo():
        nonlocal atual
        valor = atual
        atual += 1
        return valor      
    return proximo

contador1 = criar_contador(10)

print(contador1())
print(contador1())
print(contador1())