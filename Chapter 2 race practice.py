kilometers = 5
minutes = 22
seconds = 47

miles = round((kilometers * 0.62137), 1)
totalSeconds = minutes * 60 + seconds
aveSecondsPerMile = round(totalSeconds / miles)

print(miles, totalSeconds, aveSecondsPerMile)

minutesPerMile = aveSecondsPerMile // 60
secondsPerMile = aveSecondsPerMile % 60

print(minutesPerMile, "minutes", secondsPerMile, "seconds")
