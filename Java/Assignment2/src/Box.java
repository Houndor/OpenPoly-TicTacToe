/**
 * The Box class models each individual box of the Grid
 */
public class Box {

   Player content;			// The move this box holds (Empty, X, or O)
   int row, col; 			// Row and column of this box (Not currently used but possibly useful in future updates)
 
   /**
    * Constructor
    */
   public Box(int row, int col) {
	   
	   this.row = 0;
	   this.col = 0;
	   clear();  
   }
 
   /**
    * Clear the box content to EMPTY
    */
   public void clear() {
	   
	   content = Player.EMPTY;	   
   }
 
   /**
    * Display the content of the box
    */
   public void display() {
	   
	   switch(content) {
	   case X: {
		   System.out.print(" X ");
	   }
	   case O: {
		   System.out.print(" O ");
	   }
	   case EMPTY: {
		   System.out.print("   ");
	   }
	   
 	   }

   }
}