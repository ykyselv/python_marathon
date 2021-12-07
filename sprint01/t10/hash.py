import hashlib

def md5_hash(mystring):
    hash_obj = hashlib.md5(mystring.encode())
    print(f"Original string: {mystring}\nmd5 hash generated is\n{hash_obj.hexdigest()}")

def sha1_hash(mystring):
    hash_object = hashlib.sha1(mystring.encode())
    print(f"Original string: {mystring}\nmd5 hash generated is\n{hash_object.hexdigest()}")

# md5_hash('My hovercraft is full of eels')
# sha1_hash('My hovercraft is full of eels')
