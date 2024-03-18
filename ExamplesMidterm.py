# Write a function that forces the user to enter a multiple of 6. Use try except to catch invalid inputs.
def m6():
    """
    A function that returns a multiple of 6
    :return: the multiple of 6 entered by the user
    """
    while True:
        try:
            # first we need to read a number
            number = input("Please give me a multiple of 6: ")
            number = int(number)
        except ValueError:
            # if the number is not valid print an error and retry
            print("That is not a number. Retry")
            continue
        # check if the number is a multiple of 6
        if number % 6 == 0:
            # return the value
            return number
        # print an error and try again

        print("That number is not a multiple of 6. Retry")


print("A multiple of 6 is", m6())