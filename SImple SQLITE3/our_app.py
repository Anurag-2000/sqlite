import database


database.add_one('raju', 'Shanker', 'radheradhe@gmail.com')
database.delete_one('6')

myliz=[
    ('idk', 'idc', 'ily@gmail.com'),
    ('ttly', 'foff', 'beyach@gmail.com')
    ]

database.add_many(myliz)
database.search_email('anurag3sharma4@gmail.com')

# database.show_all()

