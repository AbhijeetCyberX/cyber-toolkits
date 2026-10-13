def is_valid_ipv4(ip):
    parts =ip.split(".")
    if len(parts) !=4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if not part.isdigit():
            return False
        if not 0 <= int(part) <= 255:
            return False
        if len(part) >1 and part[0] == "0":
            return False
    return True

def classify_ip(ip):
    octets = [int(x) for x in ip.split(".")]
    first ,second = octets[0] , octets[1]

    if first == 127:
        return "loopback"
    if first == 10:
        return "private (class A)"
    if first == 172 and 16 <= second <= 31:
        return "Private (Class B)"
    if first == 192 and second == 168:
        return "Private (Class C)"
    if first == 169 and second == 254:
        return "Link-Local (APIPA)"
    return "Public"

def main():
    print("=" * 40)
    print("IPv4 Validator & Classifier")
    print("=" * 40)
    print("Type 'quit' to exit\n")
 
    while True:
        ip = input("Enter an IP address: ").strip()
        if ip.lower() == "quit":
            print("Goodbye!")
            break
 
        if is_valid_ipv4(ip):
            category = classify_ip(ip)
            print(f"  [VALID]   {ip}  ->  {category}\n")
        else:
            print(f"  [INVALID] {ip} is not a valid IPv4 address\n")
 
 
if __name__ == "__main__":
    main()
 
