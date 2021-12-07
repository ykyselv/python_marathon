import logging

logging.basicConfig(level='INFO', filename='shipments.log')

class Ship:
    def __init__(self, route, containers):
        #свойства маршрута(list строк)
        self.route = route
        #(list екземпляров класса контейнер)
        self.containers = containers
        self.add_containers(containers)
        logging.info(f"[Ship] initialized: {repr(self)}")

    def add_containers(self, cont_instances):
        for cont in cont_instances:
            if cont.cargo and cont.cargo.destination in self.route:
                self.containers.append(cont)
                logging.info(f'[Ship] Added Container: {cont}')

    def __str__(self):
        text = f'Ship to {self.route} with containers:'
        for cont in self.containers:
            text += '\n' + str(cont)
        return text

    def __repr__(self):
        return f'route={self.route},containers={repr(self.containers)}'


class Container:
    def __init__(self, weight_limit, cargo=None):
        self.weight_limit = weight_limit
        if cargo and cargo.weight <= self.weight_limit:
            self.set_cargo(cargo)
        else:
            self.cargo = None
        logging.info(f'[Container] initialized: Container(weight_limit={self.weight_limit}, cargo={self.cargo}')

    def set_cargo(self, cargo2):
        if cargo2.weight <= self.weight_limit:
            self.cargo = cargo2
            logging.info(f'[Container] Cargo set: Cargo to {self.cargo.destination} with weight {self.cargo.weight}')

    def __str__(self):
        return f'Container up to {self.weight_limit} with {self.cargo}'
    def __repr__(self):
        return f'Container(weight_limit = {self.weight_limit}, cargo = destination={self.cargo.destination}, weight={self.cargo.weight}'



class Cargo:
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight
        logging.info(f'[Cargo] initialized: Cargo(destination={self.destination}, weight={self.weight}')
    def __str__(self):
        return f'Cargo to {self.destination} with weight {self.weight}'
    def __repr__(self):
        return f'Cargo(destination={self.destination}, weight={self.weight})'


