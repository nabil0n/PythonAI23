print(__name__)

def main():
    for i in range(5):
        print(f"{i} = {square(i)}")
        
def square(n):
    return n*n

if __name__ == "__main__":
    main()