# Why?

My (author) motivation is to be able to generally describe systems that respond to change.


Related (but not the same):
- reactive programming libraries:
Doesn't focus on a 'state'
- dynamical systems [pathsim](https://docs.pathsim.org/):
This library doesn't, at the face of it, look like it can do what pathsim does, 
but I think sim descriptions could be mapped somehow.

# How?

Rules/functions are repeatedly applied to a 'state' (dict)
until there are no more changes.

```python
import state_rules.main as rm
r = rm.Rules({'x':1})
#
@r.register({'return': 'x', 'x': 'x' })
def f1(x):
    return x+x

r.run(5)
r.log
```
```python
[
Iteration(i=0, state={'x': 1})
Iteration(i=1, state={'x': 2})
Iteration(i=2, state={'x': 4})
Iteration(i=3, state={'x': 8})
Iteration(i=4, state={'x': 16})
Iteration(i=5, state={'x': 32})
]
```

# Tips

- The state is a (flat) dictionary but you can use a fancy dotted dict if you want more structure.
Then, use use a function to get at a key.
- Cache function calls (yourself).
- Use `stopping` critereon to early stop.
