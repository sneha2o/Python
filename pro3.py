# Write a program to create a byte type array, read, modify, and display the elements of the array 

def main():
    byte_array = bytearray([10, 20, 30, 40, 50])
    print("Original byte array: ", byte_array)

    print("Reading Elements: ")
    for i in range(len(byte_array)):
        print(f"Element at index {i}:{byte_array[i]}")

    byte_array[1] = 22
    byte_array[3] = 55

    print("\n Modified byte array:", byte_array)

    print("Reading modified elements: ")
    for i in range(len(byte_array)):
        print(f"Elements at index {i}: {byte_array[i]}")

main()

# output:
# Original byte array:  bytearray(b'\n\x14\x1e(2')
# Reading Elements: 
# Element at index 0:10
# Element at index 1:20
# Element at index 2:30
# Element at index 3:40
# Element at index 4:50

#  Modified byte array: bytearray(b'\n\x16\x1e72')
# Reading modified elements: 
# Elements at index 0: 10
# Elements at index 1: 22
# Elements at index 2: 30
# Elements at index 3: 55
# Elements at index 4: 50


