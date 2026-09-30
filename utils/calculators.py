def cbm(length_cm, width_cm, height_cm, quantity=1):
    return (length_cm * width_cm * height_cm * quantity) / 1_000_000

def profit(revenue, product_cost, shipping_cost=0, other_cost=0):
    value = revenue - product_cost - shipping_cost - other_cost
    margin = (value / revenue * 100) if revenue else 0
    return value, margin
