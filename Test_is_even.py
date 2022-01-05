"""
Код функции is_even(): 
https://gist.github.com/aleksey-rezvov/9dc0e52479f23772ab3c8ff14be94196. 
Разработайте юнит-тесты проверяющие корректность работы функции. 
Удалось ли найти какие-либо дефекты в этой функции, полагаясь на 
ее назначение исходя из описания? Учтите, что вопрос не на знание 
фреймворков тестирования и их применение, можете взять любой, или 
даже разработать ряд самостоятельных функций.
"""

import unittest

from is_even import is_even

class Test_is_even(unittest.TestCase):
    def setUp(self):
        self.is_even = is_even
    
    # Проверяем на четность
    def test_even(self):
        self.assertEqual(self.is_even(4), True)

    # Проверяем на нечетность
    def test_odd(self):
        self.assertEqual(self.is_even(3), False)

if __name__ == "__main__":
    unittest.main()

"""
В описании функции is_even() сказано, что она возвращает булевый тип 
данных, но по фактку возвращает целочисленный. Для питона это никак 
не сскажется на работе программы, если результаты функции будут
использоваться в булевых функциях. Но тест будет провален, поэтому
лучше всего немного изменить функцию:

def is_even(number):
    ''' Returns True if **number** is even or False if it is odd. '''
    surplus = not(number % 2)
    return bool(surplus)
"""