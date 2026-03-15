import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo  as mo
    sd = """
    sequenceDiagram
        participant Alice
        participant Bob
        Bob->>Alice: Hi Alice
        Alice->>Bob: Hi Bob
    """
    mo.mermaid(sd)
    return


app._unparsable_cell(
    r"""
    class Parse:
        def __init__(self, code: str):
            self.code = code
        def lines(self): return self.code.splitlines()

        from dataclasses import dataclass
        @dataclass(frozen=True)
        class Message:
            sender:     str
            message:    str
            receiver:   str

        @property
        def messages(self):
            def _():
                for a in {'->>'}:
                    for l in self.lines():
                        if (':' in l) and (a in l):
                            _, msg = l.split(':')
                            msg = msg.strip()
                            _ = _.split(a)
                            snd, rcv = _
                            snd = snd.strip()
                            rcv = rcv.strip()
                            yield self.Message(snd, msg, rcv)
            return list(_())
        msgs = messages

        @property
        def participants(self):
            _ = frozenset(m.sender      for m in self.msgs)
            _ = frozenset(m.receiver    for m in self.msgs) | _
            return _

    p = Parse(sd)

    import state_rules.main as rm

    state = {p:'' for }

    r = rm.Rules({'x':1})
    """,
    name="_"
)


if __name__ == "__main__":
    app.run()
