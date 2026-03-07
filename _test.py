import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import dyrules.main as rm
    r = rm.Rules({'y':3})

    @r.register({'x':'y'})
    def f(x): return 33

    r.do()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
