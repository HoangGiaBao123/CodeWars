def better_than_average(class_points, your_point):
    average_score = sum(class_points) / len(class_points)

    if your_point > average_score:
        return True
    else:
        return False
