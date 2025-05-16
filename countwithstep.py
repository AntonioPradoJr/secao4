def count_with_step(start, step):
    startin = start
    def count():
        nonlocal startin
        valor = startin
        startin += step
        return valor
    return count

contador = count_with_step(5,3)

print(contador())
print(contador())
print(contador())
print(contador())