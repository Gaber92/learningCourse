# with open ("/Users/lukagaber/Desktop/SmartNinja/Python/questions.txt") as file_handle:
#     basicQuestions = file_handle.read()
#     print(basicQuestions)


# with open("/Users/lukagaber/Desktop/SmartNinja/Python/temp_lj.txt") as temp_handler:

#     min_temp = 10000
#     for line in temp_handler:
#         line = line.rstrip().split(",")

#         temperature_of_line = int(line[1])
#         if min_temp > temperature_of_line:
#             min_temp = temperature_of_line
#     print(min_temp)

# izračunaj še minimalno pa povprečno temperaturo
import json 


jordan = {
    "name": "Micheal",
    "age": 31,
    "position" : "Point Guard",
    "place_of_birth": "Chicago",
    "favourite_food": ["pasta", "pizza", "salad"]
        }

with open("/Users/lukagaber/Desktop/SmartNinja/Python/jordan.json", "w") as file_h:
    jordan_json = json.dumps(jordan)
    file_h.writelines(jordan_json)

