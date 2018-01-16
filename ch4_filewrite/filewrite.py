try:
    with open('file1.txt', 'w') as file1:
        print(file1)
    with open('file2.txt', 'w') as file2:
        print(file2)
except IOError as vlrErr:
    print(str(vlrErr))

#O uso do Try (com with) remove a necessidade de ter
# um finally somente para controlar o .close() dos arquivos
# Java copiou isso com o try-with-resources na JDK7
