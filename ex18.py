# Exercise 18 - Buy 8 Get 1 Free

"""
Let's say a coffee shop punches holes into a customer's card each time they buy a coffee.
After the card has eight hole punches, the customer can use the card to get their 9
th cup of coffee for free.

In this exercise,we will translate this into a simple calculation to see how much a given
quantity of coffees costs while considering this buy-8-get-1-free system.
"""


def get_cost_of_coffee(number_of_coffees: int, price_per_coffee: float | int) -> float | int:
    """
    Calculates how much a given quantity of coffees costs while considering the buy-8-get-1-free system.
    ___________
    Parameters:
        number_of_coffees : int
            Number of coffees ordered.
        price_per_coffee : float | int
            Price of a single coffee.
    ___________
    Returns:
        out : float | int
            The total cost of the coffee order.
    """

    if number_of_coffees == 0:
        return 0

    number_of_free_coffees = number_of_coffees // 9

    return (number_of_coffees - number_of_free_coffees) * price_per_coffee


assert get_cost_of_coffee(7, 2.50) == 17.50
assert get_cost_of_coffee(8, 2.50) == 20
assert get_cost_of_coffee(9, 2.50) == 20
assert get_cost_of_coffee(10, 2.50) == 22.50

for i in range(1, 4):
    assert get_cost_of_coffee(0, i) == 0
    assert get_cost_of_coffee(8, i) == 8 * i
    assert get_cost_of_coffee(9, i) == 8 * i
    assert get_cost_of_coffee(18, i) == 16 * i
    assert get_cost_of_coffee(19, i) == 17 * i
    assert get_cost_of_coffee(30, i) == 27 * i
