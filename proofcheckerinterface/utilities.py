def contains(element, statement):
    try:
        return statement.index(element) != -1
    except ValueError as e:
        return False