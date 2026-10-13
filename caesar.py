def shift_char(ch, shift):
    if ch.isupper():
        base = ord('A')
    elif ch.islower():
        base = ord('a')
    else:
        return ch
    return chr((ord(ch)- base + shift)%26 + base)
def caesar(text, shift):
    return "".join([shift_char(ch, shift)for ch in text])

def brute_force(ciphertext):
    print("\n Brute-force: trying all 26 shifts")
    print("-" * 40)
    for shift in range(26):
        guess = caesar(ciphertext, shift)
        print(f"shift{shift:2d}:{guess}")


def main():
    print("=" * 40)
    print("Caesar cipher Tool")
    print("=" * 40)
    print("1. Encoding")
    print("2.Decondin")
    print("3. Brute-force(CTF-mode)")
choice = input("\nChoose an option (1/2/3): ").strip()
if choice == "1":
        text = input("Enter text to encode: ")
        shift = int(input("Enter shift (0-25): "))
        print(f"\nEncoded: {caesar(text, shift)}")
 
elif choice == "2":
        text = input("Enter text to decode: ")
        shift = int(input("Enter shift (0-25): "))
        print(f"\nDecoded: {caesar(text, -shift)}")
 
elif choice == "3":
        text = input("Enter ciphertext to brute-force: ")
        brute_force(text)
 
else:
        print("Invalid option.")
 
 
if __name__ == "__main__":
    main()
