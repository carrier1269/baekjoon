import sys
import time

input = sys.stdin.readline

a = int(input().rstrip())

x, y = 1, 1

count = 2

max_number = 2

pattern_count = 2

temp = True

result = ""

state = True

while(True):
    time.sleep(1)
    if a != 1:
        if temp == True and a != count:
            x, y = 1, max_number
            print(f'x = {x}, y = {y}, co = {count}, temp = {temp}, 홀')


            if a != count:
                print("!!")

                for _ in range(pattern_count - 1):
                    print(f'x = {x}, y = {y}, co = {count}, temp = {temp}, 짝')

                    x += 1
                    y -= 1

                    count += 1


                    if a == count:
                        break

                temp = False

                pattern_count += 1

                max_number += 1
            else:
                break
        elif temp == False and a != count:
            print("error")
            print(f'x = {x}, y = {y}, co = {count}, temp = {temp}, 홀')

            x, y = max_number, 1

            if a != count:

                for _ in range(pattern_count - 1):

                    print(f'x = {x}, y = {y}, co = {count}, temp = {temp}, 홀')

                    count += 1

                    if a == count:
                        break

                    x -= 1
                    y += 1

                    

                    

                    
                temp = True

                pattern_count += 1

                max_number += 1
            else:
                break
        else:
            break

            
    else:
        break

print(f'x = {x}, y = {y}')

result = str(x) + "/" + str(y)
print(result)

