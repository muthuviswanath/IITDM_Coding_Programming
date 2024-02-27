import matplotlib.pyplot as plots
events = ["Coding", "Art on the Wall","Singing","Quiz","Skit/Drama"]
counts= [12,23,20,15,40]
plots.figure(figsize=(15,6))
plots.xticks(rotation="vertical",size=10)
plots.bar(events,counts)
plots.title("Participants")
plots.xlabel("Event Names")
plots.ylabel("Participants Count")
plots.show()