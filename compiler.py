import carrot

for line in open('test.carrot'):
    result, error = carrot.run('<stdin>', line)

    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))

            