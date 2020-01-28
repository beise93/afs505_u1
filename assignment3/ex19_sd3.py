def hooch_quantity(kegs_of_beer, barrels_of_wine):
    print(f"There are {kegs_of_beer} kegs of beer.")
    print(f"There are {barrels_of_wine} barrels of wine.")
    print(f"So we have {kegs_of_beer - barrels_of_wine} more kegs of beer than barrels of wine.")
    print("Perhaps we should cut our dissipation.\n")

hooch_quantity(24, 10)

hooch_quantity(10 + 16, 6 * 2)

old_wine = 5
new_wine = 10
kegs_of_beer = 18
hooch_quantity(kegs_of_beer, old_wine + new_wine)

hooch_quantity((kegs_of_beer + 8), (new_wine + 3) + (old_wine -4))

total_containers = hooch_quantity
total_containers(32, 16)

var_stats = (48, 24)
hooch_quantity(*var_stats)

def func_to_func():
    value1 = 48
    value2 = 14
    hooch_quantity(value1, value2)
func_to_func()
