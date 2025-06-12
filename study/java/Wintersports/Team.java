import java.util.ArrayList;
import java.util.List;

public class Team {
    private String name;
    private List<Athlete> members = new ArrayList<>();

    public Team(String name) {
        this.name = name;
    }

    // агрегація: додаємо зовнішні об’єкти Athlete
    public void addMember(Athlete a) {
        members.add(a);
    }

    public void showTeam() {
        System.out.println("Team " + name + " members:");
        for (Athlete a : members) {
            System.out.println(" - " + a.getName());
        }
    }
}
