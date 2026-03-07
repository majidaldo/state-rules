import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import dyrules.main as rm
    r = rm.Rules({'x': 3})
    #
    @r.register({'return': 'y'})
    def f(x):
        return 3

    @r.register({'return': 'y' })
    def f2(x):
        return 33

    r.run()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
