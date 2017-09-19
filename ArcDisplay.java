import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.geom.Rectangle2D;
import java.awt.image.BufferedImage;
import java.io.BufferedReader;
import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
/**
 * CircleDisplay.java
 * The code is based off of 'CONVEX NEURAL CODES IN DIMENSION 1' by ZVI ROSEN, UNIVERSITY OF PENNSYLVANIA, PA
 * and YAN X ZHANG, SAN JOSE STATE UNIVERSITY, CA
 *
 * Purpose: Creates a jpg that displays a one dimensional circular linear representation of a neural code
 *
 * Other Contributors: Dr. Luis Garcia, Alex Norma, and Alexander Farrack
 */
class ArcDisplay {
    Scanner scan = new Scanner(System.in);
    //initializing the line starting cordinates
    int x = 100;
    int y = 90;
    int[] relArray;
    int yWindow = 100;
    int circlePos = yWindow / 2;
    boolean xMove = false;
    String neuralCode;
    //NC Validation
    char checker;
    double checkerNum = 0;
    double checkerCount = 0;
    boolean validNC = false;
    int codes = 0;
    int cWidth = 100;
    int cHeight = 100;
    String[] neuralStrings;
    int relations;
    int relationNum = 1;
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
    public ArcDisplay(String sneuralCode){
        neuralCode = sneuralCode;
        neuralStrings = neuralCode.split(" ");
        relations = neuralStrings[0].length();
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
        codes = (int)(checkerCount + 1);
    }

    /**
     * Creates a list of colors to be used in the jpg.
     */
    private List<Color> createColorList() {
        List<Color> list = new ArrayList<>();
        list.add(Color.RED);
        list.add(Color.BLUE);
        list.add(Color.YELLOW);
        list.add(Color.GREEN);
        list.add(Color.MAGENTA);
        list.add(Color.CYAN);
        list.add(Color.GRAY);
        list.add(Color.ORANGE);
        return list;
    }
    /**
     * Creates the whole jpeg based off of the neural code list. Uses colors in the list of colors method to draw
     * different colored arcs to represent the relations in the code.
     */
    public void paint() {
        BufferedImage image = new BufferedImage(yWindow + (relations*10),yWindow + (relations*10), BufferedImage.TYPE_INT_RGB);
        Graphics2D g3 = image.createGraphics();

        try {
            Rectangle2D rectBackground = new Rectangle2D.Double(0, 0, yWindow + (relations * 10), yWindow + (relations * 10));
            //Color background = new Color(255,255,204);
            circlePos = ((yWindow + (relations * 10)) / 2) - (cWidth / 2);
            g3.setColor(Color.WHITE);
            g3.fill(rectBackground);
            g3.setColor(Color.lightGray);
            g3.setStroke(new BasicStroke(5));
            g3.draw(rectBackground);
            //algorithm for sorting the line by relations
            relArray = new int[neuralStrings.length];
            //Print Code
            g3.setPaint(Color.BLACK);
            //String s = ("Neural Code: " + neuralCode);
            //g3.drawString("Neural Code: " + neuralCode, 10, 20);
            //Drawing the arcs begins
            lineColor = 0;
            for(int i = 0; i < relations; i++)
            {
                g3.setColor(colors.get(lineColor));
                if ((lineColor % 8) == 0) {
                    lineColor = 0;
                }
                for (int j = 0; j < codes; j++)
                {
                    if (neuralStrings[j].substring(i,i+1).equals("1")) {
                        g3.drawArc(circlePos - ((i+ 1) * 10),circlePos - ((i+1) * 10),cWidth + ((i+1) * 20), cHeight + ((i+1) * 20), j * (360 / (codes)),1 * (360 / (codes)));
                    }
                }
                lineColor++;
            }
            g3.setPaint(Color.lightGray);

            g3.fillOval(circlePos, circlePos, cWidth, cHeight);

            ImageIO.write(image, "png", new File("ArcRep.jpeg"));
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
     * Takes an arguement (the neural code (ex: 100 110 011)) and calls paint to paint the jpeg, then opens up the jpeg file created.
     *
     * @args Neural Code
     *
     */
    public static void main(String []args){
        //System.out.print("enter NeuralCode (ex: 100,110,011)\n");
        String sneuralCode = "1";
        //calls the drawing
        if(args.length > 0) {
            //System.out.println("arg has been recieved");
            for(String arg : args) sneuralCode = arg;
        }
        ArcDisplay s=new ArcDisplay(sneuralCode);
        s.paint();

        BufferedReader input = null;
        File f = new File("ArcRep.jpeg");
        System.out.println("Done.");
    }
}
