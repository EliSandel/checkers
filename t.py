import soldier

soldier_instance = soldier.Soldier("red")

print(type(soldier_instance))


if isinstance(soldier_instance, soldier.Soldier):
    print(True)