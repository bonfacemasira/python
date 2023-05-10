thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# print(thisdict)
# print(type(thisdict))
# print(thisdict['year'])
def solution(data):
    count = 0

    for key, value in thisdict.items():
        count =+ 1
        # print(key, value)
        print(f'{key}: Quantity: {count} Price is {value}')


# solution(thisdict)

houses = {"Bonface": "Eldorado", "Leah": "Velga"}
# for house in houses:
print(houses['Leah'])