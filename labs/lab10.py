# Luhn Algorithm / Mod 10 ALgorithm
def verify_card_number(card_number):
    card_number = card_number.replace("-","")
    card_number = card_number.replace(" ","")
    digits = []
    for digit in card_number:
        digits.append(int(digit))
    
    total =0
    
    for i in range(len(digits)-1,-1,-1):
        digit = digits[i]
        if (len(digits)-i)%2==0:
            digit *= 2
                
            if digit>9:
                digit -=9
        total += digit

    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"
    
