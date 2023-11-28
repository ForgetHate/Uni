if __name__ == "__main__":
    line = ''
    racer = []
    times = []
    count = 0

    while line != "end":
        line = input("> ")
        split = line.split("::")
        if len(split) == 2:
            racer.append(split[0])
            times.append(split[1])
            count += 1
    print(racer)
    print(times)
    print(f'Number of inputs {count}')