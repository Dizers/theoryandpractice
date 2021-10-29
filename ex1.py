try:
    x = int(input('Введите первое число:'))
    z = int(input('Введите второе число:'))
except ValueError:
    print('Error: Введите ЧИСЛО!!')
    quit()

y = str(input('Введите операцию:'))

if y != '+' and '-' and '*' and '/':
    print ('Error: Используйте только: +, -, *, /')

if y == '+':
    s=x+z
    print(s)
elif y == '-':
    m=x+z
    print(m)
elif y == '*':
    m=x*z
    print(m)
elif y == '/':
    if z == 0:
        print('На ноль делить нельзя!!')
    else:
        d = x / z
        print(d)
