input_data = [[321, 465], [3213, 254],[315, 547]]


#cycle throught array, chooses min of two, creates array then maps array to string
data = " ".join(map(str, (list(min(i) for i in input_data))))

print(data)
