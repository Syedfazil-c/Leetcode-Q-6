digits =[1,2,3]
def pusone(digits):
    for i in range(len(digits)):
        if digits[i] <9:
            digits[i]+=1
            return digits
        digits[i]=0
    return [1]+digits
print(oneplus(digits))