def earth():
    country_x = "Bangladesh"
    country_y = "Barbados"
    result_x_first = (country_x.lower() < country_y.lower())
    result_y_first = (country_y.lower() < country_x.lower())
    print(f"The result of {country_x} comes first in the dictionary than {country_y} is {result_x_first}.")
    print(f"The result of {country_y} comes first in the dictionary than {country_x} is {result_y_first}.")
