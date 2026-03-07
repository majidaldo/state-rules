import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import dyrules.main as rm
    r = rm.Rules()

    @r.register
    def f(): ...


    r.funcs

    return


if __name__ == "__main__":
    app.run()
