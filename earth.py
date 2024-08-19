def earth():
    country_x = "Bangladesh"
    country_y = "Barbados"
    result_x_before_y = country_x < country_y
    result_y_before_x = country_y < country_x
    print(f"The result of {country_x} comes first in the dictionary than {country_y} is {result_x_before_y}.")
    print(f"The result of {country_y} comes first in the dictionary than {country_x} is {result_y_before_x}.")
