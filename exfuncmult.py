def generator_multi(factor):
    def multiplication(receivable_number):
        final_value = factor * receivable_number
        return final_value
    return multiplication

two = generator_multi(2)
three = generator_multi(3)
four = generator_multi(4)


print(two(10))
print(three(10))
print(four(10))