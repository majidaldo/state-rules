import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import dyrules.main as rm
    r = rm.Rules({'x':1})
    #
    @r.register({'return': 'x'})
    def f1(x):
        return x+x

    r.run(5)
    r.log
    return (r,)


@app.cell
def _(r):
    r.log[0]
    return


if __name__ == "__main__":
    app.run()
