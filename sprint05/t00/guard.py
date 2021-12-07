class Guard:
    def __init__(self, **kwargs):
        if len(kwargs) > 1:
            self.name = kwargs['name']
            self.salary = kwargs['salary']
        elif len(kwargs) == 1:
            if 'name' in kwargs:
                self.name = kwargs['name']
                self.salary = 0
            elif 'salary' in kwargs:
                self.salary = kwargs['salary']
                self.name = None
        else:
            self.name = None
            self.salary = 0

    def greet(self):
        return (f'Hello, my name is {self.name}!')

    def receive_bribe(self, num):
        if num > self.salary:
            return(f'You may pass.')
        else:
            return('I am not letting you pass.')


# if __name__ == "__main__":
#     print(f'***EXAMPLE 1***')
#     guard = Guard(name='Christopher')
#     print(guard.greet())
#     print(guard.receive_bribe(10))
#     print(f'***EXAMPLE 2***')
#     guard = Guard(salary=100)
#     print(guard.greet())
#     print(guard.receive_bribe(95))
#     print(guard.receive_bribe(105))
#     print(f'***EXAMPLE 3***')
#     guard = Guard(name='Christopher', salary=100)
#     print(guard.greet())
#     print(guard.receive_bribe(80))
#     print(guard.receive_bribe(135))