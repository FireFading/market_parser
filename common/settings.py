from random import randint


def timeout():  # seconds
    return randint(a=3, b=10)


max_wait_time = 40  # second
code_expired_time = 1  # minutes
scroll_sleep = 0.2  # seconds


class Keys:
    DELIVERY_KEY = "доставка"
    PRODUCER_KEY = "продавец"
    PRICE_KEY = "₽"
    DISCOUNT_KEY = "%"
    THIN_SPICE = "\u2009"
