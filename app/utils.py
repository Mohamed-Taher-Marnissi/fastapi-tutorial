from passlib.context import CryptContext

# telling pass What is the default hashing algorithm => Here bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password , hashed_password):
    return pwd_context.verify(plain_password , hashed_password)

