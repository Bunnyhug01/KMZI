def save(value, fileName:str, type:str):
    with open(fileName, type) as file:
        file.write(value)