# Imports
from time import sleep

# Global variables


# Functions
def create_list():
    print("Du ska få göra en lista alldeles snart")
    name = input("Vems lista är det? (Använd _ mellan för- och efternamn om det önskas) ")
    length = int(input("Hur många saker ska listan innehålla? "))
    with open(f"wish_list\{name}.txt", "wt") as wish_list:
        for _ in range(length): 
            wish_list.write(input(f"Vad önskar sig {name}? "))
    print("Listan har skapats och skickas nu till tomteverkstaden!")

def read_list():
    name = input("Vems lista vill du ha uppläst? ")
    wish_list = []
    with open(f"wish_lists\{name}.txt", "rt") as list_items:
        for line in list_items.readlines(): 
            wish_list.append(line.strip("\n"))
    print(f"{name}s lista:")
    for i in wish_list: 
        print(i)

def naughty_list():
    print("Hehehe")
    additions = int(input("Hur många ska skrivas upp på listan? "))
    with open("naughty_list.txt", "wt") as naughty_list:
        for _ in range(additions):
            naughty_list.write(input("Vem har varit stygg? "))
    read_naughty_list = input("Vill du läsa upp listan? (Ja eller Nej) ")
    if read_naughty_list == "Ja":
        with open("naughty_list.txt", "rt") as kids:
            for line in kids.readlines():
                print(line.strip("\n"))

# Main function
def main():
    print("\tTomtevikariat\nDu kommer få välja mellan:\n1. Göra en önskelista\n2. Läsa upp en önskelista\n3. Lägga till namn i Naughty List\n4. Stänga programmet")
    while True:
        choice = input("Ditt val: ")
        if choice == "1":
            create_list()
        elif choice == "2":
            read_list()
        elif choice == "3":
            naughty_list()
        elif choice == "4":
            print(f"Stänger av programmet{sleep(0.1)}.{sleep(0.1)} .{sleep(0.1)} .{sleep(0.2)}\nVänligen vänta{sleep(0.1)}.{sleep(0.1)} .{sleep(0.1)} .")
            break
        else: print("Fel inmatning, försök igen.")

# Call Main
if __name__ == "__main__":
    main()