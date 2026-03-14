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
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
