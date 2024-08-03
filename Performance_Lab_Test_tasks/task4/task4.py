import sys

def count_steps_to_average(nums):
    num_list = []
    nums_sum = 0
    counter = 0
    steps_num = 0

    try:
                                   # nums = "task4_nums.txt"
        with open(nums, "r") as f:
            for s in f:
                num_list.append(int(s))
                nums_sum+=int(s)
                counter+=1
            if counter !=0:
                mediana = nums_sum / counter
                mediana = round(mediana)
            for i in num_list:
                steps_num += abs(i-mediana)
            
            return steps_num
    except IndexError:
        print("Input name of the file with numbers!")

print(count_steps_to_average(sys.argv[1]))

