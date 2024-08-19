def earth():
    country_x = "Bangladesh"
    country_y = "Barbados"
    sorted_countries = sorted([country_x, country_y])
    result_x_first = (sorted_countries[0] == country_x)
    result_y_first = (sorted_countries[0] == country_y)
    print(f"The result of {country_x} comes first in the dictionary than {country_y} is {result_x_first}.")
    print(f"The result of {country_y} comes first in the dictionary than {country_x} is {result_y_first}.")
