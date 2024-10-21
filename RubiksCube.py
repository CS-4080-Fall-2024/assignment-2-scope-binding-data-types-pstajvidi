import random 
import kociemba
from collections import Counter 
class RubikCube: 
    def __init__(self, size): 
        self.size= size 
        self.cube={
            "Front" : [['R' for i in range(size)] for i in range(size)], # Front = Red
            "Back" : [['B' for i in range(size)] for i in range(size)], # Back= Blue
            "Up" : [['Y' for i in range(size)] for i in range(size)],   #Up = Yellow
            "Down" : [['G' for i in range(size)] for i in range(size)], #Down = Green
            "Left" : [['O' for i in range(size)] for i in range(size)], #Left= Orange
            "Right" : [['W' for i in range(size)] for i in range(size)], #Right= White
        }


    """
        
         *        +-------+
         *        |Yellow | 
         *        |   U   |
         * +------+-------+-------+-------+
         * |Oreng | Red   | White |  Blue |
         * |  L   |   F   |   R   |   B   | 
         * +------+-------+-------+-------+
         *        | Green |
         *        |  D    |
         *        +-------+
         
         
        """


    def rotate_face_clockwise(self, face):
        self.cube[face] = [list(reversed(col)) for col in zip(*self.cube[face])]
    
    def rotate_face_counterclock(self,face):
         self.cube[face] = [list(col) for col in zip(*reversed(self.cube[face]))]

    
    def rotate_front_face_clockwise(self):
        self.rotate_face_clockwise("Front")
        temp_row = self.cube["Up"][-1]

        self.cube["Up"][-1] = [self.cube["Left"][-1-i][-1] for i in range(self.size)]
        
        for i in range(self.size):
            self.cube["Left"][-1-i][-1] = self.cube["Down"][0][i]
        
        self.cube["Down"][0] = [self.cube["Right"][i][0] for i in range(self.size)]
        for i in range(self.size):
            self.cube["Right"][i][0] = temp_row[i]
 
    def rotate_front_face_counter_clockwise(self):
        self.rotate_face_counterclock("Front")
        temp_row = self.cube["Up"][-1]
        self.cube["Up"][-1] = [self.cube["Right"][i][0] for i in range(self.size)]
        for i in range(self.size):
            self.cube["Right"][i][0] = self.cube["Down"][0][i]
        self.cube["Down"][0] = [self.cube["Left"][-1-i][-1] for i in range(self.size)]
        for i in range(self.size):
            self.cube["Left"][-1-i][-1] = temp_row[i]
    
    def rotate_back_face_clockwise(self):
        self.rotate_face_clockwise("Back")
        temp_row = self.cube["Up"][0]
        self.cube["Up"][0] = [self.cube["Right"][i][-1] for i in range(self.size)]
        for i in range(self.size):
            self.cube["Right"][i][-1] = self.cube["Down"][-1][self.size-1-i]
        self.cube["Down"][-1] = [self.cube["Left"][-1-i][0] for i in range(self.size)]
        for i in range(self.size):
            self.cube["Left"][-1-i][0] = temp_row[i]
    
    def rotate_back_face_counter_clockwise(self):
        self.rotate_face_counterclock("Back")
        temp_row = self.cube["Up"][0]
        self.cube["Up"][0] = [self.cube["Left"][-1-i][0] for i in range(self.size)]
        for i in range(self.size):
            self.cube["Left"][-1-i][0] = self.cube["Down"][-1][i]
        self.cube["Down"][-1] = [self.cube["Right"][i][-1] for i in range(self.size)]
        for i in range(self.size):
            self.cube["Right"][i][-1] = temp_row[i]

    def rotate_up_face_clockwise(self):
        self.rotate_face_clockwise("Up")
        temp_row = self.cube["Front"][0]
        self.cube["Front"][0] = self.cube["Left"][0][::-1]  # Left row needs to be reversed
        self.cube["Left"][0] = self.cube["Back"][0]   
        self.cube["Back"][0] = self.cube["Right"][0]
        self.cube["Right"][0] = temp_row

    def rotate_up_face_counter_clockwise(self):
        self.rotate_face_counterclock("Up")
        temp_row = self.cube["Front"][0]
        self.cube["Front"][0] = self.cube["Left"][0]
        self.cube["Left"][0] = self.cube["Back"][0]
        self.cube["Back"][0] = self.cube["Right"][0]
        self.cube["Right"][0] = temp_row

    def rotate_down_face_clockwise(self):
        self.rotate_face_clockwise("Down") 
        initial = self.cube["Front"][-1] 
        self.cube["Front"][-1] = self.cube["Left"][-1]
        self.cube["Left"][-1] = self.cube["Back"][-1]
        self.cube["Back"][-1] = self.cube["Right"][-1]
        self.cube["Right"][-1] = initial

    def rotate_down_face_counter_clockwise(self):
        self.rotate_face_counterclock("Down")
        temp_row = self.cube["Front"][-1]
        self.cube["Front"][-1] = self.cube["Right"][-1]
        self.cube["Right"][-1] = self.cube["Back"][-1]
        self.cube["Back"][-1] = self.cube["Left"][-1]
        self.cube["Left"][-1] = temp_row

    def rotate_left_face_clockwise(self):
        self.rotate_face_clockwise("Left")
        temp_col = [self.cube["Up"][i][0] for i in range(self.size)]
        for i in range(self.size):
            self.cube["Up"][i][0] = self.cube["Back"][-1-i][self.size-1]
            self.cube["Back"][-1-i][self.size-1] = self.cube["Down"][i][0]
            self.cube["Down"][i][0] = self.cube["Front"][i][0]
            self.cube["Front"][i][0] = temp_col[i]

    def rotate_left_face_counter_clockwise(self):
        self.rotate_face_counterclock("Left")
        temp_col = [self.cube["Up"][i][0] for i in range(self.size)]
        for i in range(self.size):
            self.cube["Up"][i][0] = self.cube["Front"][i][0]
            self.cube["Front"][i][0] = self.cube["Down"][i][0]
            self.cube["Down"][i][0] = self.cube["Back"][-1-i][self.size-1]
            self.cube["Back"][-1-i][self.size-1] = temp_col[i]

    def rotate_layer_clockwise(self, layer):
        temp_row = self.cube["Front"][layer]
        self.cube["Front"][layer] = self.cube["Left"][layer]
        self.cube["Left"][layer] = self.cube["Back"][layer][::-1]
        self.cube["Back"][layer] = self.cube["Right"][layer][::-1]
        self.cube["Right"][layer] = temp_row

    def rotate_layer_counter_clockwise(self, layer):
        temp_row = self.cube["Front"][layer]
        self.cube["Front"][layer] = self.cube["Right"][layer]
        self.cube["Right"][layer] = self.cube["Back"][layer][::-1]
        self.cube["Back"][layer] = self.cube["Left"][layer][::-1]
        self.cube["Left"][layer] = temp_row

    def rotate_column_up(self, column):
        temp_col = [self.cube["Front"][i][column] for i in range(self.size)]
        for i in range(self.size):
            self.cube["Front"][i][column] = self.cube["Down"][i][column]
        for i in range(self.size):
            self.cube["Down"][i][column] = self.cube["Back"][-1-i][column]
        for i in range(self.size):
            self.cube["Back"][-1-i][column] = self.cube["Up"][i][column]
        for i in range(self.size):
            self.cube["Up"][i][column] = temp_col[i]
            
    def rotate_column_down(self, column):
        temp_col = [self.cube["Front"][i][column] for i in range(self.size)]
        for i in range(self.size):
            self.cube["Front"][i][column] = self.cube["Up"][i][column]
        for i in range(self.size):
            self.cube["Up"][i][column] = self.cube["Back"][-1-i][column]
        for i in range(self.size):
            self.cube["Back"][-1-i][column] = self.cube["Down"][i][column]
        for i in range(self.size):
            self.cube["Down"][i][column] = temp_col[i]
            
    def display(self):
        # Display the cube state for each face
        for face in self.cube:
            print(f"{face} face:")
            for row in self.cube[face]:
                print(' '.join(row))
            print()  # Blank line after each face

    def scramble(self, rotations):
        possible_moves = [
            self.rotate_front_face_clockwise,
            self.rotate_front_face_counter_clockwise,
            self.rotate_back_face_clockwise,
            self.rotate_back_face_counter_clockwise,
            self.rotate_up_face_clockwise,
            self.rotate_up_face_counter_clockwise,
            self.rotate_down_face_clockwise,
            self.rotate_down_face_counter_clockwise,
            self.rotate_left_face_clockwise,
            self.rotate_left_face_counter_clockwise,
            self.rotate_column_up,
            self.rotate_column_down,
        ]
        
        # Perform `rotations` number of random moves
        for _ in range(rotations):
            move = random.choice(possible_moves)  # Choose a random move
            if move in [self.rotate_column_up, self.rotate_column_down]:
                column = random.randint(0, self.size - 1)  # Select a random column for column moves
                move(column)
            else:
                move()  # Regular face rotations

    

cube = RubikCube(3)
cube.rotate_column_down(2)
cube.display()
print("post rotation")
cube.rotate_back_face_clockwise()
cube.display()

print("/// scramble")
cube.scramble(30)
cube.display()
