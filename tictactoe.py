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
        print "---+---+----"
        print " " + l + " | "+ c + " | " + r    
        print "---+---+----"
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
        if row == 1 and column  == 1 and lt == " ":
                lt = current
        if row == 1 and column == 2 and t == " ":
                t = current
        if row == 1 and column == 3 and rt == " ":
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
                #check if someone has won the game
        if lt == t == rt and lt != " ":
          someonewon = True
        if lt == c == rb and lt != " ":
          someonewon = True
        if lt == c == rb and lt != " ":
          someonewon = True
        if lt == l == lb and lt != " ":
          someonewon = True
        if t == c == b and t != " ":
          someonewon = True
        if rt == c == lb and rt != " ":
          someonewon = True
        if rt == r == rb and rt != " ":
          someonewon = True
        if lb == b == rb and lb != " ":
          someonewon = True
        if l == c == r and l != " ":
          someonewon = True



        if lt != " ":
            validsquare = False
            print "Cozener"
            row = input( " Enter a conscientious row: ")
            column = input ( " Enter a conscientious column: ")
        if t != " ":
            validsquare = False
            print "Cozener"
            row = input( " Enter a conscientious row: ")
            column = input ( " Enter a conscientious column: ")
        if rt != " ":
            validsquare = False
            print "Cozener"
            row = input( " Enter a conscientious row: ")
            column = input ( " Enter a conscientious column: ")
        if r != " ":
            validsquare = False
            print "Cozener"
            row = input( " Enter a conscientious row: ")
            column = input ( " Enter a conscientious column: ")
        if c != " ":
            validsquare = False
            print "Cozener"
            row = input( " Enter a conscientious row: ")
            column = input ( " Enter a conscientious column: ")
        if l != " ":
            validsquare = False
            print "Cozener"
            row = input( " Enter a conscientious row: ")
            column = input ( " Enter a conscientious column: ")
        if lb != " ":
            validsquare = False
            print "Cozener"
            row = input( " Enter a conscientious row: ")
            column = input ( " Enter a conscientious column: ")
        
        if b != " ":
            validsquare = False
            print "Cozener"
            row = input( " Enter a conscientious row: ")
            column = input ( " Enter a conscientious column: ")
        if rb != " ":
            validsquare = False
            print "Cozener"
            row = input( " Enter a conscientious row: ")
            column = input ( " Enter a conscientious column: ")
        
        
        
        
        
        
        
        

        
    


