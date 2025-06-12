import java.util.ArrayList;
import java.util.List;

public class Athlete {
    private String name;
    private WinterSport sport;
    private List<Equipment> gear = new ArrayList<>();

    public Athlete(String name, WinterSport sport) {
        this.name = name;
        this.sport = sport;
    }

    public String getName() {
        return name;
    }

    // Inner class
    public class Equipment {
        private String type;
        private String brand;
        public Equipment(String type, String brand) {
            this.type = type;
            this.brand = brand;
        }
        @Override
        public String toString() {
            return type + " (" + brand + ")";
        }
    }

    public void addEquipment(String type, String brand) {
        gear.add(new Equipment(type, brand));
    }

    public void showGear() {
        System.out.println(name + "'s equipment:");
        for (Equipment e : gear) {
            System.out.println(" - " + e);
        }
    }

    public void joinSport() {
        sport.participate(this);  // асоціація
    }
}
