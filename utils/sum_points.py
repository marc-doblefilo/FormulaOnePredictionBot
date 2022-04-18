def sum_points(results: list, prediction: list) -> int:
    points: int = 0

    for driver in prediction:
        if driver in results:
            points += 1

    for index, driver in enumerate(prediction):
        if results[index] == driver:
            points += 2

    return points