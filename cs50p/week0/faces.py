# making faces


def convert(text):
    return text.replace(":)", "😄").replace(":(", "😟")


def main():
    print(convert(input()))


main()
