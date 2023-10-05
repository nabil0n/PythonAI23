from gg27_Modul import square

def main():
    test_square()

def test_square():
    assert square(2) == 4
    assert square(5) == 25
    assert square(1) == 1
    assert square(-5) == 25

if __name__ == "__main__":
    main()

# q.square(5)

# print("start")

# try:
#     assert 1 < 0
# except AssertionError:
#     print("0 is not more than 1")

# print("end")