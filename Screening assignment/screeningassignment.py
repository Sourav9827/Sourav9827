def replacestring(filename="example.txt", wordtoreplace="placement", wordtoreplacewith="screening"):
    try:
        file = open(filename, "r")
        data = file.read()
        data = data.replace(wordtoreplace, wordtoreplacewith)
        file.close()
        file = open(filename, "w")
        file.write(data)
        file.close()
    except Exception as e:
        print(e)

x = input("File name: ")
y = input("word to replace: ")
z = input("Word to replace with: ")

replacestring(x, y, z)