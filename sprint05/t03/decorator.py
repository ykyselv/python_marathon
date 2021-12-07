import logging

logging.basicConfig(level='INFO', filename='shipments.log')

def log_decor(function_to_decorate):
    def wrapper(*args):
        buff = function_to_decorate(*args)
        logging.info(f"<{type(args[0]).__name__}>: - {function_to_decorate.__name__} method has been called.")
        return buff
    return wrapper

class Ship:
    @log_decor
    def __init__(self, route, containers):
        #свойства маршрута(list строк)
        self.route = route
        #(list екземпляров класса контейнер)
        self.containers = []
        self.add_containers(containers)

    @log_decor
    def add_containers(self, cont_instances):
        for cont in cont_instances:
            if cont.cargo and cont.cargo.destination in self.route:
                self.containers.append(cont)

    @log_decor
    def __str__(self):
        text = f'Ship to {self.route} with containers:'
        for cont in self.containers:
            text += '\n' + str(cont)
        return text

    @log_decor
    def __repr__(self):
        return f'route={self.route},containers={repr(self.containers)}'


class Container:
    @log_decor
    def __init__(self, weight_limit, cargo=None):
        self.weight_limit = weight_limit
        if cargo and cargo.weight <= self.weight_limit:
            self.set_cargo(cargo)
        else:
            self.cargo = None

    @log_decor
    def set_cargo(self, cargo2):
        if cargo2.weight <= self.weight_limit:
            self.cargo = cargo2

    @log_decor
    def __str__(self):
        return f'Container up to {self.weight_limit} with {self.cargo}'

    @log_decor
    def __repr__(self):
        return f'Container(weight_limit = {self.weight_limit}, cargo = {repr(self.cargo)}'

class Cargo:
    @log_decor
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight

    @log_decor
    def __str__(self):
        return f'Cargo to {self.destination} with weight {self.weight}'
    @log_decor
    def __repr__(self):
        return f'Cargo(destination={self.destination}, weight={self.weight})'

