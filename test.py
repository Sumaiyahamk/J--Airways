from crud import add_passenger, get_passengers

add_passenger("Sumaiya", "Rahman", 22)

get_passengers()

from crud import *

# CREATE
add_passenger("John", "Smith", 25)

# READ
print("All Passengers:")
get_passengers()

# UPDATE
update_passenger(1, 30)

# DELETE
delete_passenger(2)

# READ AGAIN
print("After Update/Delete:")
get_passengers()