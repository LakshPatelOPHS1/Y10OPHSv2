rain = input("Is it raining rn? Yes or No ").lower()

if rain == "yes":
    wind = input("Is it windy? Yes or No ").lower()

    if wind == "yes":
        print("Its too windy for an umbrella")

    else:
        print("Take umbrella")

else:
    print("Nice")
