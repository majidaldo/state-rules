

class Rules:
    def __init__(self, state: dict = {}, log: bool=True):
        self.state = state
        self.funcs = []
        self.log = [] if log is True else False

    def register(self, argmap: dict[str, str] | None = None):
        """decorator on a function"""
        from inspect import signature
        def add_func(f,  argmap=argmap):
            if argmap is None:
                argmap = {p:p for p in signature(f).parameters}
            for s in signature(f).parameters:
                if s not in argmap:
                    argmap[s] = s
            
            if 'return' not in argmap:
                argmap['return'] = f'{f.__module__}.{f.__name__}({','.join(v for v in argmap.values())})'

            f.argmap = argmap
            f._argmap_no_return = {fa:s  for fa,s in f.argmap.items() if (fa != 'return') }
            self.funcs.append(f)
        return add_func
    
    def __iter__(self):
        state = self.state
        for f in self.funcs:
            _ = {fa:state[s] for fa,s in f._argmap_no_return.items() }
            _ = f(**_)
            state[f.argmap['return']] = _
        yield state
    
    def run(self, maxiter = 10):
        i = 0
        from types import SimpleNamespace as NS
        class Iteration(NS): pass
        
        while True:
            if i >= maxiter: break
            oldstate = self.state.copy() # shallow vs deep?
            _ = iter(self)
            self.state = newstate = next(_)

            if self.log is not False:
                self.log.append(Iteration(i=i, state=newstate))

            if newstate == oldstate:
                break
            else:
                i = i+1
                newstate = oldstate
                continue
            
        return self.state


