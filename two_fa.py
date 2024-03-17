import time
import pyotp
import qrcode

#random keys
key = pyotp.random_base32() 

print(key)


# time based 2fa (refresh like every 30s)
key = "EclipseAdityaIsMySuperSecretKey"

totp = pyotp.TOTP(key)
print(totp.now())


input_code = input("Enter 2FA Code:")
print(totp.verify(input_code))


#using Hotp //uses counter values for key generation
key = "EclipseAdityaIsMySuperSecretKey"
hotp = pyotp.HOTP(key)
counter = 0
print(hotp.at(0))
print(hotp.at(1))
print(hotp.at(2))
print(hotp.at(3))
print(hotp.at(4))

for hotps in range(5):
    print(hotp.verify(input("Enter Code: "),counter))
    counter +=1


# authenticator based 2fa
key = "EclipseAdityaIsMySuperSecretKey"
uri = pyotp.totp.TOTP(key).provisioning_uri(name = "Aditya",
                                            issuer_name="Eclipse Aditya")

print(uri)

qrcode.make(uri).save("totp.jpeg")

totp = pyotp.TOTP(key)
while True:
    print(totp.verify(input("Enter code: ")))
