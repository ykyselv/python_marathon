import logging

logging.basicConfig(level='INFO')

def log_decor(function_to_decorate):
    def wrapper(*args, **kwargs):
        logging.info(f"{function_to_decorate.__name__} with {kwargs}")
        return function_to_decorate(*args,**kwargs)
    return wrapper

class Knight:
    instances = []
    i = 1

    @log_decor
    def __new__(cls, *args, **kwargs):
        if cls.i > 4:
            logging.error(f"Cannot create a Knight. The Round Table can only fit 4 Knights.")
        elif kwargs.get('name') == "Arthur":
            logging.error(f"Cannot create a Knight with the name Arthur. Arthur is the King.")
        else:
            for key, value in kwargs.items():
                cls.i += 1
                setattr(cls, key,value)
                return super().__new__(cls)

    @log_decor
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key,value)
        self.instances.append(self)



# if __name__ == '__main__':
#     Knight(name='Robin', title='Not-quite-so-brave-as-Sir-Lancelot',
#     deed='Nearly fought the Dragon of Angnor.')
#     Knight(name='Arthur', age=25)
#     Knight(name='Aban', height=150)
#     Knight(name='Ector', title='Responsible')
#     Knight(name='Galahad')
#     Knight(title='Brave', skill='archery')
#     Knight(name='Tristan')
#     Knight(name='Arthur')
#     for i in Knight.instances:
#         print(i.__dict__)