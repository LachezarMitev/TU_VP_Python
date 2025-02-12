def ReadTXT(file):
    try:
        f = open(f, 'r')
        output = f.read()
        return output
    except:
        return "Sth went wrong!"

print(ReadTXT(input()))