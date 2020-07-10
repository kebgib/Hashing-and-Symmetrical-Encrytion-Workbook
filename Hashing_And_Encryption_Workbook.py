## I&T Webcast: Hashing and Symmetric Encryption -- What Why and How?
## The Python portions of this class are a bonus. The real take-aways here are the concepts behind hashing and encrypting data.
##
##AGENDA:
## 1.	The Python Interactive Development Environment (Python IDLE) 
## https://www.python.org/ 
## Feel free to grab Python 3.8 if you want to follow along, THIS IS NOT REQUIRED for this exercise/meeting
##
## 2.	Assigning variables, calling variables, string encoding and byte code.
##   a.	What is encoding? -- https://www.w3.org/International/questions/qa-what-is-encoding
##   b.	The above reading not required, but informative for modern computing basics for the curious.
##   c.	We will be hashing and encrypting bytecode encoded data
##
## 3.	Hashing data using SHA256 (Secure Hashing Algorithm 256 bit)
##   a.	Main Topics: Hashing in modern computing, password storage, and content integrity. 
##   b.	Examples in Python’s built in hashlib library -  https://docs.python.org/3/library/hashlib.html 
##   c.	BONUS – ‘Cracking’ or reverse engineering hashed values
##
## 4.	Symmetrical Encryption using AES128 –and- SHA256 for message authentication
##   a.	Main Topics: Keys, and examples of failed decryption.
##   b.	Examples in Python’s 3rd party Cryptography library (additional install required) https://cryptography.io/en/latest/ 
##
## 5.	Roundtable/Open Discussion


########ENCODING#########
# https://www.w3.org/International/questions/qa-what-is-encoding

# Python encoding is ASCII by default. 

# Create a bytecode encoded string, signified by the opening 'b' before the actual string
bytecode = b"abcde"
myname = b"Kevin Gibson"
# utf-8 is used here because it is a very common encoding.
bytecode.decode("utf-8") 
myname.decode("utf-8")
# The computer interperets the encoding and displays the text to you accordingly.
# This may seem ephemeral or behind the scenes but is a basic 


##########HASHING#############
##!! Hashlib is the built in library for hashing data within Python.
## https://docs.python.org/3/library/hashlib.html

# Import the hashing library
import hashlib
# What algos are available to us for use?
hashlib.algorithms_available
# Lets hash something using the sha256 method 
hashedpass1 = hashlib.sha256(b"MySecretPassword123!$").hexdigest()
# Let's hash another
kevins_password = hashlib.sha256(b"MySecretPassword123!$").hexdigest()
# Lets compare these two hashes. Are they equal and the same?
hashedpass1 == kevins_password
# A 3rd hashed password
hashedpass2 = hashlib.sha256(b"MySecretPassword").hexdigest()
# Does this equal our 1st hash? Why not?
hashedpass1 == hashedpass2


######### "CRACKING" A HASHED PASSWORD... #############
##!! Cracking a hash using a word list/password list. 
##!! This is time consuming and increases with time/computing power based on the complexity of passwords
##!! Simple passwords will be cracked in minutes using a simple wordlist and permeutation combos
##!! ie. Password, Password0, Password1, Password2, Password3 ..... Password902138.

# This is my list of passwords to attempt
password_list = [b"MySecretPassword123!$", b"MyKitty222", b"June2019@!", b"password", b"admin_root"]

# for each item in my list, do something
for password in password_list:
	print(password)

# Lets hash each password in password_list and compare its hash to hashedpass1
# This is how hackers will 'reverse engineer' stolen password hashes to find actual passwords
for password_to_test in password_list:
	test_hash = hashlib.sha256(password_to_test).hexdigest()
	if test_hash == hashedpass1: 
		print("Hash Cracked!")
		print(password_to_test) 
		print(hashedpass1)



########ENCRYPTION###############
##!! This is an encryption library that requires installation outside of python 
## Fernet is built on top of a number of standard cryptographic primitives. Specifically it uses:
##
## AES in CBC mode with a 128-bit key for encryption; using PKCS7 padding.
## HMAC using SHA256 for authentication.
## Initialization vectors are generated using os.urandom().
## https://cryptography.io/en/latest/

# Import the Cryptography library
from cryptography.fernet import Fernet
# My 1st encryption key
key1 = Fernet.generate_key()
# My 2nd encryption key
key2 = Fernet.generate_key()
# Let's encrypt this message! 
message = Fernet(key1).encrypt(b"A really secret message. Not for prying eyes.")
# Now that we have it encrypted, lets decrypt it and see its contents
Fernet(key1).decrypt(message)
# this works!
Fernet(key2).decrypt(message)
# this FAILS due to message hash digest mismatch. Fernet uses SHA256 for message authentication.
