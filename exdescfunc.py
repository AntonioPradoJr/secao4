def discount_generation(disc_value):
    def discount_apply(product_value):
        final_value = product_value - (disc_value * product_value)
        return final_value
    return discount_apply

discount10 = discount_generation(0.10)

print(discount10(100))




