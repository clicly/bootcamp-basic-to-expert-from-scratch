# Lo básico con operaciones matemáticas

def add(x, y): return x + y


print(add(120, 34))  # 154
print(add(100, 34))  # 134
print(add(90, 34))  # 124
print(add(1, 34))   # 35


def substraction(x, y): return x - y


print(substraction(120, 34))  # 86
print(substraction(100, 34))  # 66
print(substraction(90, 34))  # 56
print(substraction(1, 34))   # -33


def multiplication(x, y): return x * y


print(multiplication(1, 2))     # 2
print(multiplication(4, 5))     # 20
print(multiplication(-3, 10))   # -30
print(multiplication(-3, -11))  # 33


def division(x, y): return x / y


print(division(10, 4))  # 2.5
print(division(20, 4))  # 5


def rest(x, y): return x % y


print(rest(4, 2))  # 0
print(rest(4, 3))  # 1


def exponential(x, y): return x ** y


print(exponential(4, 2))  # 16
print(exponential(4, 4))  # 256


# Argumentos determinados / indeterminados

# Sin argumentos

def x(): return 456


print(x())  # 456

# Argumentos y con valores por defecto


def acumulator(x, y=10): return x + y


print(acumulator(34))       # 44
print(acumulator(34, 4))    # 38

# Indeterminados

# Por posición

get_length_pos_params = lambda *args: len(args)

print(get_length_pos_params(1, 2, 3, 4))                   # 4
print(get_length_pos_params(1, 2, 3, 4, 34, 4, 5, 5, 6))   # 9
print(get_length_pos_params(1))                             # 1

get_exist_key_in_params = lambda **kwargs: kwargs.get('name', 'No existe name')

print(get_exist_key_in_params(name='Anartz', lastname='Mugika')) # Anartz
print(get_exist_key_in_params(lastname='Mugika'))               # No existe name

# Por posición / nombre

is_same_length_args_kwargs = lambda *args, **kwargs : len(args) == len(kwargs)

print(is_same_length_args_kwargs(1,2, name='Anartz')) # False
print(is_same_length_args_kwargs(1,2, name='Anartz', lastname='Mugika')) # True

# FUnción anonima dentro de otra función

def divisor (n):
    return lambda a: a / n

two_divisor = divisor(2) # lambda a: a / 2
three_divisor = divisor(3) # lambda a: a / 3
five_divisor = divisor(5) # lambda a: a / 5
ten_divisor = divisor(10) # lambda a: a / 10
twelve_divisor = divisor(20) # lambda a: a / 20

# 2
print("=========2========")
print(two_divisor(134)) # 67
print(two_divisor(4)) # 2
print(two_divisor(90)) # 45

# 3
print("=========3========")
print(three_divisor(39)) # 13
print(three_divisor(9)) # 3
print(three_divisor(7)) # 2.33

# 5
print("=========5========")
print(five_divisor(25)) # 5
print(five_divisor(1)) # 0.2
print(five_divisor(2)) # 0.4

# 10
print("=========10========")
print(ten_divisor(134)) # 13.4
print(ten_divisor(4)) # 0.4
print(ten_divisor(90)) # 9

# 20
print("=========20========")
print(twelve_divisor(134)) # 6.7
print(twelve_divisor(4)) # 0.2
print(twelve_divisor(90)) # 4.5