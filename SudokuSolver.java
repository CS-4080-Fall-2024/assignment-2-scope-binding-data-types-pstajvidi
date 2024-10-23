public class SudokuSolver{
    
    public static void main(String[] args){
        char [][] board = { 
            {'5','3','.','.','7','.','.','.','.'},
            {'6','.','.','1','9','5','.','.','.'},
            {'.','9','8','.','.','.','.','6','.'},
            {'8','.','.','.','6','.','.','.','3'},
            {'4','.','.','8','.','3','.','.','1'},
            {'7','.','.','.','2','.','.','.','6'},
            {'.','6','.','.','.','.','2','8','.'},
            {'.','.','.','4','1','9','.','.','5'},
            {'.','.','.','.','8','.','.','7','9'} 
        }; 

        if (solveSudoku(board)) {
            printBoard(board);
        } else {
            System.out.println("No solution exists.");
        }

    }

    /*
     * returns true if it is able to solve the sodoku
     * 
     */
    public static boolean solveSudoku(char [][] board){
        //for each row in the puzzle
        for (int row= 0; row<9; row++){
            //for each col in the puzzle
            for (int col=0; col<9; col++){
                //check if the element is a dot (.) aka empty
                if(board[row][col]=='.'){
                    // if it is, then run threw all the numbers possible in a sodoku
                    for(char num='1'; num<='9'; num++){
                        //check if each number works for the puzzle
                        if (isValidNum(board, row, col, num)) {
                            //if the number is valid, aka it works, 
                            //then add the number to the matrix
                            board[row][col] = num; 
                            //if the entire entire boerd is solved then retunr true
                            if (solveSudoku(board)) {
                                return true; 
                            }
                            
                            board[row][col] = '.'; 
                        }
                    }
                    return false; 
                }
                
            }
        }
        return true; 
    }

    /*
     * check of a number is valid, and works for the puzzle, returns boolean
     */
    public static boolean isValidNum(char [][] board, int row, int col, char num){
        //for each number 0 t9 
        for (int i = 0; i < 9; i++) {
            // Check the row
            if (board[row][i] == num) {
                return false;
            }
            // Check the column
            if (board[i][col] == num) {
                return false;
            }
            // Check the 3x3 subgrid
            if (board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == num) {
                return false;
            }
        }
        return true;
    }

    
    private static void printBoard(char[][] board) {
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                System.out.print(board[row][col] + " ");
            }
            System.out.println();
        }
    }

}

