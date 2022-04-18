from utils.sum_points import sum_points

def test_should_return_0():
    results = ['LEC', 'VER', 'SAI']
    prediction =  ['HAM', 'RUS', 'PER']

    assert 0 == sum_points(results, prediction)

def test_should_return_3():
    results = ['LEC', 'VER', 'SAI']
    prediction =  ['VER', 'SAI', 'LEC']

    assert 3 == sum_points(results, prediction)

def test_should_return_5():
    results = ['LEC', 'VER', 'SAI']
    prediction =  ['VER', 'LEC', 'SAI']

    assert 5 == sum_points(results, prediction)

def test_should_return_9():
    results = ['LEC', 'VER', 'SAI']
    prediction =  ['LEC', 'VER', 'SAI']

    assert 9 == sum_points(results, prediction)