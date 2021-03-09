
def calculate_tree_height(height, age):
    age_power = 1.2 ** int(age)
    future_height = float(height) * age_power
    future_height= round(future_height, 4)
    return future_height




