# Единственный способ вашего взаимодействия с этим кодом - 
# посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое такое лямбда-выражение transformation, чтобы 
# transformed_values получился копией values.


values = [1, 23, 42, 'asdfg']

trasformation = (lambda x: x)

transformed_values = list(map(trasformation, values))

if values == transformed_values:
    print('ok')
else:
    print('fail')
