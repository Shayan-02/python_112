n = int(input("عدد مورد نظر خود را وارد کنید: "))

# yekan va dahgan
yekan = n % 10 # baghimandeh taghsim e adad daryaft shode az karbar bar 10
dahgan = n // 10 # kharj e ghesmate taghsim e adad daryaft shode az karbar bar 10

reverse = str(yekan) + str(dahgan)
print("reverse :", reverse)

# first_name = input("enter your first name: ")
# last_name = input("enter your last name: ")

# full_name = first_name + " " + last_name
# print("your full name is:", full_name)