import marimo

__generated_with = "0.24.0"
app = marimo.App()


@app.cell
def _():
    import state_rules.main as rm
    _r = rm.Rules({'x':1}, log=True)
    @_r.register({
        'x': 'x',
         'y': 'x',
        'return': 'x',})
    def f1(x, y,):
        return x+y

    _r.run(5, stopping=lambda s: True)
    _r.log
    return (rm,)


@app.cell
def _(rm):
    # case for 'flexible' argmaps
    from box import Box
    # Instantiate the same ways as a regular dict
    _s = Box({
    'x':{'x': 1},
    'z.y.x' : 3,
    'y': 'yv',
    },
    default_box=True, box_dots=True)
    _s = dict(_s.items(dotted=True))
    _r = rm.Rules(_s, log=True)
    # second argmap
    @_r.register({'x': 'z.y.x', 'return': 'z.y.x.r' })
    # first argmap
    @_r.register({'x': 'x.x', 'return': 'x.x.r' })
    def fd(x): return x+x
    _r.run(5)
    _r.log
    return


if __name__ == "__main__":
    app.run()
