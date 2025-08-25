// A program to find total amount.
// Luyanda Ntombela 
// NTMLUY004
// 19 August 2024 

import static org.junit.Assert.*;
import org.junit.Test;

public class TestOfTime {

    // 1. Test that Time stores the correct value
    @Test
    public void testTimeCreation() {
        Time t = new Time("13:45");
        assertEquals("13:45:00", t.toString());
    }

    // 2. Test subtracting an earlier Time from a later Time
    @Test
    public void testTimeSubtraction() {
        Time t1 = new Time("15:00");
        Time t2 = new Time("14:00");
        Duration d = t1.subtract(t2);
        assertEquals(1, d.intValue("hour"));
    }

    // 3. Test subtracting the same Time
    @Test
    public void testSubtractSameTime() {
        Time t = new Time("12:30");
        Duration d = t.subtract(t);
        assertEquals(0, d.intValue("second"));
    }

    // 4. Test intValue with milliseconds
    @Test
    public void testDurationMilliseconds() {
        Time t1 = new Time("10:00:00");
        Time t2 = new Time("10:00:01");  // 1 second apart
        Duration d = t2.subtract(t1);
        assertEquals(1000, d.intValue("millisecond"));
    }

    // 5. Test intValue with seconds
    @Test
    public void testDurationSeconds() {
        Time t1 = new Time("09:00:00");
        Time t2 = new Time("09:01:05"); // 65 seconds apart
        Duration d = t2.subtract(t1);
        assertEquals(65, d.intValue("second"));
    }

    // 6. Test intValue with minutes
    @Test
    public void testDurationMinutes() {
        Time t1 = new Time("08:00:00");
        Time t2 = new Time("09:05:00"); // 65 minutes apart
        Duration d = t2.subtract(t1);
        assertEquals(65, d.intValue("minute"));
    }

    // 7. Test intValue with hours
    @Test
    public void testDurationHours() {
        Time t1 = new Time("06:00:00");
        Time t2 = new Time("09:00:00"); // 3 hours apart
        Duration d = t2.subtract(t1);
        assertEquals(3, d.intValue("hour"));
    }
}
