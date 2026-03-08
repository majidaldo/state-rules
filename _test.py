import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import dyrules.main as rm
    r = rm.Rules({'x':1})
    #
    @r.register({'return': 'x', 'x': lambda k: (print(k), True )[1] })
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
