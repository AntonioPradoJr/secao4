def pass_generator(pref):
    prefix = pref
    count = 1
    def new_pass():
        nonlocal prefix
        nonlocal count
        new_pass_concate = prefix + str(count)
        count += 1
        return new_pass_concate
    return new_pass

senha = pass_generator("user_")

print(senha())
print(senha())

