import os
import platform
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def open_folder(path):
    """Opens the folder at the given path and attempts to highlight the file."""
    system = platform.system()

    if system == "Windows":
        os.startfile(path)
    elif system == "Darwin":  # macOS
        os.system(f"open -R '{path}'")
    elif system == "Linux":
        os.system(f"xdg-open '{path}'")
    else:
        print("Unsupported operating system.")

def display_options(path):
    """Displays available folders and files for user selection."""
    clear()
    print(f"Current Directory: {path}")  # Display the current directory
    items = os.listdir(path)
    for i, item in enumerate(items):
        print(f"{i+1}. {item}")

    print(f"\n{Fore.BLUE}{Style.BRIGHT}[0/~] Go back to the previous directory{Style.RESET_ALL}")
    choice = input(f"\n{Fore.BLUE}{Style.BRIGHT}[{failure}] Enter the number of the folder/file to access or 'q' to quit: {Style.RESET_ALL}")
    return choice, items

def main():
    """Main function to navigate the file system."""
    global failure
    failure = 0
    current_path = "S:/School/DB/files"  # Start at the 'files' directory

    while True:
        choice, items = display_options(current_path)

        if choice.lower() == 'q':
            break
        elif choice == '0' or choice == '~':
            current_path = os.path.dirname(current_path)  # Go up one directory
        else:
            try:
                choice = int(choice)
                selected_item = items[choice - 1]
                selected_path = os.path.join(current_path, selected_item)

                if os.path.isdir(selected_path):
                    current_path = selected_path
                    print("-" * 20)
                elif os.path.isfile(selected_path):
                    open_folder(selected_path)
                    time.sleep(5)
                    break
                else:
                    clear()
                    failure += 1  # Increment failure counter on invalid selection
                    if failure < 5:
                        print(f"{Fore.RED}{Style.BRIGHT}Invalid selection.{Style.RESET_ALL}")
                    elif 5 <= failure < 10:
                        print(f"{Fore.RED}{Style.BRIGHT}Are you an idiot? Try to use this program correctly!!!.{Style.RESET_ALL}")
                        time.sleep(0.3)
                    elif 10 <= failure < 20:
                        print(f"{Fore.RED}{Style.BRIGHT}I quit this job, find the files yourself.{Style.RESET_ALL}")
                        time.sleep(0.6)
                        open_folder(current_path)
                        time.sleep(1)
                        break
                    time.sleep(1)

            except (ValueError, IndexError):
                clear()
                failure += 1  # Increment failure counter on invalid selection
                if failure < 5:
                    print(f"{Fore.RED}{Style.BRIGHT}Invalid selection.{Style.RESET_ALL}")
                elif 5 <= failure < 10:
                    print(f"{Fore.RED}{Style.BRIGHT}Are you an idiot? Try to use this program correctly!!!.{Style.RESET_ALL}")
                    time.sleep(0.3)
                elif 10 <= failure < 20:
                    print(f"{Fore.RED}{Style.BRIGHT}I quit this job, find the files yourself.{Style.RESET_ALL}")
                    time.sleep(0.6)
                    open_folder(current_path)
                    time.sleep(1)
                    break
                time.sleep(1)

if __name__ == "__main__":
    main()