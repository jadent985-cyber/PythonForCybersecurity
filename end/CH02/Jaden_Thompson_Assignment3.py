name = input("What is your name?")
color = input("What is your favorite color?")
pet = input("What is your first pet's name?")
maiden = input("What is your mother's maiden name?")
school = input("What elementary school did you attend?")

hackerfile = open("hackme.txt", "w")
hackerfile.write(name + "\n")
hackerfile.write(color + "\n")
hackerfile.write(pet + "\n")
hackerfile.write(maiden +"\n")
hackerfile.write(school + "\n")

hackerfile.close()