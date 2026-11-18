
# Find alphabetical order of key characters
def get_order(key):
    return sorted(range(len(key)), key=lambda i: key[i])


# Encryption
def encrypt(message, key):
    message = message.replace(" ", "").upper()
    key = key.upper()

    cols = len(key)

    # Add padding X
    while len(message) % cols != 0:
        message += "X"

    rows = len(message) // cols

    # Create grid row by row
    grid = []

    for i in range(rows):
        grid.append(list(message[i * cols:(i + 1) * cols]))

    print("\nGrid:")
    print(" ".join(key))

    for row in grid:
        print(" ".join(row))

    # Read columns in alphabetical order
    cipher = ""

    for c in get_order(key):
        for r in range(rows):
            cipher += grid[r][c]

    return cipher


# Decryption
def decrypt(cipher, key):
    key = key.upper()

    cols = len(key)
    rows = len(cipher) // cols

    # Create empty grid
    grid = [[""] * cols for i in range(rows)]

    # Fill columns in alphabetical order
    k = 0

    for c in get_order(key):
        for r in range(rows):
            grid[r][c] = cipher[k]
            k += 1

    # Read grid row by row
    plain = ""

    for r in range(rows):
        plain += "".join(grid[r])

    return plain.rstrip("X")


# Main Program
message = input("Enter message: ")
key = input("Enter key: ")

encrypted = encrypt(message, key)
print("\nEncrypted:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)
