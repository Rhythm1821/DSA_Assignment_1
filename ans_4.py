def plusOne(digits):
    carry = 1  
    
    for i in range(len(digits)-1, -1, -1):
        digits[i] += carry  
        carry = digits[i] // 10  
        digits[i] %= 10  
    
    if carry:
        digits.insert(0, carry)  
    
    return digits
print(plusOne([1,2,3]))