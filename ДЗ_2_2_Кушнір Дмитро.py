from collections import deque

def is_palindrome(input_str):
    # Видаляємо пробіли та робимо всі символи нижнього регістру
    filtered_str = ''.join(ch.lower() for ch in input_str if ch.isalnum())

    # Додаємо символи рядка у deque
    char_deque = deque(filtered_str)

    # Порівнюємо символи на початку і в кінці deque
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

