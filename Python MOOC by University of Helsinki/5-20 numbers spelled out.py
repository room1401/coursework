'''
Please write a function named dict_of_numbers(), which returns a new dictionary. 
The dictionary should have the numbers from 0 to 99 as its keys. 
The value attached to each key should be the number spelled out in words. 
Please don't formulate each spelled out number by hand.
Figure out how you can use loops and dictionaries in your solution.
'''

# Write your solution here
def dict_of_numbers():
    ones = [
        '', 'one', 'two', 'three','four', 
        'five', 'six','seven', 'eight', 'nine', 
        'ten', 'eleven', 'twelve', 'thirteen', 
        'fourteen', 'fifteen', 'sixteen', 
        'seventeen', 'eighteen', 'nineteen']

    tens = [
        'twenty', 'thirty', 'forty', 'fifty', 
        'sixty', 'seventy', 'eighty', 'ninety']

    dic = {0: 'zero'}

    for i in range(1, 20):
        dic[i] = ones[i]
        
    for i in range(20, 100):
        one = "-" + ones[i % 10] if i % 10 else ""
        dic[i] = tens[i // 10 - 2] + one

    return dic

if __name__ == "__main__":
    dict_of_numbers()
