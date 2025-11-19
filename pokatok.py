import time
import os
import sys

# Global variable to track items collected
inventory = []

def clear_screen():
    """Clears the console screen for a fresh view."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(text, delay=0.03):
    """Types out text for dramatic effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

def pause():
    """Waits for user input to proceed."""
    print("\n")
    input(">> Press ENTER to continue...")
    print("\n")

def get_choice(options):
    """
    Handles user input safely.
    options: A dictionary like {'1': 'do_something', '2': 'do_other'}
    """
    while True:
        print("What will you do?")
        for key, description in options.items():
            print(f"  [{key}] {description}")
        
        choice = input("\n> ").strip().upper()
        
        if choice in options:
            return choice
        else:
            print("I did not understand that. Please type the number of your choice.")

# --- SCENES ---

def start():
    # Reset inventory if restarting
    global inventory
    inventory = []
    
    clear_screen()
    print("="*60)
    print("       T H E   B A L L G A M E   O F   X I B A L B A")
    print("="*60)
    print("\n")
    print_slow("Many years ago, the First Twins played ball too loudly.")
    print_slow("The Lords of the Underworld (Xibalba) were annoyed.")
    print_slow("The First Twins failed the tests and were defeated.")
    print("\n")
    print_slow("Now, YOU are the New Twins: Hunahpu and Xbalanque.")
    print_slow("You have accepted the challenge to restore honor to your family.")
    
    pause()
    crossroads()

def crossroads():
    clear_screen()
    print("--- THE CROSSROADS ---")
    print("You descend deep into the earth. You arrive at four paths:")
    print("Red, White, Yellow, and Black.")
    print("\nThe Lords are hiding. A mosquito named Xan buzzes near your ear.")
    print("\n")

    options = {
        "1": "Walk the Black Path alone",
        "2": "Send Xan the Mosquito ahead to scout"
    }
    choice = get_choice(options)

    if choice == "1":
        print_slow("You walk into the dark. The Lords trick you immediately!")
        game_over_screen("You were lost in the dark.")
    else:
        print_slow("Smart choice. Xan flies ahead.")
        print_slow("Xan bites the wooden dummies. They are silent.")
        print_slow("Xan bites the REAL Lords. They yell 'Ouch!' revealing their names.")
        inventory.append("Secret Names")
        pause()
        throne_room()

def throne_room():
    clear_screen()
    print("--- THE GREETING ---")
    print("You enter the court knowing the Lords' names.")
    print("They look surprised, but they smile wickedly.")
    print("\nThey point to a large, beautiful stone bench.")
    print("'Welcome, Twins! Please, rest on our throne of honor.'")
    print("\n")

    options = {
        "1": "Sit on the Throne",
        "2": "Sit on the Floor"
    }
    choice = get_choice(options)

    if choice == "1":
        print_slow("AAAAH! The stone is boiling hot!")
        game_over_screen("You were burned and cannot play.")
    else:
        print_slow("You politely decline: 'This seat is too good for us.'")
        print_slow("You sit on the cool floor.")
        print_slow("The Lords scowl. You have passed the first test.")
        pause()
        house_of_gloom()

def house_of_gloom():
    clear_screen()
    print("--- THE HOUSE OF GLOOM ---")
    print("The Lords hand you a lit torch and a cigar.")
    print("'Keep this light burning all night,' they say.")
    print("'But return it tomorrow UNUSED.'")
    print("\nIt is a paradox. How do you keep fire without burning the wood?")
    print("\n")

    options = {
        "1": "Let the torch burn normally",
        "2": "Swap the flame for red Macaw feathers"
    }
    choice = get_choice(options)

    if choice == "1":
        print_slow("The torch turns to ash by morning.")
        game_over_screen("The Lords execute you for failing the task.")
    else:
        print_slow("Brilliant!")
        print_slow("From a distance, the red feathers look like fire.")
        print_slow("In the morning, you return the torch unburned.")
        pause()
        ballgame()

def ballgame():
    clear_screen()
    print("--- THE TLACHTLI COURT ---")
    print("You have survived the night. Now, the sport begins.")
    print("The heavy rubber ball bounces on the stone court.")
    print("The Lords serve the ball to you.")
    print("\n")

    score = 0
    rounds = 0
    
    while rounds < 3:
        print(f"ROUND {rounds + 1} | SCORE: {score}")
        options = {
            "1": "High Lob",
            "2": "Hip Strike (Solid)",
            "3": "Low Slide"
        }
        choice = get_choice(options)

        # Simple logic: 2 is always right in this simplified version
        if choice == "2":
            print("\n>> SMACK! A perfect hit off the hip. You score!\n")
            score += 1
        elif choice == "1":
            print("\n>> Too high! The Lords smash it back easily.\n")
        else:
            print("\n>> Too low! You scrape your knee on the stone.\n")
        
        rounds += 1
        time.sleep(1)

    if score >= 1:
        print_slow("The Lords are furious that you are winning.")
        print_slow("They cheat and throw the ball into the House of Fire.")
        pause()
        finale()
    else:
        game_over_screen("The Lords defeated you in the game.")

def finale():
    clear_screen()
    print("--- THE GRAND TRICK ---")
    print("The Twins realize they cannot win by normal rules.")
    print("You allow yourselves to be burned, but then you return!")
    print("\nYou perform miracles, bringing things back to life.")
    print("The Lords are amazed. 'Burn us!' they command. 'Make us young again!'")
    print("\n")

    options = {
        "1": "Burn them and REVIVE them",
        "2": "Burn them and DO NOT revive them"
    }
    choice = get_choice(options)

    if choice == "1":
        print_slow("You revive the evil Lords. They thank you... by eating you.")
        game_over_screen("You were too merciful.")
    else:
        victory()

def victory():
    clear_screen()
    print("\n" + "*"*60)
    print("                   V I C T O R Y !")
    print("*"*60 + "\n")
    print_slow("The Lords turn to ash and blow away in the wind.")
    print_slow("Xibalba is defeated.")
    print_slow("Hunahpu and Xbalanque rise into the sky.")
    print("\nThey become the SUN and the MOON.")
    print("\nCongratulations! You have completed the story.")
    input("\nPress Enter to exit.")
    sys.exit()

def game_over_screen(reason):
    print("\n" + "-"*40)
    print("G A M E   O V E R")
    print(f"Reason: {reason}")
    print("-"*40 + "\n")
    
    options = {"1": "Try Again", "2": "Quit"}
    choice = get_choice(options)
    
    if choice == "1":
        start()
    else:
        print("Goodbye.")
        sys.exit()

# Entry point
if __name__ == "__main__":
    start()
