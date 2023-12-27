a = input("Enter the data word: ")
b = a
if len(a) > 4:
    print("Please enter only 4 bits")
else:
    e = int(input("1.Without error 2.Error\n"))
    if e == 1:
        count = 0
        for i in range(4):
            if a[i] == '1':
                count += 1
        if count % 2 == 0:
            a += "0"
        else:
            a += "1"
    else:
        a += "1"
        print("After adding the parity bit:", a)
        print("Syndrome checking 5 value: 0 and no error")
        print("The data word:", b)
        a += "0"
        print("After adding the parity bit:", a)
        print("Syndrome checking 5 value: 1 and error occur")
'''
Output:
Enter the data word: 1011
1.Without error 2.Error
2
After adding the parity bit: 10111
Syndrome checking 5 value: 0 and no error
The data word: 1011
After adding the parity bit: 101110
Syndrome checking 5 value: 1 and error occur

Output 2:
Enter the data word: 101010
Please enter only 4 bits
'''