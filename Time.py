print("Please enter a number greater than 60:")
ms = int(input())

weeks = ms / 604800
days = weeks / 7
hours = days / 24
minutes = hours / 60
seconds = ms % 60

seconds1 = int(seconds)
minutes1 = int(minutes)
hours1 = int(hours)
days1 = int(days)
weeks1 = int(weeks)


if ms>604800:
    print(f"{weeks1}", end=' ')
elif ms<604800:
    print(f"A week", end=' ')
elif ms<172800:
    print(f"{days1}", end=' ')
elif ms<86400:
    print("A day", end=' ')
elif ms<7200:
    print(f"{hours1}", end=' ')
elif ms<3600:
    print("An hour", end=' ')
elif ms>=120:
    print(f"{minutes1}", end=' ')
elif ms<=199:
    print("A minute", end=' ')
elif ms<60:
    print(f"{seconds1}")
else:
    print("MY BRAIN IS FRIED")
