# State	Literacy Rate	State	Literacy Rate
# Kerala	94.0%	Delhi	86.2%
# Chandigarh	86.0%	Himachal Pradesh	82.8%
# Maharashtra	82.3%	Tamil Nadu	80.1%
# Uttarakhand	78.8%	Gujrat	78.0%
# West Bengal	76.3%	Punjab	75.8%
# Haryana	75.6%	Karnataka	75.4%
# Meghalaya	74.4%	Chhattisgarh	70.3%
# Madhya Pradesh	69.3%	Uttar Pradesh	67.7%
# Jammu and Kashmir	67.2%	Andhra Pradesh	67.0%
# Jharkhand	66.4%	Rajasthan	66.1%
# Bihar	61.8%

import matplotlib.pyplot as plots
xaxis = ["Kerala","Delhi","Chandigarh"]
yaxis = [94.0,86.2,82.8]
plots.plot(xaxis,yaxis)
plots.xlabel("State Names")
plots.ylabel("Literacy Count in %")
plots.title("Literacy Rate in India")
plots.show()
