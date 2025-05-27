class PythonChatBot:

    def __init__(self, bot, year):
        self.bot = bot
        self.year = year

    def greet(self):
        print(f"Hello! My name is {self.bot}.")
        print(f"I was created in {self.year}.")

    def remind_name(self):
        print("Please, remind me your name.")
        print(f"What a great name you have, {input()}!")

    def guess_age(self):
        print("Let me guess your age.")
        print("Enter remainders of dividing your age by 3, 5 and 7.")
        age = (int(input()) * 70 + int(input()) * 21 + int(input()) * 15) % 105
        print(f"Your age is {age}; that's a good time to start programming!")

    def count(self):
        print("Now I will prove to you that I can count to any number you want.")
        for i in range(int(input()) + 1):
            print(f"{i}!")

    def test(self):
        print("Let's test your programming knowledge.")
        print("""Why do we use methods?
        1. To repeat a statement multiple times.
        2. To decompose a program into several small subroutines.
        3. To determine the execution time of a program.
        4. To interrupt the execution of a program.""")
        while True:
            if input() == "2":
                print("Completed, have a nice day!")
                break
            else:
                print("Please, try again.")

    def end(self):
        print("Congratulations, have a nice day!")

    def start(self):
        self.greet()
        self.remind_name()
        self.guess_age()
        self.count()
        self.test()
        self.end()


py_bot = PythonChatBot("Aid", "2020")
py_bot.start()