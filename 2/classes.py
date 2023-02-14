class MyClass:
    """A simple example class"""

    def __init__(self, num = 0):
        self.i = num

    def f(self):
        print(self.i)
        return 'hello world'


custom_var = MyClass()
new_var = MyClass(1)

custom_var.f()
new_var.f()

custom_var.new_member = 10
print(custom_var.new_member)

