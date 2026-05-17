class Road_length(BaseException):
    def __str__(self):
        return "length cant be 0 meters"

length = [-6, -9, 9, 6, 3,7]

def calculate_length(length):
    result = 0
    for n in length:
        if n <= 0:
            raise Road_length("Помилка: голос не може бути 0!")

        result += n

    return result

try:
     print(calculate_length(length))
except Road_length as e:
    print(e)
    print("error due to negative values")
except BaseException as e:
    print(f"some mistakes: {e}")