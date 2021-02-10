def custom_for_loop(func, iterable):

    iterator = iter(iterable)
    results = []
    while True:
        try:
            val = next(iterator)
        except StopIteration:
            break
        else:
            results.append(func(val))
    
    return results

def func(x):
    print("Your value is:", x)


custom_for_loop(func, [10, 20, 30, 40])
