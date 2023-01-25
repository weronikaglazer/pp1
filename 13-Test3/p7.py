class C:
    @staticmethod
    def m1(n):
        new_number = ""
        for digit in str(n):
            if (digit % 2 == 0):
                new_number += digit
        return new_number
    
    @staticmethod
    def m2(n):
        previous = None
        for digit in str(n):
            if digit < previous:
                return False
            else:
                previous = digit
        return True
    

    @staticmethod
    def m3(n):
        digits = ["0","1","2","3","4","5","6","7","8","9"]
        
        for digit in str(n):
            if (digit in digits):
                digits.remove(digit)
        
        missing = "".join(digits)
        return missing
    

