def menu1():
    question = ('в чем вопрос?')
    print(question)
    print ('1. Find I')
    print ('2. Find H')
    print ('3. Find t')
    print ('4. Find b')
    name =int(input('Type the option'))
    if name==1:
        print ('I defies as H multiplied by t and b')
        H=int(input ('Put in the following values H  - '))
        t=int(input ('Put in the following values t  - '))
        b=int(input ('Put in the following values b  - '))
        
              
def menu2():
    print ('чего искать будем?')
def menu3():
    print ('спроси меня о чем-нибудь')

question = "каво решаем?"
print(question)
print ('1. решение задачи на кодирование звука')
print ('2. решение задачи на кодирование изображения')
print ('3. решение задачи на кодирвание текстовой информации')
name = int( input('Введи пункт-'))  # считываем строку и кладём её в переменную name
print(f"Пытаемся найти решение задачи номер {name}!")  # форматированный вывод

if name==1:
    menu1()
elif name==2:
    menu2()
elif name==3:
    menu3()
else:
    print ('тычо')
    
