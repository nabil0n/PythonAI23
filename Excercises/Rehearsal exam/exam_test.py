def change(n=int):
    
    currency = {
        1000: ["Tusenlapp: ", 0],
        500: ["Femhundralapp: ", 0],
        200: ["Tvåhundralapp: ", 0],
        100: ["Hundralapp: ", 0],
        50: ["Femtiolapp: ", 0],
        20: ["Tjugolapp: ", 0],
        10: ["Tia: ", 0],
        5: ["Femkrona: ", 0],
        2: ["Tvåkrona: ", 0],
        1: ["Enkrona: ", 0],
    }
    
    while n != 0:
        for key, value in currency.items():
            while n - key >= 0:
                n -= key
                currency[key][1] += 1
                #print(f"added 1 to {value}")

    result = []
    for value in currency.values():
        if value[-1] != 0:
            result.append(value)
    return result

print(change(3214))