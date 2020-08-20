import random
import string
from words import words


# генерация случайного слова
def valid_word(words):
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    # пользовательский ввод
    while len(word_letters) > 0 and lives > 0:
        # использованные буквы
        print('У вас осталось', lives, 'жизней и вы уже использовали эти буквы: ', ' '.join(used_letters))

        # текущее слово
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Текущее слово: ', ' '.join(word_list))

        user_letter = input('Угадай букву: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1
                print('Буквы', user_letter, 'в слове нет.')

        elif user_letter in used_letters:
            print('Вы уже выбирали эту букву! Попробуйте еще раз. ')
        else:
            print('Неправильно! Попробуйте еще раз. ')

    if lives == 0:
        print('Попытки закончились. Загаданное слово:', word)
    else:
        print('Слово', word, 'отгадано! Поздравляем!')


if __name__ == '__main__':
    hangman()
