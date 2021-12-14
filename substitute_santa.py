# Imports
from time import sleep

# Global variables


# Functions
def create_list():
    pass

def read_list():
    pass
# Main function
def main():
    print("\tTomtevikariat\nDu kommer få välja mellan:\t1. Göra en önskelista\t2. Läsa upp en önskelista\t3. Stänga programmet")
    while True:
        choice = input("Ditt val: ")
        if choice == "1":
            create_list()
        elif choice == "2":
            read_list()
        elif choice == "3":
            print(f"Stänger av programmet{sleep(0.1)}.{sleep(0.1)} .{sleep(0.1)} .{sleep(0.2)}\nVänligen vänta{sleep(0.1)}.{sleep(0.1)} .{sleep(0.1)} .")
            break
        else: print("Fel inmatning, försök igen.")

# Call Main
if __name__ == "__main__"_:
    main()