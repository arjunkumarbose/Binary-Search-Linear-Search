import search

def main():
    arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
    arr.sort()
    x = int(input("Enter the number to search: "))
    print("Sorted Array:", arr)

    # Perform linear search
    linear_result = search.linear_search(arr, x)
    if linear_result == -1:
        print("Linear search: Element not found")
    else:
        print(f"Linear search: Element found at index {linear_result}")

    # Perform binary search
    binary_result = search.binary_search(arr, x)
    if binary_result == -1:
        print("Binary search: Element not found")
    else:
        print(f"Binary search: Element found at index {binary_result}")

if __name__ == "__main__":
    main()
