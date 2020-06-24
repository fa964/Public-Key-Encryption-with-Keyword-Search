import KeyGen
import Encryption
import Decryption
import Test


if __name__ == '__main__':

    '''
    #remove comments to run key gen
    #Generate public/private key pair for each word in dictionary'''
    KeyGen.key_gen()
    

    #encrypt message with public key
    public_key_filename = "public_key_1.pem"
    Encryption.RSA_encryption(public_key_filename)

    #trapdoor is private key
    trapdoor = "private_key_1.pem"

    #test for specific word/private key
    Test.test(trapdoor)

    '''
    #decrypt for message
    private_key_filename = "private_key_1.pem"
    Decryption.RSA_decryption(private_key_filename)
    '''
