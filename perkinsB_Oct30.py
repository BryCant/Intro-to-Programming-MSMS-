# make a loop that prints "Operation" 10 times. Make the number of times the loop runs a variable that can be changed.
# inside the loop, print the first n digits of the Fibonacci sequence (1,1,2,3,5,7,12, …)
# now give your users a choice allow them to generate a fibonacci sequence OR
# they can generate a square number sequence (0, 1, 4, 9, 16, …)

flag = 0
chosen_topic = int(input("Sequences: [0] Fibonacci  [1] N-Squared \nChoose your favorite sequence: "))
final_n = int(input("How many digits into the chosen sequence: "))
curr_n, prev_n1, prev_n2 = 1, 1, 0

print(prev_n2 if (chosen_topic == 0) else '-----------------')
while flag < (final_n if chosen_topic == 1 else (final_n - 1)):
    if chosen_topic == 0:
        print(curr_n)
        curr_n = prev_n1 + prev_n2
        prev_n2 = prev_n1
        prev_n1 = curr_n
    elif chosen_topic == 1:
        print(flag**2)
    flag += 1

