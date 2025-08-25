// A code to helps the a person to find things that he/she can afford.
 // Luyanda Ntombela
 // NTMLUY004
 // 12 August 2025
 
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
/**
 * See Assignment II Question II
 *
 * @author Stephan Jamieson
 * @version 26/7/2019
 */
public class MarketPlace {
    
    private MarketPlace() {}
    
    private final static Currency RAND = new Currency("R", "ZAR", 100);
    
    private static Seller makeSeller(final String data) {
        final Scanner scanner = new Scanner(data.trim());
        scanner.useDelimiter("\\s*,\\s*");
        
        String ID = scanner.next();
        String name = scanner.next();
        String location = scanner.next();
        String product = scanner.next();
        String unit_price = scanner.next();
        Money unitPrice = new Money(unit_price, RAND);
        int numberOfUnits = scanner.nextInt();
        
        Seller seller = new Seller();
        
        seller.ID = ID;
        seller.name = name;
        seller.location = location;
        seller.product = product;
        seller.unitPrice = unitPrice;
        seller.numberOfUnits = numberOfUnits;
        
        scanner.close();
        
        return seller;
    }
    
    private static Seller[] parseFile(final String fileName) throws FileNotFoundException {
        File file = new File(fileName);
        
        if (!file.exists()){
            System.out.println("The file contains no seller data.");
            return null;
        }   
        
        final Scanner inFile = new Scanner(file);
        
    
        if (!inFile.hasNextLine()) {
            System.out.println("The file contains no seller data.");
            inFile.close();
            return null;
        }
        
        int count = Integer.parseInt(inFile.nextLine().trim());
        if (count == 0){
            System.out.println("The file contains no seller data.");
            inFile.close();
            return null;
        }
        Seller[] sellers = new Seller[count];
        for (int index = 0; index < sellers.length; index++){
            if (inFile.hasNextLine()){
                sellers[index] = makeSeller(inFile.nextLine());
          
            }
        }
        inFile.close();
        return sellers;
    }
    
    public static void main(final String[] args) throws FileNotFoundException {
        final Scanner inKey = new Scanner(System.in);
        System.out.println("Enter the name of a \"Comma Separated Values\" (CSV) file:");
        final Seller[] sellers = parseFile(inKey.nextLine());
        

        if (sellers == null || sellers.length == 0){
            inKey.close();
            return;
        }
        System.out.println("Enter the name of a product:");
        String product = inKey.nextLine();
        
        System.out.println("Enter the number of units required:");
        int numberOfUnits = inKey.nextInt();
        
        System.out.println("Enter the maximum unit price:");
        Money unitPrice = new Money(inKey.next(), RAND);
        inKey.nextLine();
        boolean found = false;

        for (Seller s : sellers) {
            if (s != null && s.product.equalsIgnoreCase(product) && s.numberOfUnits >= numberOfUnits && s.unitPrice.compareTo(unitPrice) <= 0) {

                System.out.println(s.ID + " : " + s.name + " in " + s.location +" has " + s.numberOfUnits + " " + s.product + " for " + s.unitPrice + " each.");
                found = true;
            }
        }

        if (!found) {
            System.out.println("None found.");
        }
        inKey.close();
    }
}