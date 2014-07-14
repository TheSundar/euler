# function modular_pow(base, exponent, modulus)
#     Assert :: (modulus - 1) * (base mod modulus) does not overflow base
#     result := 1
#     base := base mod modulus
#     while exponent > 0
#         if (exponent mod 2 == 1):
#            result := (result * base) mod modulus
#         exponent := exponent >> 1
#         base := (base * base) mod modulus
#     return result

def modular_pow(base,exponent,modules):
    if base >=(modules - 1) * (base % modules):
        result=1
        base=base % modules
        while exponent>0:
            if exponent %2 ==1:
                result=(result*base)%modules
            exponent = exponent >> 1
            base=(base*base) % modules
        return result