import random 

class RubikCube: 
    def __init__(self, size): 
        self.size= size 
        self.cube={
            "Front" : [['R' for i in range(size)] for i in range(size)], # Front = Red
            "Back" : [['B' for i in range(size)] for i in range(size)], # Back= Blue
            "Left" : [['O' for i in range(size)] for i in range(size)], #Left= Orange
            "Right" : [['W' for i in range(size)] for i in range(size)], #Right= White
            "Up" : [['Y' for i in range(size)] for i in range(size)],   #Up = Yellow
            "Down" : [['G' for i in range(size)] for i in range(size)], #Down = Green
           
        }

    def display(self):
        for face in self.cube:
            print(f"{face} face:")
            for row in self.cube[face]:
                print(' '.join(row))
            print() 

    def rotate_face_clockwise(self, face):
        self.cube[face] = [list(row) for row in zip(*self.cube[face][::-1])]

    def rotate_face_anticlockwise(self, face):
        self.cube[face] = [list(row) for row in zip(*self.cube[face])][::-1]


    def turn_row_right(self, row):
        if row < 0 or row >= self.size:
            raise ValueError("Invalid row number")

        # Rotate rows of Front, Left, Back, Right faces
        front_row = self.cube["Front"][row]
        left_row = self.cube["Left"][row]
        back_row = self.cube["Back"][row]
        right_row = self.cube["Right"][row]

        # Perform the row shift
        self.cube["Front"][row] = left_row
        self.cube["Left"][row] = back_row
        self.cube["Back"][row] = right_row
        self.cube["Right"][row] = front_row

        # Rotate top or bottom face if necessary
        if row == 0:
            self.rotate_face_anticlockwise("Up")
        elif row == self.size - 1:
            self.rotate_face_clockwise("Down")
    
    def turn_row_left(self, row):
        if row < 0 or row >= self.size:
            raise ValueError("Invalid row number")

        #  Rotate rows of Front, Left, Back, Right faces
        front_row = self.cube["Front"][row]
        left_row = self.cube["Left"][row]
        back_row = self.cube["Back"][row]
        right_row = self.cube["Right"][row]

        # Perform the row shift in reverse direction
        self.cube["Front"][row] = right_row
        self.cube["Left"][row] = front_row
        self.cube["Back"][row] = left_row
        self.cube["Right"][row] = back_row

        # Rotate top or bottom face if necessary
        if row == 0:
            self.rotate_face_clockwise("Up")
        elif row == self.size - 1:
            self.rotate_face_anticlockwise("Down")

    def turn_column_up(self, col):
        if col < 0 or col >= self.size:
            raise ValueError("Invalid column number")

        # Rotate columns of Front, Down, Back, Up faces
        front_col = [self.cube["Front"][i][col] for i in range(self.size)]
        down_col = [self.cube["Down"][i][col] for i in range(self.size)]
        back_col = [self.cube["Back"][i][col] for i in range(self.size)]
        up_col = [self.cube["Up"][i][col] for i in range(self.size)]

        # Perform the column shift upwards
        for i in range(self.size):
            self.cube["Front"][i][col] = down_col[i]
            self.cube["Down"][i][col] = back_col[i]
            self.cube["Back"][i][col] = up_col[self.size - 1 - i]  # Reverse direction for back face
            self.cube["Up"][i][col] = front_col[i]

        # Rotate Left or Right face if necessary
        if col == 0:
            self.rotate_face_anticlockwise("Left")
        elif col == self.size - 1:
            self.rotate_face_clockwise("Right")

    def turn_column_down(self, col):
        if col < 0 or col >= self.size:
            raise ValueError("Invalid column number")

        #  Rotate columns of Front, Down, Back, Up faces
        front_col = [self.cube["Front"][i][col] for i in range(self.size)]
        down_col = [self.cube["Down"][i][col] for i in range(self.size)]
        back_col = [self.cube["Back"][i][col] for i in range(self.size)]
        up_col = [self.cube["Up"][i][col] for i in range(self.size)]

        # Perform the column shift downwards
        for i in range(self.size):
            self.cube["Front"][i][col] = up_col[i]
            self.cube["Down"][i][col] = front_col[i]
            self.cube["Back"][i][col] = down_col[self.size - 1 - i]  # Reverse direction for back face
            self.cube["Up"][i][col] = back_col[i]

        #  Rotate Left or Right face if necessary
        if col == 0:
            self.rotate_face_clockwise("Left")
        elif col == self.size - 1:
            self.rotate_face_anticlockwise("Right")

    def scrambler(self, moves=20):
        for _ in range(moves):
            # Randomly choose between row or column turn
            if random.choice(['row', 'column']) == 'row':
                row = random.randint(0, self.size - 1)
                direction = random.choice(['left', 'right'])
                if direction == 'left':
                    self.turn_row_left(row)
                else:
                    self.turn_row_right(row)
            else:
                col = random.randint(0, self.size - 1)
                direction = random.choice(['up', 'down'])
                if direction == 'up':
                    self.turn_column_up(col)
                else:
                    self.turn_column_down(col)

   

    

cube = RubikCube(3)
cube.display()

print("After scrambiling function")
cube.scrambler(moves=20)
cube.display()

