def validate_pin(pin):
    compte = 0
    
    if all(e.isdigit()):
            if compte == 4 or compte == 6:
                return True
            else:
                return False
        
print(validate_pin("1"))