import matplotlib.pyplot as plots

x = [10, 22, 15, 36,12]
sorted_list = sorted(x)
plots.plot([1,2,3,4,5],sorted_list)

plots.title("Sample Chart")
plots.ylabel("Count")
plots.xlabel("Events")
plots.show()

