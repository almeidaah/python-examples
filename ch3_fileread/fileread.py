try:
    data = open('file.txt')

    for each_line in data:
        try:
            (role, line) = each_line.split(":", 1)
            print(role, '')
            print( ' said : ', '')
            print( line, '')
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing');