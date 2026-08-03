hackerfile = open("hackme.txt", "r")

info = hackerfile.readlines()
print("here is someone to hack - information")
print(info[0])
print(info[1])
print(info[2])
print(info[3])
print(info[4])

hackerfile.close()