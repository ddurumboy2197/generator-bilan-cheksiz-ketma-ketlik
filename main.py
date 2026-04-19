def kvadrat_sonlar():
    n = 1
    while True:
        yield n ** 2
        n += 1

kvadrat_sonlar_generator = kvadrat_sonlar()

for _ in range(10):
    print(next(kvadrat_sonlar_generator))
```

```python
def kvadrat_sonlar():
    n = 1
    while True:
        yield n ** 2
        n += 1

kvadrat_sonlar_generator = kvadrat_sonlar()

for i in range(10):
    print(f"Kvadrat son {i+1}: {next(kvadrat_sonlar_generator)}")
