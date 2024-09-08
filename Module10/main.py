#import class structured module
from cityu_pack.sub_class_pack.class_module import ClassModule

temp_object = ClassModule(global_init_param=1)
print("global_init_param: ", temp_object.global_init_param)

class_add_answer = temp_object.add(1,2)
print("class_add_answer: ", class_add_answer)

# Class-based multiply function
class_mult_answer = temp_object.multiply(1,2)
print("class_mult_answer: ", class_mult_answer)

# explicit import such as average
from cityu_pack.sub_func_pack.func_module import avg
avg_answer = avg(1,2)
print("\navg_answer: ", avg_answer)

#import all in function structured module
from cityu_pack.sub_func_pack.func_module import *
add_answer = add(1,2)
print("add_answer: ",add_answer)

#import all in function structured module
from cityu_pack.sub_func_pack.func_module import multiply
mult_answer = multiply(1,2)
print("multiply_answer: ",mult_answer)