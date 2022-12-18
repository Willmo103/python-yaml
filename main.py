practice_file = """ doe: "a deer, a female deer"
 ray: "a drop of golden sun"
 pi: 3.14159
 xmas: true
 french-hens: 3
 calling-birds:
   - huey
   - dewey
   - louie
   - fred
 xmas-fifth-day:
   calling-birds: four
   french-hens: 3
   golden-rings: 5
   partridges:
     count: 1
     location: "a pear tree"
   turtle-doves: two"""


def yaml_to_dict(file: str):
    raw = file.splitlines()
    # print(raw)
    for line in raw:
        split_line = line.split(':')
        if len(split_line) > 1:
            key, value = split_line[0], split_line[1]
        else:
            print(line)

        print(key)
        print(value)


if __name__ == '__main__':
    yaml_to_dict(practice_file)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
