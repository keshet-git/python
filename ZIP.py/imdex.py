usernames = ["Bro","Dude","Raichl"]
passwords = ("p~ssword","pypu","guest")
login_data = ['1/1/2021','1/2/2021','1/3/2021']
#users = dict(zip(usernames, passwords))

#print(type(users))
#for key,value in users.items():
 #   print(key+' '+value)

users = (zip(usernames, passwords, login_data))


for i in users:
    print(i)