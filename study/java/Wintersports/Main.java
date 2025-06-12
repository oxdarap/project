public class Main {
    public static void main(String[] args) {
        // Створюємо вид спорту
        WinterSport skiing = new WinterSport("Skiing");
        WinterSport.Location alps = new WinterSport.Location("Alpine Center");
        skiing.addEvent("Downhill", alps);
        skiing.addEvent("Slalom", new WinterSport.Location("Slalom Arena"));
        skiing.listEvents();

        // Створюємо спортсменів
        Athlete ivan = new Athlete("Ivan Petrov", skiing);
        ivan.addEquipment("Skis", "Rossignol");
        ivan.addEquipment("Helmet", "Giro");
        ivan.joinSport();
        ivan.showGear();

        Athlete olga = new Athlete("Olga Ivanova", skiing);
        olga.addEquipment("Skis", "Salomon");
        olga.joinSport();

        // Створюємо команду
        Team teamUA = new Team("Ukraine Ski Team");
        teamUA.addMember(ivan);
        teamUA.addMember(olga);
        teamUA.showTeam();
    }
}
