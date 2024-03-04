class two_lists:
    def __init__(self):
        self.a: list = []
        self.b: list = []

    def append_a(self, elem):
        self.a.append(elem)

    def append_b(self, elem):
        self.b.append(elem)

    def append(self, elem):
        self.b.append(elem)
        self.a.append(elem)


def main():
    ...


if __name__ == "__main__":
    main()
