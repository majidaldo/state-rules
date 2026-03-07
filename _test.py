import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import dyrules.main as rm
    r = rm.Rules({'x':'x'})
    #
    @r.register({'return': 'x'})
    def f1(x):
        return x

    r.run()
    r.log
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
