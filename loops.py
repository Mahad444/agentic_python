# while loop example
count = 0
while count < 100:
    print("Count is:", count)
    count += 1

# for loop example
video_games = ["Call of Duty", "FIFA", "PUBG", "Fortnite"]
for game in video_games:
    print("I love playing", game)

# range function example
video_games.append("GTA")

print("Updated list of video games:", video_games)


# for loop with range
for i in range(1, 11):
    print("Number:", i)
    if i == 5:
        print("Halfway there!")

# for loop with range and step
for i in range(0, 20, 2):
    print("Even number:", i)