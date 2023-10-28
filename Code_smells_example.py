#Code Smells Example for long method
def calculate_total_price(items):
    total = 0
    for item in items:
        if item.quantity > 0 and item.price > 100:
                total += item.price * 0.9
            else:
                total += item.price * 0.95
    return total
