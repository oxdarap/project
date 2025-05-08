import java.io.*;
import java.util.*;
import java.util.concurrent.*;

public class MultiThreadedWordPrinter {

    private static final int THREAD_COUNT = 18;

    public static void main(String[] args) throws Exception {
        String filePath = "C:\\Users\\oxdarap\\IdeaProjects\\lab1\\src\\input.txt"; // Вкажи шлях до свого файлу
        List<String> allWords = readWordsFromFile(filePath);

        int chunkSize = allWords.size() / THREAD_COUNT;

        ExecutorService executor = Executors.newFixedThreadPool(THREAD_COUNT);

        for (int i = 0; i < THREAD_COUNT; i++) {
            int start = i * chunkSize;
            int end = (i == THREAD_COUNT - 1) ? allWords.size() : (i + 1) * chunkSize;

            List<String> subList = allWords.subList(start, end);

            Runnable task = new WordPrinter(subList, i + 1);
            executor.execute(task);
        }

        executor.shutdown();
    }

    // Зчитування всіх слів з файлу
    private static List<String> readWordsFromFile(String filePath) throws IOException {
        List<String> words = new ArrayList<>();
        BufferedReader reader = new BufferedReader(new FileReader(filePath));
        String line;

        while ((line = reader.readLine()) != null) {
            String[] split = line.split("\\s+"); // Розбиває за пробілами
            Collections.addAll(words, split);
        }

        reader.close();
        return words;
    }

    // Клас потоку для виводу слів
    static class WordPrinter implements Runnable {
        private final List<String> words;
        private final int threadId;

        public WordPrinter(List<String> words, int threadId) {
            this.words = words;
            this.threadId = threadId;
        }

        @Override
        public void run() {
            for (String word : words) {
                System.out.println("Потік " + threadId + ": " + word);
            }
        }
    }
}
