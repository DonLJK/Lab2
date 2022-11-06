import Lab2Ex6 as L2

def test_find_min_max():
    val2 = [10, 20, 30, 40, 50, 60]
    result = (10,60)
    minmax = L2.find_min_max(val2)
    assert (result==minmax)

def test_calc_average():
    input_arr = [10, 10, 10]
    expected = 10
    avg = L2.calc_average(input_arr)

    assert(avg == expected)

def test_calc_median_temperature():
    input_arr = [1, 2, 3, 4, 5]
    expected = 3
    Median = L2.calc_median_temperature(input_arr)

    assert(Median == expected)