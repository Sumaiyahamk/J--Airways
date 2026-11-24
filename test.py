from crud import add_passenger, delete_passenger, get_passengers, update_passenger

# 1. READ (first 5 passengers)
print("Sample Passengers:")
for row in get_passengers(limit=5):
    print(row)

# 2. CREATE a test passenger
add_passenger("TEST01", "Tamim", "Iqbal", "Male", 35, "Bangladesh")
print("Added TEST01")

# 3. UPDATE the test passenger's age
update_passenger("TEST01", 30)
print("Updated TEST01 age to 30")

# 4. DELETE the test passenger so the database stays clean
delete_passenger("TEST01")
print("Deleted TEST01")