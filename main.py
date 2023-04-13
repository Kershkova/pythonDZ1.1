import re


def parse_cookie(query: str) -> dict:
    d = {}
    lenght = len(query)
    index_1 = query.find('name')
    index_2 = query.find('age')
    if index_1 == -1 and index_2 == -1:
        d = {}
    if index_1 != -1 and index_2 != -1:
        name = query[index_1 + 5 : index_2-1]
        age = query[index_2 + 4 : lenght]
        age = re.sub("[^0-9]", "", age)
        d["name"] = name
        d["age"] = age

    else:
        if index_1 != -1 and index_2 == -1:
            name = query[index_1 + 5: lenght]
            name = re.sub("[^A-Za-z]", "", name)
            d["name"] = name
        else:
            if index_1 == -1 and index_2 != -1:
                age = query[index_2 + 4: lenght]
                age = re.sub("[^0-9]", "", age)
                d["age"] = age
    return d


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28k,,sjdbf ajkhdgf ajsd;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28k,,sjdbf ajkhdgf ajsd;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('er;age=28;') == {'age': '28'}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('12345mfjdj djldkshdg') == {}
    assert parse_cookie('age=35') == {'age': '35'}
    assert parse_cookie('name=Dima/age=28;') == {'name': 'Dima', 'age': '28'}
