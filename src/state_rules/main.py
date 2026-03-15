class types:
    state_keys = int | str
    state = dict # can it be something else? just need mapping and iter
    from typing import Callable
    argmap = dict[state_keys, state_keys | Callable ]  # callable[state keys,-> ]

class Rules:

    def __init__(self, state: types.state = {}, log: bool=True):
        self.state = state
        self.funcs = []
        self.log = [] if log is True else False

    def add_func(self, f, argmap: types.argmap | None = None):
        from inspect import signature
        if argmap is None:
            argmap = {p:p for p in signature(f).parameters}
        for s in signature(f).parameters:
            if s not in argmap:
                argmap[s] = s
        
        if 'return' not in argmap:
            argmap['return'] = f'{f.__module__}.{f.__name__}()'#{','.join(v for v in argmap.values())})' doesnt work when v is callable

        f.argmap = argmap
        f._argmap_no_return = {fa:s  for fa,s in f.argmap.items() if (fa != 'return') }
        self.funcs.append(f)


    def register(self, argmap: types.argmap | None = None):
        """decorator on a function"""
        return lambda f: self.add_func(f, argmap=argmap)
    
    @classmethod
    def _argmapf2args(cls, am: types.argmap, state: types.state):
        for fa, s in am.items():
            if callable(s):
                for sk,sv in state.items():
                    ssk = s(sk)
                    if ssk == True:
                        yield fa, sv
                    else: assert(ssk == False)
    
    def __iter__(self):
        state = self.state
        for f in self.funcs:
            _ = {fa:state[s]  for fa,s in f._argmap_no_return.items() if not callable(s) } # simple case
            _.update(self._argmapf2args(f._argmap_no_return, state ) )
            _ = f(**_)
            rm = f.argmap['return']
            if not callable(rm):
                state[rm] = _
            else:
                assert(callable(rm))
                for sk, sv in (state.copy() if self.i == 0 else state ).items():          # have to copy...
                    rmsk = rm(sk)
                    if rmsk == True:
                        state[sk] = _                                                     # ...b/c this might change
                    else: assert(rmsk == False)
        yield state
    
    def run(self, maxiter = 10):
        i = self.i = 0
        from types import SimpleNamespace as NS
        class Iteration(NS): pass

        if self.log is not False:
            self.log.append(Iteration(i=i, state=self.state.copy()))
        
        while True:
            if i >= maxiter: break
            oldstate = self.state.copy()                                    # shallow vs deep?
            _ = iter(self)
            self.state = newstate = next(_)

            if self.log is not False:
                self.log.append(Iteration(i=i+1, state=newstate.copy()))    # shallow vs deep?

            if newstate == oldstate:
                break
            else:
                i = i+1
                newstate = oldstate
                continue
            
        return self.state


