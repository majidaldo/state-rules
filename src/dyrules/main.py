

class unbound(): pass
unbound = unbound()


class Rules:
    def __init__(self, state: dict = {}, funcs: list[callable] = []):
        self.state = state
        self.funcs = funcs

    @property
    def register(self):
        def add_func(f):
            self.funcs.append(f)
        return add_func
    
    

