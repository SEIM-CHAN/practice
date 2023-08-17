from random import sample


sample_list = list(range(5))
def multi(x):
    y = x * 2
    return y

sample2_list = map(multi, sample_list)
print(list(sample2_list))

