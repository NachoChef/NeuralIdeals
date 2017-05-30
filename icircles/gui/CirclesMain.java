package icircles.gui;

public class CirclesMain {

    public static void main(String args[]) {
        if (args.length > 0)
            new CirclesFrame(args[0]);
        else
            System.exit(0);
    }
}
