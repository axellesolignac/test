from lib import average, get_median
def class_average_median(lst):
    averages = []
    for sub_list in lst:
        sub_list_average = average(sub_list)
        averages.append(sub_list_average)
    class_average = average(averages)
    class_median = get_median(averages)
    return class_average, class_median

eleve1 = [14,11,12,13]
eleve2 = [10,8,6,17]
eleve3 = [7,5,15]

class_all = [eleve1,eleve2,eleve3]

CA, CM = class_average_median(class_all)
print(CA,CM)