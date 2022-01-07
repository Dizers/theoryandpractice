
class SpecialHashMapException(Exception):
    pass

class IlocObject:
    def __init__(self, dict_):
        self.dict_ = dict_

    def __getitem__(self, key):
        items = sorted(self.dict_.items())
        return items[key][1]


class PlocObject:
    def __init__(self, dict_):
        self.dict_ = dict_

    def __getitem__(self, key):
        try:
            result = {}
            conditions = key.replace(' ', '').replace('<>', '!=').split(',')

            for key_str, value in self.dict_.items():
                expression = ''
                key = key_str.replace('(', '').replace(')', '').split(',')

                if len(key) == len(conditions):
                    expression = ' and '.join(
                        [item[0] + item[1] for item in zip(key, conditions)])
                    if eval(expression):
                        result.update({
                            key_str: value
                        })

            return result
        except Exception as e:
            raise SpecialHashMapException(e)


class SpecialHashMap(dict):
    def __init__(self):
        self.ploc = PlocObject(self)
        self.iloc = IlocObject(self)


if __name__ == '__main__':

    map = SpecialHashMap()
    map['value1'] = 1
    map['value2'] = 2
    map['value3'] = 3
    map['1'] = 10
    map['2'] = 20
    map['3'] = 30
    map['1,5'] = 100
    map['5,5'] = 200
    map['10,5'] = 300

    print(map.iloc[0])
    print(map.iloc[2])
    print(map.iloc[5])
    print(map.iloc[8])

    print('Условие:')

    map = SpecialHashMap()
    map['1'] = 10
    map['2'] = 20
    map['3'] = 30
    map['(1,5)'] = 100
    map['(5,5)'] = 200
    map['(10,5)'] = 300
    map['(1, 5, 3)'] = 400
    map['(5, 5, 4)'] = 500
    map['(10, 5, 5)'] = 600

    print(map.ploc['>=1'])
    print(map.ploc['<3'])
    print(map.ploc['>0, >0'])
    print(map.ploc['>=10, >0'])
    print(map.ploc['<5, >=5, >=3'])
