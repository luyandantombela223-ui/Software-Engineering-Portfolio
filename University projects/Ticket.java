// A program to find test a tickect.
// Luyanda Ntombela 
// NTMLUY004
// 19 August 2025 


public class Ticket {
    // Instance variables
    private String id;
    private Time issueTime;

    // Constructor
    public Ticket(Time currentTime, String ID) {
        this.issueTime = currentTime;
        this.id = ID;
    }

    // Methods
    public String ID() {
        return id;
    }

    public Duration age(Time currentTime) {
        // age = currentTime - issueTime
        return currentTime.subtract(issueTime);
    }

    @Override
    public String toString() {
        return "Ticket[id=" + id + ", time=" + issueTime.toString() + "]";
    }
}
