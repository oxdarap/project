import java.util.ArrayList;
import java.util.List;

public class WinterSport {
    private String name;
    private List<Event> events = new ArrayList<>();

    // Static nested class
    public static class Location {
        private String venue;
        public Location(String venue) { this.venue = venue; }
        public String getVenue() { return venue; }
    }

    public WinterSport(String name) {
        this.name = name;
    }

    // композиція: WinterSport створює Event
    public void addEvent(String eventName, Location loc) {
        events.add(new Event(eventName, loc));
    }

    public void listEvents() {
        // Local class
        class EventDetail {
            void print() {
                for (Event e : events) {
                    System.out.println(e.name + " @ " + e.location.getVenue());
                }
            }
        }
        new EventDetail().print();
    }

    private class Event {
        private String name;
        private Location location;
        private Event(String name, Location loc) {
            this.name = name;
            this.location = loc;
        }
    }

    // асоціація: Athlete бере участь у цьому спорті
    public void participate(Athlete a) {
        System.out.println(a.getName() + " participates in " + name);
    }
}
