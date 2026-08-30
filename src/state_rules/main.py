class types:
    state_key = int | str # hashable?
    state = dict # can it be something else? just need mapping and iter
    var = str
    argmap = dict[var, state_key]


class Rules:

    def __init__(self, state: types.state = {}, *, log: bool=False):
        self.state = state
        self.funcs = []
        self.log = [] if log is True else False

    def add_func(self, f, argmap: types.argmap = {}):
        from inspect import signature
        if not argmap:
            argmap = {p:p for p in signature(f).parameters}
        for s in signature(f).parameters:
            if s not in argmap:
                argmap[s] = s
        if 'return' not in argmap:
            argmap['return'] = f'{f.__module__}.{f.__name__}()'

        from types import SimpleNamespace as NS
        _ = NS(
            f = f,
            argmap = {fa:sk  for fa,sk in argmap.items() if (fa != 'return') },
            return_statekey = argmap['return'],)
        self.funcs.append(_)

    def register(self, argmap: types.argmap = {}):
        def decorator(f):
            self.add_func(f, argmap=argmap)
            return f
        return decorator

    
    def _apply(self, state):
        s = state
        for f in self.funcs:
            _ = {a:s[sk] for a,sk in f.argmap.items() }
            _ = f.f(**_)
            s[f.return_statekey] = _
            yield f, s

    from typing import Callable
    def run(self, maxiter = 10, *, stopping: Callable[[types.state], bool] | None = None):
        i = self.i = 0
        from types import SimpleNamespace as NS
        class Iteration(NS):    pass


        from copy import deepcopy as copy
        if self.log is not False:
            self.log.append(Iteration(i=i, state=copy(self.state)))
        if stopping is not None:
            if stopping(self.state): return self.state

        # shallow vs deep copy?
        while True:
            if i >= maxiter: break
            oldstate = copy(self.state)
            s = self.state
            for f,s in self._apply(self.state):
                if self.log is not False:
                    self.log.append(
                        Iteration(i=i+1,
                            rule=f, 
                            state=copy(s),))
                if stopping is not None:
                    if stopping(s): return s
            self.state = newstate = s

            if newstate == oldstate: # b/c of this, have to copy
                break
            else:
                i = i+1
                newstate = oldstate
                continue
            
        return self.state

