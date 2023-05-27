from models import Quote, Author, Tag
import connect

def find(com):
    command = com.split(":")
    if command[0]== 'name':
        quotes=[]
        rec = Quote.objects.select_related()
        for record in records:
            print(record)
            quotes.append(record.quote)
        return(quotes)

    if command[0] == 'tag':
        quotes = []
        records = Quote.objects(tags__name=command[1])
        for record in records:
            print(record.quote)
            quotes.append(record.quote)
        return(quotes)

    if command[0] == 'tags':
        quotes = []
        tags = command[1]
        list_tag = tags.split(":")
        list = ' '.join(list_tag)
        list_tags = list.split(",")
        print(list_tags)
        records = Quote.objects(tags__name=list_tags[0])  or Quote.objects(tags__name=list_tags[1])
        for record in records:
            quotes.append(record.quote)
        return (quotes)

    if command[0] == 'exit':
        return ('exit')

if __name__ == "__main__":
    ex = True
    while ex:
        com = input('задайте параметры поиска в формате команда:значение_: ')
        result = find(com)
        if result == 'exit':
            ex = False
        print(result)