def getTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    if minutes > 1:
        return "%02d minutes, %02d seconds" % (minutes, seconds)
    else:
        return "%02d minute, %02d seconds" % (minutes, seconds)

if __name__ == "__main__":
    line = ''
    racer = []
    times = []

    while line != "end":
        line = input("> ")
        split = line.split("::")
        if len(split) == 2:
            racer.append(split[0])
            times.append(int(split[1]))

    averageTime = getTime(sum(times) / len(times))
    fastestTime = getTime(min(times))
    slowestTime = getTime(max(times))
    winner = racer[times.index(min(times))]

    print(f'Average Time: {averageTime} \nFastest Time: {fastestTime} \nSlowest Time: {slowestTime} \nWinner: {winner}')
