//A program to store the seller datails.
// Luyanda Ntombela 
// NTMLUY004
// 19 August 2025


public class Register {
    // Instance variables
    private Ticket[] tickets;
    private int numTickets;

    // Constructor
    public Register() {
        tickets = new Ticket[100]; // fixed length array
        numTickets = 0;
    }

    // Store the given ticket in the register
    public void add(Ticket ticket) {
        if (numTickets < tickets.length) {
            tickets[numTickets] = ticket;
            numTickets++;
        } else {
            System.out.println("Register is full! Cannot add ticket.");
        }
    }

    // Determine whether a ticket with the given ID is in the collection
    public boolean contains(String ticketID) {
        for (int i = 0; i < numTickets; i++) {
            if (tickets[i].ID().equals(ticketID)) {
                return true;
            }
        }
        return false;
    }

    // Get the Ticket with the given ID from the collection
    public Ticket retrieve(String ticketID) {
        for (int i = 0; i < numTickets; i++) {
            if (tickets[i].ID().equals(ticketID)) {
                return tickets[i];
            }
        }
        return null; // if not found
    }
}
