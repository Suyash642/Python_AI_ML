# Program for displaying details and calculating total marks and percentage

#declaring firstname and lastname
firstname = "Suyash "
lastname = "Bidkar"

#Concatenating firstname and lastname to display fullname
fullname = firstname + lastname

#display fullname
print("Fullname: {} \n".format(fullname))

#declaring clgname and clgaddress
clgname = "YCCE "
clgaddress = "Wanadongri, Hingna"

#concatenating clgname and clgaddress 
college = clgname + clgaddress

#displaying college
print("College:- {}\n".format(college))

#declaring 5 different subjects marks
sub1_marks = 80
sub2_marks = 85
sub3_marks = 90
sub4_marks = 87
sub5_marks = 95

#calculate total marks and percentage
total_marks = sub1_marks+ sub2_marks+ sub3_marks+ sub4_marks+ sub5_marks
percentage = (total_marks/500)*100

#display total_marks and percentage
print("Total Marks Obtained: {} from 500 \nPercentage: {}%".format(total_marks, percentage))
