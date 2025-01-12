immutable_var = 1,2,3,4,5,6,7,'a','b','c'
print(type(immutable_var))
#immutable_var[0] = 30 # Кортеж или tuple не изменяемый тип данных
print(immutable_var)
mutable_list = [5,20,50,'a','v','d']
mutable_list[1] = 100
print(mutable_list)
print(type(mutable_list))