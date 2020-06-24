from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

def test(trapdoor):
    #Read encrypted message
    file_in = open("encrypted_message.bin", "rb")
    private_key = RSA.import_key(open(trapdoor).read())

    enc_session_key, nonce, tag, ciphertext = \
       [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]
    file_in.close()

    # Test Data
    cipher_rsa = PKCS1_OAEP.new(private_key)

    try:
        #output yes on correct key
        cipher_rsa.decrypt(enc_session_key)
        print("Yes.")
    except:
        #else no
        print("No.")

if __name__ == '__main__':
    test("private_key_1.pem")
    print("Done")
