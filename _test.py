import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import dyrules.main as rm
    r = rm.Rules()
    #
    @r.register({'return': 'y'})
    def f1():
        return 'f1'

    @r.register({ 'return': 'y' })
    def f2():
        return 'f2'


    r.run()
    r.log
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
