

class Rules:
    def __init__(self, state: dict = {},):
        self.state = state
        self.funcs = []

    def register(self, argmap: dict[str, str] | None = None):
        """decorator on a function"""
        from inspect import signature
        def add_func(f,  argmap=argmap):
            if argmap is None:
                argmap = {p:p for p in signature(f).parameters}
            
            if 'return' not in argmap:
                argmap['return'] = f'{f.__module__}.{f.__name__}({','.join(v for v in argmap.values())})'

            assert('return' in argmap)
            for p in argmap:
                if p !='return':
                    assert(p in signature(f).parameters)
                    if argmap['return'] != argmap[p]:
                        assert(argmap[p] in self.state )
            f.argmap = argmap
            f._argmap_no_return = {fa:s  for fa,s in f.argmap.items() if s != f.argmap['return'] }
            self.funcs.append(f)
        return add_func
    
    def __iter__(self):
        state = self.state
        for f in self.funcs:
            _ = {fa:state[s] for fa,s in f._argmap_no_return.items() }
            _ = f(**_)
            state[f.argmap['return']] = _
            yield state
    
    def run(self, maxi = 10):
        i = 0
        while True:
            if i >= maxi: break
            oldstate = self.state.copy()
            _ = iter(self)
            self.state = newstate = next(_)
            #print(oldstate, newstate, i)
            if newstate == oldstate:
                print(i, )
                break
            else:
                i = i+1
                newstate = oldstate
                continue
        return self.state


