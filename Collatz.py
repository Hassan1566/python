import sys
def collatz(n):
    print(n, end=' ')
    if n == 1:
        return
    if n % 2 == 0:
        collatz(n // 2)
    else:
        collatz(3 * n + 1)

def main():
    print("Enter a number:")
    try:
        number = int(input())
        if number <= 0:
            raise ValueError("Number must be positive.")
    except ValueError as e:
        print("Invalid input:", e)
        sys.exit(1)
        
    collatz(number)
    print()  # For a newline after the sequence
    sys.exit()

main()