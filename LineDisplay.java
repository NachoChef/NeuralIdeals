import java.awt.*;
import java.awt.geom.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.awt.image.*;
import javax.imageio.*;
import java.io.*;
import java.io.File;
/**
 * LineDisplay.java
 * The code is based off of 'CONVEX NEURAL CODES IN DIMENSION 1' by ZVI ROSEN, UNIVERSITY OF PENNSYLVANIA, PA
 * and YAN X ZHANG, SAN JOSE STATE UNIVERSITY, CA
 *
 * Purpose: Creates a jpg that displays a one dimensional linear line representation of a neural code
 *
 * Other Contributors: Dr. Luis Garcia, Alex Norma, and Alexander Farrack
 */
class LineDisplay{
	Scanner scan = new Scanner(System.in);
	//initializing the line starting cordinates
	int x = 100;
	int y = 90;
	int[] relArray;
	int yWindow = 140;
	boolean xMove = false;
	String neuralCode;
	//NC Validation
	char checker;
	double checkerNum = 0;
	double checkerCount = 0;
	boolean validNC = false;

	//ex: String neuralCode = "1000,0100,1100,0001,1100,1110";
	String[] neuralStrings;// = neuralCode.split(",");
	int relations;// = neuralStrings[0].length();

	//initializing a list of colors to use
	private final List<Color> colors;
	Color background = new Color(255,255,234);
	//creating a "pointer" for list of colors, indexes start at 0
	int lineColor = 0;

	/**
	 * Uses the neural code to see if its valid, if so creates a list of them to prepare for use.
	 *
	 * @param sneuralCode (string, (ex: 100 110 011)): a string of the neural codes
	 */
	//this creates the "canvas" that we will be editing, outside of the methods for global editing
    public LineDisplay(String sneuralCode){
    	neuralCode = sneuralCode;
		neuralStrings = neuralCode.split(" ");
		relations = neuralStrings[0].length();
		//System.out.print("Inside class");
		//this algorithm test to see if there is a valid neural code
		while (validNC == false){
			for(int i = 0; i < neuralCode.length(); i++){
				if( neuralCode.charAt(i) == ' '){
					checkerCount++;
				}
				if( neuralCode.charAt(i) != ' ' && neuralCode.charAt(i) != '0' && neuralCode.charAt(i) != '1'){
					System.out.print("Invalid neural code, Try again\n");
					neuralCode = scan.nextLine();
					checkerNum = 0;
					checkerCount = 0;
					checker = '0';
					i = 0;
				}
			}
			while (checker != ' ' && checkerNum != neuralCode.length()){
				checker = neuralCode.charAt((int)checkerNum);
				checkerNum++;
			}
			if (checker == ' '){
				checkerNum--;
				if ((neuralCode.length() - checkerCount) / (checkerCount+1) == checkerNum){
					validNC = true;
				}
				else{
					System.out.print("Invalid neural code, Try again\n");
					neuralCode = scan.nextLine();
					checkerNum = 0;
					checkerCount = 0;
					checker = '0';
				}
			}
			else{
				validNC = true;
			}

		}



		//Splits the NC into seperate Strings
		neuralStrings = neuralCode.split(" ");
		relations = neuralStrings[0].length();

		//creating the color list for the color coded display of lines
		colors = createColorList();

		for(int i = 0; i < relations; i++){
			yWindow = yWindow + 30;
		}
    }


	/**
	 * Creates a list of colors to be used in the jpg.
	 */
	private List<Color> createColorList() {
	        List<Color> list = new ArrayList<>();
	        list.add(Color.RED);
	        list.add(Color.YELLOW);
			list.add(Color.GREEN);
	        list.add(Color.MAGENTA);
	        list.add(Color.CYAN);
	        list.add(Color.GRAY);
	        list.add(Color.BLUE);
	        list.add(Color.ORANGE);
	       	return list;
    }
	/**
	 * Creates the whole jpeg based off of the neural code list. Uses colors in the list of colors method to draw
	 * the relations of the code with different colored lines on different y levels.
	 */
    public void paint() {
		BufferedImage image = new BufferedImage(180+(neuralStrings.length*50),yWindow-30, BufferedImage.TYPE_INT_RGB);
		Graphics2D g3 = image.createGraphics();

		try{

		Rectangle2D rectBackground = new Rectangle2D.Double(0, 0, 180+(neuralStrings.length*50), yWindow-30);
		//Color background = new Color(255,255,204);
		g3.setColor(Color.WHITE);
		g3.fill(rectBackground);
		g3.setColor(Color.lightGray);
		g3.setStroke(new BasicStroke(12));
		g3.draw(rectBackground);
		g3.setStroke(new BasicStroke(2));






		//algorithm for sorting the line by relations
		relArray = new int[neuralStrings.length];
		for (int i = 0; i < neuralStrings.length; i++){

		}

		//Print Code
		g3.setPaint(Color.BLACK);
		String s = ("Neural Code: " + neuralCode);
		g3.drawString("Neural Code: " + neuralCode, 30, 60);
        //print out the labels of the neural codes
		for (int i = 0; i < relations; i++){
			g3.drawString("Neur. " + (i+1), 35, (y+(30*i)+7));
		}
        //algorithm to make the lines no ordering involved
        for (int i = 0; i < neuralStrings.length; i++){
			yWindow = yWindow + 30;
			lineColor = 0;
			y = 90;
			for (int j = 0; j < relations; j++){
				//System.out.print(neuralStrings[i].substring(j,j+1));
				if ((j % 8) == 0){
					lineColor = 0;
				}
				if (neuralStrings[i].substring(j,j+1).equals("1")){
					Rectangle2D rect = new Rectangle2D.Double(x, y, 50, 6);
					g3.setColor(colors.get(lineColor));
					g3.fill(rect);
					g3.setColor(Color.black);
					g3.draw(rect);
					//g3.setColor(colors.get(lineColor));
					g3.draw(new Line2D.Double(x, y, x+50, y));
					//xMove = true;
				}
				y = y + 30;
				lineColor++;
			}
			x = x + 50;
		}

		            ImageIO.write(image, "png", new File("LineRep.jpeg"));
		            //System.out.println("Panel saved as Image.");
		            //System.exit(0);
		        }
		        catch(Exception e)
		        {
		            e.printStackTrace();
        }
        g3.dispose();
    }
	/**
	 * Takes in a neural code a a arguement and calls paint to paint the jpeg, then opens up the jpeg file created.
	 *
	 * @args Neural Code e.g. (the neural code (ex: 100 110 011))
	 *
	 */
    public static void main(String []args){
		//System.out.print("enter NeuralCode (ex: 100 110 011)\n");
		String sneuralCode = "1";
		//calls the drawing
		if(args.length > 0) {
			System.out.println("arg has been recieved");
			for(String arg : args) sneuralCode = arg;
		}
        LineDisplay s=new LineDisplay(sneuralCode);
        s.paint();

        BufferedReader input = null;
    	File f = new File("LineRep.jpeg");
    		System.out.println("Done.");
    	}
}
