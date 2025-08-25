// A program to find the seller datails.
// Luyanda Ntombela 
// NTMLUY004
// 09 August 2024 


import java.util.Scanner;

public class TestSeller{

   public static void main(String[] args){
    Currency rand = new Currency("R", "ZAR", 100);
      
    Scanner scanner = new Scanner(System.in);
    
    System.out.println("Please enter the details of the seller.");
    
    System.out.print("ID: ");
    String ID = scanner.nextLine();
    
    System.out.print("Name: ");
    String name = scanner.nextLine();
    
    System.out.print("Location: ");
    String location = scanner.nextLine();
   
    System.out.print("Product: ");
    String product = scanner.nextLine();
    
    System.out.print("Price: ");
    String Pric = scanner.nextLine();
    
    System.out.print("Units: ");
    int numberOfUnits = scanner.nextInt();
    
    scanner.close();
    
    Money unitPrice = new Money(Pric, rand);
    Seller seller = new Seller();
    
    seller.ID = ID;
    seller.name = name;
    seller.location = location;
    seller.product = product;
    seller.unitPrice = unitPrice;
    seller.numberOfUnits = numberOfUnits;
    
    
        
       
    System.out.println("The seller has been successfully created:");
    System.out.println("ID of the seller: "+ seller.ID);
    System.out.println("Name of the seller: "+ seller.name);
    System.out.println("Location of the seller: "+ seller.location);
    System.out.println("The product to sell: "+ seller.product);
    System.out.println("Product unit price: "+ seller.unitPrice);
    System.out.println("The number of available units: "+ seller.numberOfUnits);
   
   }

}