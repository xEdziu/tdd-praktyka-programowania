def Add(value):
    value = value.replace("\n", ",")
    if value == "" :
        return 0
    if value == "," or value == ",," or value[-1] == "," or value[0] == ",":
        raise ValueError
    numbers = map(int, value.split(","))
    return sum(numbers)