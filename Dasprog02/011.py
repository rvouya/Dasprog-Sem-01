boiling_point = float(input("Enter the observed boiling point in °C: "))

def within_x_percent(ref, data, x):
    lowerbound = ref - (x / 100) * ref
    upperbound = ref + (x / 100) * ref
    return lowerbound <= data <= upperbound

def identify_substance(boiling_point):
    if within_x_percent(100, boiling_point, 5):
        return "Water"
    elif within_x_percent(357, boiling_point, 5):
        return "Mercury"
    elif within_x_percent(1187, boiling_point, 5):
        return "Copper"
    elif within_x_percent(2193, boiling_point, 5):
        return "Silver"
    elif within_x_percent(2660, boiling_point, 5):
        return "Gold"
    else:
        return "Substance unknown"
    
print(identify_substance(boiling_point))