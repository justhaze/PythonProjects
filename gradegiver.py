class Silverwear:
    def __init__(self,fork,spoon,knife):
        self.fork = fork
        self.spoon = spoon
        self.knife = knife
    
    def handheld(self):
        print("I want " + self.fork + "forks." )
        print("I want "+ self.spoon + 'spoons.')
        print('I want ' + self.knife + 'knife.')
        

s1 = Silverwear(23,3,22)



#############
# student_scores = {
#     'Harry':81,
#     'Ron': 78,
#     'Hermione':99,
#     'Draco': 74,
#     'Neville': 62

# }

# for score in student_scores:
#     student_grades = {}
#     newscore = student_scores[score]
#     if newscore < 70:
#         student_grades[score] = 'TRASH AF'


# print(student_grades)


##############################################
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country_name,visit_count,city_count):
#     newlist = {}
#     newlist['country'] = country_name
#     newlist['visits'] = visit_count
#     newlist['cities'] = city_count
#     travel_log.append(newlist)
# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)