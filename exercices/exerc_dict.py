#Scroll down to see the answers!

#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
user = {
    'age': 33,
    'username': 'Awk',
    'weapons': ['katana', 'shuriken'],
    'is_active': True,
    'clan': 'yolo'
}

#2 iterate and print all the keys in the above user.
print(user.keys())

#3 Add a new weapon to your user
user['weapons'].append('shield')

#4 Add a new key to include 'is_banned'. Set it to false
user.update({'is_banned': False})

#5 Ban the user by setting the previous key to True
user['is_banned'] = True

#6 create a new user2 my copying the previous user and update the age value and username value. 
user2 = user.copy()
user2.update({'age': 100, 'username': 'TImbo'})
