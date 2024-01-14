import carrot

while True:
    text = input('carrot> ')
    result, error = carrot.run('fileName', text)

    if error: print(error.as_string())
    else: print(result)

    