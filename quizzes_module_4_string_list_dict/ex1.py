def format_address(address_string):
    house_number = ""
    street_name = ""

    # Separate the house number from the street name.

    address_parts = address_string.split()

    for index,address_part in enumerate(address_parts):
        # Complete the if-statement with a string method.
        if index == 0:
            house_number = address_part
        else:
            street_name += address_part + " "
    # Remove the extra space at the end of the last "street_name".
    # Use a string method to return the required formatted string.
    return f"House number {house_number} on a street named {street_name}"


print(format_address("123 Main Street"))
# Should print: "House number 123 on a street named Main Street"


# print(format_address("1001 1st Ave"))
# # Should print: "House number 1001 on a street named 1st Ave"
#
#
# print(format_address("55 North Center Drive"))
# # Should print "House number 55 on a street named North Center Drive"
