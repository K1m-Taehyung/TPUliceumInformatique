import math
def menu5():
    question = ('Какой формулой пользуемся, дружище?')
    print(question)
    print ('1. b определяется как I/(Ht)')
    print ('2. b определяется как log2(K)')
    name =int(input('Введите опцию: \n '))
    if name==1:
        H=int(input ('Вставьте значение для H:  \n '))
        t=int(input ('Вставьте значение для t:  \n '))
        I=int(input ('Вставьте значение для I:  \n '))
        print(I/(H*t))
        print ('Всегда пожалуйста :)')
    elif name==2:
        K=int(input ('Вставьте значение для K:  \n '))
        print (math.log2(K))
        print ('Всегда пожалуйста :)')
    else:
        print('не понимаю :(')

def menu1():
    question = ('в чем вопрос?')
    print(question)
    print ('1. Найти I')
    print ('2. Найти H')
    print ('3. Найти t')
    print ('4. Найти b')
    print ('*Дополнительные параметры могут быть затребованы (например - "K")')
    name =int(input('Введите опцию: \n '))
    if name==1:
        print ('I определяется как H умноженное на t и b')
        H=int(input ('Вставьте значение для H:  \n '))
        t=int(input ('Вставьте значение для t:  \n '))
        b=int(input ('Вставьте значение для b:  \n '))
        print(H*t*b)
        print ('Всегда пожалуйста :)')
    elif name==2:
        print ('H определяется как I/(tb)')
        I=int(input ('Вставьте значение для I:  \n '))
        t=int(input ('Вставьте значение для t:  \n '))
        b=int(input ('Вставьте значение для b:  \n '))
        print(I/(t*b))
        print ('Всегда пожалуйста :) ')
    elif name==3:
        print ('t определяется как I/(Hb)')
        I=int(input ('Вставьте значение для I:  \n '))
        t=int(input ('Вставьте значение для H:  \n '))
        b=int(input ('Вставьте значение для b:  \n '))
        print(I/(H*b))
        print ('Всегда пожалуйста :) ')
    elif name==4:
        menu5()
    else:
        print('не понимаю :(')
    
              
def menu2():
    print ('чего искать будем?')
def menu3():
    print ('спроси меня о чем-нибудь')

question = "каво решаем?"
print(question)
print ('1. решение задачи на кодирование звука')
print ('2. решение задачи на кодирование изображения')
print ('3. решение задачи на кодирвание текстовой информации')
name = int( input('Введи пункт: \n' ))  # считываем строку и кладём её в переменную name
print(f"Пытаемся найти решение задачи номер {name}!")  # форматированный вывод

if name==1:
    menu1()
elif name==2:
    menu2()
elif name==3:
    menu3()
else:
    print ('тычо')
    
