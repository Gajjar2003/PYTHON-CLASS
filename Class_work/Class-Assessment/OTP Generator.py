import random

def generator_otp(length=4):
    if length  <= 0 :
        raise ValueError("OTP length must be positive. ")
    otp = ''.join([str(random.randint(0,9)) for _ in range(length)])
    return otp

otp = generator_otp()
print("You are OTP : ",otp)