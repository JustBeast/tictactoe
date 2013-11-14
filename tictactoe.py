lt = " "
t  = " "
rt = " "
l  = " "
c  = " "
r  = " "
lb = " "
b  = " "
rb = " "

# The current player playing the game
current = "X"
# Whether or not someone has one
someonewon = False
pieces = 0

while not someonewon:
	# Prints out the board	
	print " " +lt + " | " + t + " | " + rt 
	print "---+-----+----"
	print " " + l + " | "+ c + " | " + r    
	print "---+-----+----"
	print " " + lb + " | " + b + " | " + rb
	print " It is " + current + " s' turn. "

	# Get next to place piece
	row = input (" Enter a row: ")
	column = input ("Enter a column: ")

	while row > 3 or row < 1 or column > 3 or column < 1:
		print "Not a valid location"
		row = input( " Enter a real row: ")
		column = input ( " Enter a real column:  ")


	# Check which variable to change
	if row == 1 and column  == 1:
		lt = current
	if row == 1 and column == 2:
		t = current
	if row == 1 and column == 3:
		rt = current
	if row == 2 and column == 1:
		l = current
	if row == 2 and column == 2:
		c = current
	if row == 2 and column == 3:
		l = current
	if row == 3 and column == 1:
		lb = current 
	if row == 3 and column == 2:
		b = current 
	if row == 3 and column == 3:
		rb = current 

	# Switch current to be the 
	if current == "X":
		current = "O"
	else: 
		current = "X"
		#check if someone has one the game
	if lt == t == rt and lt != " ":
		someonewon = True
    if lt == c == rb and lt != " ":
    	someonewon = True
    if lt == c == rb
    	someonewon = True




   
print "Someone Won!" 






g


