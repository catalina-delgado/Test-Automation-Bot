def es_numero_feliz(number):
    try:

        results = []
        
        #until the sum is 1 or the period does not repeat
        while number != 1 and number not in results:
            results.append(number)
            number = sum(int(digit) ** 2 for digit in str(number))
    
        return number == 1

    except Exception as e:
        print(f"There was an error {e}")


value =  es_numero_feliz(19) 
print(f"Is the number 19 happy? {value}")
value = es_numero_feliz(4)
print(f"Is the number 4 happy? {value}")
