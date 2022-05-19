
class Button():
    def __init__(self, pos: int, key: str):
        self.pos = pos
        self.key = key
        self.pressed = 0


class Keyboard():
    def __init__(self, *args: Button) -> None:
        self.buttons = args

    def press(self, info: int):
        # Takes in a position of the button pressed, and returns that button's output
        try:
            filtered_button = [i for i in self.buttons if i.pos == info][0]

            filtered_button.pressed += 1

            print(filtered_button.key)

        except IndexError:
            print("No button at that position!")

    def typing(self, typing_input: list) -> None:
        # * This isn't the most beautiful solution, but it works.
        try:
            phrase = ""
            for i in typing_input:
                filtered_button = [j for j in self.buttons if j.pos == i][0]
                phrase += filtered_button.key

            print(phrase)

        except IndexError:
            print("No button at that position!")


if __name__ == '__main__':
    b1 = Button(0, 'H')
    b2 = Button(1, 'I')

    keyboard = Keyboard(b1, b2)

    keyboard.press(1)
    keyboard.press(0)

    keyboard.typing([1, 0, 1, 0, 1])

    print(b1.pressed)
    print(b2.pressed)
