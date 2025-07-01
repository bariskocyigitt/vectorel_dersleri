def fonk_yield(xxx):
    for meyve in xxx:
        yield meyve
    
meyveler=["muz","dut","elma"]

output= fonk_yield(meyveler)
print(output)
print(next(output))
print(next(output))