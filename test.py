def test(num):
    a = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    b = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen",
    "Sixteen","Seventeen","Eighteen","Nineteen"]
    c = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    if num >= 0 and num < 10:
        return a[num]
    elif num >= 10 and num < 20:
        return b[num-10]
    elif num >= 20 and num < 100:
        if num % 10 == 0:   # agar 10 ka multiple hai
            return c[num//10]
        else:
            return c[num//10] + " " + a[num%10]
    elif num >= 100 and num < 1000:
        if num % 100 == 0: # sirf hundred
            return a[num//100] + " hundred"
        else:
            return a[num//100] + " hundred and " + test(num % 100)
    else:
        return "ye code 1000 se upar kaam nai karega"


num = int(input("enter a number: "))
print(test(num))



























# # def test(num):
# #     if num==7:
# #         print("seven")
# #     else:
# #         print("wrong number")
# # a=int(input("Enter a Number: "))
# def test(num):
#     trans = {
#         '0': 'zero', '1': 'one', '2': 'two', '3': 'three',
#         '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten'
#     }
#     result = ' '.join(trans[d] for d in num)
#     print(result)
#
#
# num = input("Enter a number: ")
# test(num)
#
#
#
#
#
#
#



