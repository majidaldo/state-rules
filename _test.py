import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import state_rules.main as rm
    r = rm.Rules({0:1})
    #
    @r.register({'return': 0, 'x': 0 })
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
