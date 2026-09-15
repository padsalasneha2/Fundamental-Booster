print("welcome to the intrective personal data collecter")
print()

name = input("please enter your name: ")
age = int(input("please enter your age: "))
height = float(input("please enter your height in meters: "))
favorite_number = int(input("please enter your favorite number: "))
print()

print("thank you for providing your information!")
print()
print("name: ", name, "(type: ", type(name), ", memory address: ", id(name), ")")
print("age: ", age , "(type: ", type(age), ", memory address: ", id(age), ")")
print("height: ", height , "(type: ", type(height), ", memory address: ", id(height), ")")
print("favorite number: ", favorite_number , "(type: ", type(favorite_number), ", memory address: ", id(favorite_number), ")")
print()

birth_year = 2026 - age
print("Your birth year is approximately:", birth_year,
      "(based on your age of", age, ")")

print()
print("Thank you for using the Personal Data Collector. Goodbye!")