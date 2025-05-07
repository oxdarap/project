import java.io.*;
import java.util.*;
import java.nio.file.Files;
import java.nio.file.Paths;

public class PrimeNumberFileProcessor {

    private static final String FILE_NAME = "numbers.txt";
    private static final String PRIME_FILE_NAME = "primes.txt";
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        while (true) {
            System.out.println("\n--- МЕНЮ ---");
            System.out.println("1. Заповнити файл з клавіатури");
            System.out.println("2. Додати нові записи у файл");
            System.out.println("3. Переглянути записи з файлу");
            System.out.println("4. Редагувати запис у файлі");
            System.out.println("5. Зберегти прості числа у новий файл");
            System.out.println("0. Вийти");

            System.out.print("Виберіть опцію: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1 -> writeNumbersFromKeyboard();
                case 2 -> appendNumbersToFile();
                case 3 -> readNumbersFromFile();
                case 4 -> editNumberInFile();
                case 5 -> savePrimesToFile();
                case 0 -> {
                    System.out.println("Завершення роботи.");
                    return;
                }
                default -> System.out.println("Невірна опція!");
            }
        }
    }

    private static void writeNumbersFromKeyboard() {
        try (PrintWriter writer = new PrintWriter(new FileWriter(FILE_NAME))) {
            System.out.println("Введіть числа через пробіл:");
            scanner.nextLine(); // очищення буфера
            String input = scanner.nextLine();
            writer.println(input);
            System.out.println("Файл успішно збережено.");
        } catch (IOException e) {
            System.out.println("Помилка запису у файл.");
        }
    }

    private static void appendNumbersToFile() {
        try (PrintWriter writer = new PrintWriter(new FileWriter(FILE_NAME, true))) {
            System.out.println("Введіть числа для додавання:");
            scanner.nextLine(); // очищення буфера
            String input = scanner.nextLine();
            writer.println(input);
            System.out.println("Дані додано у файл.");
        } catch (IOException e) {
            System.out.println("Помилка при додаванні.");
        }
    }

    private static void readNumbersFromFile() {
        try (BufferedReader reader = new BufferedReader(new FileReader(FILE_NAME))) {
            String line;
            System.out.println("Зміст файлу:");
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.out.println("Помилка читання файлу.");
        }
    }

    private static void editNumberInFile() {
        try {
            List<String> lines = new ArrayList<>(Files.readAllLines(new File(FILE_NAME).toPath()));
            if (lines.isEmpty()) {
                System.out.println("Файл порожній.");
                return;
            }

            System.out.println("Записи у файлі:");
            for (int i = 0; i < lines.size(); i++) {
                System.out.println((i + 1) + ": " + lines.get(i));
            }

            System.out.print("Оберіть номер рядка для редагування: ");
            int index = scanner.nextInt();
            scanner.nextLine(); // очищення буфера

            if (index < 1 || index > lines.size()) {
                System.out.println("Невірний індекс.");
                return;
            }

            System.out.print("Введіть новий вміст для рядка: ");
            String newContent = scanner.nextLine();
            lines.set(index - 1, newContent);

            Files.write(new File(FILE_NAME).toPath(), lines);
            System.out.println("Файл оновлено.");
        } catch (IOException e) {
            System.out.println("Помилка редагування.");
        }
    }

    private static void savePrimesToFile() {
        try (BufferedReader reader = new BufferedReader(new FileReader(FILE_NAME));
             PrintWriter writer = new PrintWriter(new FileWriter(PRIME_FILE_NAME))) {

            String line;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.trim().split("\\s+");
                for (String part : parts) {
                    try {
                        int num = Integer.parseInt(part);
                        if (isPrime(num)) {
                            writer.print(num + " ");
                        }
                    } catch (NumberFormatException ignored) {
                    }
                }
            }
            System.out.println("Прості числа збережено у файл: " + PRIME_FILE_NAME);
        } catch (IOException e) {
            System.out.println("Помилка при збереженні простих чисел.");
        }
    }

    private static boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }
}
