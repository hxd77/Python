#三明治
def make_sandwich(*toppings):
    print("\nMaking a  sandwich with the following toppings:" )
    for topping in toppings:
        print("- "+topping)

make_sandwich("pepperoni")
make_sandwich("pineapple",'apple')
make_sandwich('mushrooms','green peppers','extra cheese')
