# Task

# 1 Create a dictionary 
# {"city": "Moscow", "temperature": "20"}
geo_position = {
    "city": "Moscow",
    "temperature": 20
}
# 2 Display the value of the city key
print(geo_position["city"])
# 3 Decrease the "temperature" value by 5
geo_position["temperature"] -= 5
print(geo_position["temperature"])
# 4 Display the entire dictionary
print(geo_position)
# 5 Check if the dictionary contains the country key

# print(geo_position["country"])
print(geo_position.get("coutnry"))
# 6 Print the default value "Russia" for the country key
print(geo_position.get("country", "Russia"))
# 7 Add a date element to the dictionary with the value 
# "05/27/2019"
geo_position["date"] = "05/27/2019"
# 8 Display the length of the dictionary
print(len(geo_position))