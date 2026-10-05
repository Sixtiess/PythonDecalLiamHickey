# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    },
    "Antares": {
        "RA": "16h 29m 24.4s",
        "Dec": "−26° 25′ 55″",
        "Magnitude": 1.06,
        "Spectral Type": "M1.5Iab-Ib"
    },
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def print_star_names(targets):
    print("The stars in the targets dictionary are: ")
    for star in targets:
        print(star)

# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def print_star_details(targets):
    for star in targets:
        print(f"{star} has a spectral type of {targets[star]['Spectral Type']}")
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.



def find_big_stars(targets):
    for star in targets:
        if targets[star]["Magnitude"] > 0.1:
            print(f"{star} has a magnitude of {targets[star]['Magnitude']}")
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.

def find_brightest_star(targets):
    closest_star = None
    closest_declination = 1000000000000
    brightest_magnitude = 1000000000000

    for star, info in targets.items():
        declination = float(info["Dec"].split("°")[0])  # Extract the degree part of the Declination
        magnitude = info["Magnitude"]

        # First check if the current stars declination is closer to 20 than the one we have svaed so far, if it is we save it.
        #  If the declination is the same as the one we have saved, we check if the magnitude is brighter than the one we have saved, if it is we save it.
        if abs(declination - 20) < closest_declination or (abs(declination - 20) == closest_declination and magnitude < brightest_magnitude): 
            closest_declination = abs(declination - 20)
            brightest_magnitude = magnitude
            closest_star = star

    return closest_star
# 6) What is your favorite constellation?

print("Capricorn is my favorite constellation because it is the zodiac sign of my birthday and I like the mythology behind it.")
