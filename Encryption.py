from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

def RSA_encryption(public_key_filename):
    #data to encypt
    file_in = open("message.txt", "r")
    data = file_in.read().encode("utf-8")
    file_in.close()

    # Gets keys
    recipient_key = RSA.import_key(open(public_key_filename).read())
    session_key = get_random_bytes(16)

    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)

    #Writes Data to File
    file_out = open("encrypted_message.bin", "wb")
    [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
    file_out.close()

if __name__ == '__main__':
    RSA_encryption("public_key_1.pem")
    print("Done")
