#Video Game Rental System - Midterm Project for CS 121
#Author: Mervin Debalucos

#Dictionary to store game library with quantity and cost
game_library = {"Donkey Kong": {"quantity": 3, "cost": 2}, "Super Mario Bros": {"quantity": 5, "cost": 3}, "Tetris": {"quantity": 2, "cost": 1}}
#Dictionary to store user accounts with password, balance and games rented
user_accounts = {}

#Main function to display the menu
def main():
  while True:
    try:
      print("Welcome to the Video Game Rental System!")
      print("1. Register")
      print("2. Login")
      print("3. Admin Login")
      print("4. Exit")

      choice = input("Enter your choice: ")
      if choice == "1":
        register_user()
      elif choice == "2":
        login()
      elif choice == "3":
        admin_login()
      elif choice == "4":
        print("Exiting program...")
        exit()
      else:
        print("Invalid choice. Please try again.")
    except ValueError:
      print("Invalid input. Please try again.") 
      return
    break

#Function to register a new user
def register_user():
  while True:
    try:
      print("Register for a new account")
      username = input("Enter a username: ")
      password = input("Enter a password: ")
      user_accounts[username] = {"password": password, "games_rented": []}
      balance = float(input("Enter your balance:$ "))
      user_accounts[username]["balance"] = balance
      print("Account created successfully!")
    except ValueError:
      print("Invalid input. Please try again.")
      return
    break
  
#Function to login to an existing account
def login():
  print("Login to your account")
  username = input("Enter your username: ")
  password = input("Enter your password: ")
  if username in user_accounts:
    if user_accounts[username]["password"] == password:
      logged_in_menu(username)
    else:
      print("Incorrect password. Please try again.")
  else:
    print("Account not found. Please register for an account.")

#Function to login as an admin
def admin_login():
  print("Admin Login")
  username = input("Enter your username: ")
  password = input("Enter your password: ")
  if username == "admin" and password == "adminpass":
    admin_menu()
  else:
    print("Incorrect username or password. Please try again.")

#Function to display the menu for a logged in user
def logged_in_menu(username):
  print("Welcome, " + username + "!")
  print("1. Rent a game")
  print("2. Return a game")
  print("3. View games rented")
  print("4. Display Inventory")
  print("5. Free Game Rental")
  print("6. Exit")

  choice = input("Enter your choice: ")
  if choice == "1":
    rent_game(username)
  elif choice == "2":
    return_game(username)
  elif choice == "3":
    view_games_rented(username)
  elif choice == "4":
    display_inventory(username)
  elif choice == "5":
    redeem_free_rental(username)
    print("Exiting program...")
    exit()
  else:
    print("Invalid choice. Please try again.")

#Function to redeem a free rental
def redeem_free_rental(username):
    if user_accounts[username]["balance"] >= 100:
        print("You have enough balance to redeem a free rental!")
        user_accounts[username]["balance"] -= 100
        print("You have successfully redeemed a free rental!")
    else:
        print("You do not have enough balance to redeem a free rental. Please try again later.")

#Function to display the inventory
def display_inventory(username):
    print("Inventory")
    print("1. View all games")
    print("2. View games by quantity")
    print("3. View games by cost")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        view_all_games()
    elif choice == "2":
        view_games_by_quantity()
    elif choice == "3":
        view_games_by_cost()
    elif choice == "4":
        print("Exiting program...")
        exit()
    else:
        print("Invalid choice. Please try again.")

#Function to view games by quantity in the library
def view_games_by_quantity():
    print("Games by quantity")
    sorted_games = sorted(game_library.items(), key=lambda x: x[1]["quantity"], reverse=True)
    for game in sorted_games:
        print(game[0] + " - Quantity: " + str(game[1]["quantity"]) + ", Cost: $" + str(game[1]["cost"]))  

#Function to view games by cost in the library
def view_games_by_cost():
    print("Games by cost")
    sorted_games = sorted(game_library.items(), key=lambda x: x[1]["cost"], reverse=True)
    for game in sorted_games:
        print(game[0] + " - Quantity: " + str(game[1]["quantity"]) + ", Cost: $" + str(game[1]["cost"]))  

#Function to display the menu for an admin
def admin_menu():
  print("Admin Menu")
  print("1. Add a game")
  print("2. Update game quantity")
  print("3. Update game cost")
  print("4. View all games")
  print("5. Exit")

  choice = input("Enter your choice: ")
  if choice == "1":
    add_game()
  elif choice == "2":
    admin_update_game()
  elif choice == "3":
    update_game_cost()
  elif choice == "4":
    view_all_games()
  elif choice == "5":
    print("Exiting program...")
    exit()
  else:
    print("Invalid choice. Please try again.")

#Function to rent a game
def rent_game(username):
  print("Games available for rent:")
  for game in game_library:
    print(game + " - Quantity: " + str(game_library[game]["quantity"]) + ", Cost: $" + str(game_library[game]["cost"]))

  game_to_rent = input("Enter the name of the game you want to rent: ")
  if game_to_rent in game_library:
    if game_library[game_to_rent]["quantity"] > 0:
      game_library[game_to_rent]["quantity"] -= 1
      user_accounts[username]["games_rented"].append(game_to_rent)
      print("Game rented successfully!")
    else:
      print("Game is out of stock. Please try again later.")
  else:
    print("Game not found. Please try again.")

#Function to return a game
def return_game(username):
  print("Games rented by " + username + ":")
  for game in user_accounts[username]["games_rented"]:
    print(game)

  game_to_return = input("Enter the name of the game you want to return: ")
  if game_to_return in user_accounts[username]["games_rented"]:
    game_library[game_to_return]["quantity"] += 1
    user_accounts[username]["games_rented"].remove(game_to_return)
    print("Game returned successfully!")
  else:
    print("Game not found in your rented games. Please try again.") 

#Function to view games rented by a user
def view_games_rented(username):
  print("Games rented by " + username + ":")
  for game in user_accounts[username]["games_rented"]:
    print(game)

#Function to add a game to the library
def add_game():
  game_name = input("Enter the name of the game you want to add: ")
  game_quantity = int(input("Enter the quantity of the game: "))
  game_cost = int(input("Enter the cost of the game: "))
  game_library[game_name] = {"quantity": game_quantity, "cost": game_cost}
  print("Game added successfully!")

#Function to update the quantity of a game
def admin_update_game():
  game_name = input("Enter the name of the game you want to update: ")
  if game_name in game_library:
    new_quantity = int(input("Enter the new quantity of the game: "))
    game_library[game_name]["quantity"] = new_quantity
    print("Game quantity updated successfully!")
  else:
    print("Game not found. Please try again.")

#Function to update the cost of a game
def update_game_cost():
  game_name = input("Enter the name of the game you want to update: ")
  if game_name in game_library:
    new_cost = int(input("Enter the new cost of the game: "))
    game_library[game_name]["cost"] = new_cost
    print("Game cost updated successfully!")
  else:
    print("Game not found. Please try again.")

#Function to view all games in the library
def view_all_games():
  print("All games in the library:")
  for game in game_library:
    print(game + " - Quantity: " + str(game_library[game]["quantity"]) + ", Cost: $" + str(game_library[game]["cost"]))

#Main function to run the program
if __name__ == "__main__":
  while True:
    main()

