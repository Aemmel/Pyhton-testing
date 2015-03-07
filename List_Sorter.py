#
# tried using the "try" and "except" statements properly and some new tequnices
# after getting back to python after 5 (!) months, I can see why its so popular. Just a beautiful language 
#


__author__ = 'Emil Donkersloot'


def main():
    var_inp = "" #def
    ul = [] #def
    while var_inp.lower() != "stop":
        try:
            var_inp = input("Write number or 'stop': ")
            if var_inp.lower() == "stop":
                break
            ul.append(int(var_inp))
        except ValueError:
            print("Input must be an integer number or 'stop'")

    ul.sort()
    print(ul)


if __name__ == '__main__':
    main()
