# 12 Beginner Python Projects with https://www.youtube.com/watch?v=8ext9G7xspg&ab_channel=freeCodeCamp.org

# # String concatenation (how to put strings together)
# # Suppose we want to create a string that says "Subscribe to ______"
# youtuber = "Chai Tea" # Some string variable

# # a few ways to do this
# print("Subscribe to " + youtuber)
# print("Subscribe to {}".format(youtuber))
# print(f"Subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")

madlibs = f"Computer programming is so {adj}! It makes so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlibs)