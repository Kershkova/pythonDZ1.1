import re


def parse(query: str) -> dict:
    d = {}
    lenght = len(query)
    index_1 = query.find('name')
    print(index_1)
    index_2 = query.find('color')
    print(index_2)
    if index_1 != -1 and index_2 != -1:
        d = {}
    if index_1 != -1 and index_2 != -1:
        name = query[index_1 + 5 : index_2-1]
        color = query[index_2 + 5 : lenght]
        color = re.sub("[^A-Za-z]", "", color)
        d["name"] = name
        d["color"] = color
    else:
        if index_1 != -1 and index_2 == -1:
            name = query[index_1 + 4: lenght]
            name = re.sub("[^A-Za-z]", "", name)
            d["name"] = name
        else:
            if index_1 == -1 and index_2 != -1:
                color = query[index_2 + 5 : lenght]
                color = re.sub("[^A-Za-z]", "", color)
                d["color"] = color
    return d


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('http:///?name=Dima') == {'name': 'Dima'}
    assert parse('https://example.com/path/to/page?name=hoooom&color=black') == {'name': 'hoooom', 'color': 'black'}
    assert parse('https://example.com/path/to/page?=hoooom&color=black') == {'color': 'black'}
    assert parse('htcom/path/to/page?=hoooom&color=black') == {'color': 'black'}
    assert parse('https://example.com/path/to/page?numi=hoooom&cplor=black') == {}
    assert parse('e?name=hoooom&color=black') == {'name': 'hoooom', 'color': 'black'}
