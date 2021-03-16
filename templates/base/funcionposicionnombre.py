def super_funcion(*args,**kwargs):
    total=2
    for arg in args:
        total+=arg
        print("sumatoria => ", total)
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])

print(super_funcion(100,20,10,30, trs="Hola a todos", nombre="matias"))