def greetings(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")


def remind_user_name():
    print("Please, remind me your name.")
    user_name = input()
    print(f"What a great name you have, {user_name}!")


def predict_user_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    rem3, rem5, rem7 = int(input()), int(input()), int(input())
    user_age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print(f"Your age is {user_age}; that's a good time to start programming!")


def bot_count():
    print('Now I will prove to you that I can count to any number you want.')
    user_num = input()
    for i in range(int(user_num)+1):
        print(f'{i} !')
        
    print('Completed, have a nice day!')


def test():
    print("Let's test your programming knowledge.")
    print("""Why do we use methods?
    1. To repeat a statement multiple times.
    2. To decompose a program into several small subroutines.
    3. To determine the execution time of a program.
    4. To interrupt the execution of a program.""")

    while 1:
        if input() == "2":
            print("Completed, have a nice day!")
            break
        else:
            print("Please, try again.")

    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greetings('Aid', '2020')  # change it as you need
remind_user_name()
predict_user_age()
bot_count()
test()
end()