from werkzeug.security import generate_password_hash, check_password_hash

def hashing_password(password):
    hashedPassword = generate_password_hash(password, method='pbkdf2:sha256')

    return hashedPassword


def cheching_password(userPassword, reqPassword):
    if check_password_hash(userPassword, reqPassword):
        return True
    
    else:
        return False