import json


# book_info = {
#     'title': 'Sherlok Holmes',
#     'autor': 'Arthur Conan Doyle',
#     'publication year': 1887,
#     'genre': ['detective', 'novel']
# }
#
# with open ('data.json', 'w') as json_file:
#     json.dump(book_info, json_file)

# book_info_str = json.dumps(book_info)
#
# print(type(book_info_str))


# book_info_str = '{"title": "Sherlok Holmes", "autor": "Arthur Conan Doyle", "publication year": 1887, "genre": ["detective", "novel"]}'
#
# book_info = json.loads(book_info_str)
#
# print(book_info)
# print(type(book_info))

with open('data.json') as json_file:
    book_info = json.load(json_file)

    print(book_info)
    print(type(book_info))