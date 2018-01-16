man = []
other = []

try:

    with open('data.txt') as data:
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(':', 1)
                #Retira espaços em branco, como o .trim() do Java
                line_spoken = line_spoken.strip()
                if role == 'Man':
                    man.append(line_spoken)
                elif role == 'Other Man':
                    other.append(line_spoken)

            except ValueError:
                pass
    #data.close()
except IOError:
    print('Data file is missing')