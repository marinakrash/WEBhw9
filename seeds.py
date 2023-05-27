import json
import string

from models import Quote, Author, Tag
import connect

with open('authors.json') as file:
    file_data = json.load(file)
    for row in file_data:
        a=Author(fullname = row['fullname'], born_date = row['born_date'],
                        born_location=row['born_location'], description=row['description'])
        a.save()
        with open('quotes.json') as file:
            file_data2 = json.load(file)
            for row2 in file_data2:
                if row2['author'] == row['fullname']:
                    tag = Tag(name=row2['tags'])
                    Quote(tags = tag, author = a, quote = row2['quote']).save()