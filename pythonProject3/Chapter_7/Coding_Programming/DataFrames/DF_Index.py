# import pandas as pa
# simple_lst_pop= pa.Series([234733,348345,6789043,5678934], index=['Assam','Bihar','Karnataka','Andhra'])
# simple_lst_lit= pa.Series([65,67.43,78,89], index=['Assam','Bihar','Karnataka','Andhra'])
# data = {'Population':simple_lst_pop,'Literacy':simple_lst_lit}
# my_frame = pa.DataFrame(data)
# print(my_frame)
#
# my_frame.index = ["USA","India","Japan","Germany"]
# print(my_frame)

import pandas as pa
simple_lst_pop= pa.Series([234733,348345,6789043,5678934])
simple_lst_lit= pa.Series([65,67.43,78,89])
data = {'Population':simple_lst_pop,'Literacy':simple_lst_lit}
my_frame = pa.DataFrame(data)
my_frame.index = ["USA","India","Japan","Germany"]
my_frame.columns= ["Income","Age"]
print(my_frame)