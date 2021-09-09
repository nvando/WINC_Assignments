__winc_id__ = "25a8041d2d5e4e3ab61ab1be43bfb863"
__human_name__ = "dictionaries"


def create_passport(name, date_birth, place_birth, height, nationality):
    passport = {
        "name": name,
        "date_of_birth": date_birth,
        "place_of_birth": place_birth,
        "height": height,
        "nationality": nationality,
    }
    return passport


def add_stamp(passport, country):

    # check whether visited country equals home country
    if country not in passport.values():
        # check if the passport already has a stamp
        if "stamps" not in passport.keys():
            # create a key-value pair for stamps: country
            passport["stamps"] = [country]
        elif country not in passport["stamps"]:
            # add the country to the list of countries (stamps)
            passport["stamps"].append(country)

    return passport


def check_passport(passport, destination, allowed_countries, banned_countries):
# check if citizen is allowed to travel to destination

    # first check if allowed countries have been listed for this nationality
    if passport["nationality"] in allowed_countries:
        # check if person's home country is allowing travel to destination
        if (
            destination in allowed_countries[passport["nationality"]]
            or destination == passport["nationality"]
        ):
            # check if destination is allowing person access
            if destination in banned_countries:
                # ceck for each stamp if it is not listed on the banned countries list of destination
                for stamp in passport['stamps']:
                    if stamp in banned_countries[destination]:
                        print("person not allowed entry as person has visited banned country")
                        return False
                if passport["nationality"] in banned_countries[destination]:
                    print("person not allowed entry as person is from banned country")
                    return False
                else:
                    print("person allowed to travel, adding stamp")
                    passport = add_stamp(passport, destination)
                    return passport
            elif destination not in banned_countries:
                print("no info for this destination on the banned countries list")
                passport = add_stamp(passport, destination)
                return passport
        else:
            print("destination not listed on the allowed country list")
            return False
    else:
        print("no info for this nationality in allowed country list")
        return False


allowed_countries = {
    # values: a list of countries that citizens that are from this country are allowed to travel to by that country.
    "Belgium": ["Netherlands", "Germany", "Cameroon", "North Korea"],
    "Germany": ["Netherlands", "Denmark"],
    "Netherlands": ["Germany", "Belgium", "India"],
}
banned_countries = {
    # values: a list of countries that a person is not allowed to have been to, as forbidden by the destination country.
    "Netherlands": ["North Korea", "Australia"],
    "Germany": ["North Korea", "Sweden", "India"],
}

passport_nikie = create_passport("Nikie", "1985-06-02", "Bemmel", 1.73, "Netherlands")
passport_nikie = add_stamp(passport_nikie, "Australia")
passport_nikie = add_stamp(passport_nikie, "India")
passport_nikie = add_stamp(passport_nikie, "Cameroon")
print(passport_nikie)
print(check_passport(passport_nikie, "Germany", allowed_countries, banned_countries))
