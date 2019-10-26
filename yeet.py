
#This is because this isnt read  fromthe file yet! so need to append first!
w ="Breakfrom1line000"
x ="web"
y ="user"
z ="pass"
with open('storefile.json') as fii:
	lines =[line.rstrip('\n') for line in fii.readlines()] # to not get empty space

lines.append(w)
lines.append(x)
lines.append(y)
lines.append(z)
for line in lines:
 if line == "Breakfrom1line000":
 	counter = 0
 if line != "Breakfrom1line000":
	 print(line)
	 if counter == 2:
	 	print("___________________________________") # add line :D
	 counter = counter +1
 
	 
print len(lines)
print counter

#if counter == certain number add button!!!!!!!
### add line after each username and password!
	 
