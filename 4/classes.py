class Testclass:

    test_param = 1

    def __init__(self, test_arg) -> None:
        self.test_param = test_arg




a = 1
print(a)

class Int:

    def __init__(self, value) -> None:
        self.value = value

    def get_value(self):
        return self.value
    
    def __repr__(self) -> str:
        return str(self.value)


b = Int(5)
print(b)

print()