from werkzeug.security import generate_password_hash, check_password_hash

password = input('input youyr password:')

hashed_password = generate_password_hash(password, method='sha256')
print(f'your encoded token: {hashed_password}')

if check_password_hash(hashed_password, password): 
    print(f'password OK')