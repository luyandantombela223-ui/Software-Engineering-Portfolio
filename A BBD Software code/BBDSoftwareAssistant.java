import java.util.Random;
import java.util.Scanner;

/**
 * BBD Software Assistant
 * A fun program that shares random facts, values, and
 * motivational tips related to BBD Software.
 *
 * Author: Luyanda Ntombela
 */
public class BBDSoftwareAssistant {

    private static final String[] COMPANY_FACTS = {
        "BBD Software has over 35 years of experience in software solutions.",
        "BBD partners with clients in finance, telecoms, insurance, and government sectors.",
        "BBD is known for solving complex business problems with smart tech.",
        "BBD values innovation, teamwork, and continuous learning."
    };

    private static final String[] CAREER_TIPS = {
        "Write clean, readable code — it matters in real projects.",
        "Always test your programs. Debugging is a developer's superpower.",
        "Teamwork is key: software is rarely built alone.",
        "Keep learning new technologies, just like BBD invests in growth."
    };

    private static final String[] MOTIVATION = {
        "You are the future of tech 🚀",
        "Every bug fixed is a step closer to mastery 💻",
        "Stay curious, keep building 🔥",
        "Great software starts with one line of code ✨"
    };

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random rand = new Random();

        System.out.println("✨ Welcome to the BBD Software Assistant ✨");
        System.out.print("Enter your name: ");
        String name = sc.nextLine();

        // Pick random messages
        String fact = COMPANY_FACTS[rand.nextInt(COMPANY_FACTS.length)];
        String tip = CAREER_TIPS[rand.nextInt(CAREER_TIPS.length)];
        String quote = MOTIVATION[rand.nextInt(MOTIVATION.length)];

        System.out.println("\nHello " + name + "! Here’s your BBD insight for today:\n");
        System.out.println("📌 Company Fact: " + fact);
        System.out.println("💡 Career Tip: " + tip);
        System.out.println("🔥 Motivation: " + quote);

        System.out.println("\nThank you for exploring the BBD Assistant. Keep coding, " + name + "!");
        sc.close();
    }
}
