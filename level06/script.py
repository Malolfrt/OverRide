def calculate_serial(login):
    login = login.strip()
    length = len(login)
    
    if length <= 5:
        print("Login trop court (> 5 caractères requis)")
        return None
    
    if length > 28:
        login = login[:28]
        length = 28
    
    for c in login:
        if ord(c) <= 31:
            print("Caractères de contrôle interdits")
            return None
    
    hash_val = (ord(login[3]) ^ 0x1337) + 6221293
    
    for i in range(length):
        hash_val += (hash_val ^ ord(login[i])) % 0x539
    
    return hash_val

# Exemple
login = "abcdefgh"
serial = calculate_serial(login)
print(f"Login: {login}")
print(f"Serial: {serial}")