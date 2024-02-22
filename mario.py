def main():
    while True:
        height_str = input("Height: ")
        try:
            height = int(height_str)
            if 1 <= height <= 8:
                break
            else:
                print("Please enter a number between 1 and 8.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    for i in range(1, height + 1):
        spaces = height - i
        blocks = i

        print(" " * spaces, end="")
        print("#" * blocks)

if __name__ == "__main__":
    main()
