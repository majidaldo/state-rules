import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import state_rules.main as rm
    r = rm.Rules({'x':1})
    #
    @r.register({'return': 'x', 'x': 'x' })
    def f1(x):
        return x+x

    r.run(5)
    r.log
    return (rm,)


@app.cell
def _(rm):
    from box import Box
    # Instantiate the same ways as a regular dict
    _ = Box({
        'contact': {'email': 'john@example.com', 'x': 1},
        'z.y.x' : 3,
        'y': 'yv',
        #'x': 0
    },
        default_box=True, box_dots=True)

    _ = rm.Rules(dict(_.items(dotted=True)) )
    @_.register({
        'x':        lambda k: k.endswith('.x'),
        'return':   lambda k: k.endswith('.x') ,
          })
    def fd(x): return x+x
    _.run(5)
    _.log
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
