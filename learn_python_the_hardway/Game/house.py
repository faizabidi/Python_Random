from sys import exit
from textwrap import dedent


# Parent class
class House(object):
    def enter(self):
        print(f"This is just a placeholder enter function.")
        exit(1)


class Targaryen(House):
    def enter(self):
        info = """
            This is house Targaryen. Asnwer this question to proceed in
            this game.
            Question -> Was Daenerys a Targaryen? Answer in "True" or "False"
        """
        print(dedent(info))
        ans = input('answer > ')
        if ans == "True":
            return 'Lannister'
        else:
            return 'GameOver'


class Lannister(House):
    def enter(self):
        info = """
            This is house Lannister. Asnwer this question to proceed
            in this game. Question -> Was Tywin a Lannister? Answer in "True"
            or "False"
        """"

        print(dedent(info))
        ans = input('answer > ')

        if ans == "True":
            return 'Stark'
        else:
            return 'GameOver'


class Stark(House):
    def enter(self):
        info = """
            This is house Stark. Asnwer this question to proceed in
            this game.
            Question -> Was Robert a Stark? Answer in "True" or "False"
        """
        print(dedent(info))
        ans = input('answer > ')
        if ans == "True":
            return 'GameOver'
        else:
            return 'Baratheon'


class Baratheon(House):
    def enter(self):
        info = """
            This is house Baratheon. Asnwer this question to proceed in
            this game.
            Question -> Was Sansa a Baratheon? Answer in "True" or "False"
        """
        print(dedent(info))
        ans = input('answer > ')
        if ans == "True":
            return 'GameOver'
        else:
            return 'Tyrell'


class Tyrell(House):
    def enter(self):
        info = """
            This is house Tyrell. Asnwer this question to proceed in
            this game.
            Question -> Was Olenna a Tyrell? Answer in "True" or "False"
        """
        print(dedent(info))
        ans = input('answer > ')
        if ans == "True":
            return 'GameWon'
        else:
            return 'GameOver'


class GameWon(House):
    def enter(self):
        print("Congrats! You won the game! Bye!")
        exit(1)


class GameOver():
    def enter(self):
        print("You lost the game. Bye!")
        exit(1)
