import os
import platform

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
  items = os.listdir(path)
  for i, item in enumerate(items):
    print(f"{i+1}. {item}")

  choice = input("\nEnter the number of the folder/file to access or 'q' to quit: ")
  return choice, items

def main():
  """Main function to navigate the file system."""
  current_path = os.getcwd() + "/files" # Start at the 'files' directory
  while True:
    choice, items = display_options(current_path)

    if choice.lower() == 'q':
      break

    try:
      choice = int(choice)
      selected_item = items[choice - 1]
      selected_path = os.path.join(current_path, selected_item)

      if os.path.isdir(selected_path):
        current_path = selected_path 
        print("-" * 20) 
      elif os.path.isfile(selected_path):
        open_folder(selected_path) 
      else:
        print("Invalid selection.")

    except (ValueError, IndexError):
      print("Invalid input. Please enter a valid number or 'q'.")

if __name__ == "__main__":
  main()