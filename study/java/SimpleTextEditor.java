import javax.swing.*;
import java.awt.*;
import java.io.*;

public class SimpleTextEditor extends JFrame {

    private JTextArea textArea;

    public SimpleTextEditor() {
        setTitle("Простий текстовий редактор");
        setSize(700, 500);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // === Текстова область ===
        textArea = new JTextArea();
        JScrollPane scrollPane = new JScrollPane(textArea);
        add(scrollPane, BorderLayout.CENTER);

        // === Меню ===
        JMenuBar menuBar = new JMenuBar();

        // --- Файл ---
        JMenu fileMenu = new JMenu("Файл");
        JMenuItem openItem = new JMenuItem("Відкрити");
        JMenuItem saveItem = new JMenuItem("Зберегти");
        JMenuItem restartItem = new JMenuItem("Перезапустити програму");
        JMenuItem exitItem = new JMenuItem("Вийти");

        fileMenu.add(openItem);
        fileMenu.add(saveItem);
        fileMenu.addSeparator();
        fileMenu.add(restartItem);
        fileMenu.add(exitItem);

        // --- Довідка ---
        JMenu helpMenu = new JMenu("Довідка");
        JMenuItem usageHelpItem = new JMenuItem("Довідка по редактору");
        JMenuItem aboutItem = new JMenuItem("Про програму");
        helpMenu.add(usageHelpItem);
        helpMenu.add(aboutItem);

        menuBar.add(fileMenu);
        menuBar.add(helpMenu);
        setJMenuBar(menuBar);

        // === Обробники подій ===
        openItem.addActionListener(e -> openFile());
        saveItem.addActionListener(e -> saveFile());
        exitItem.addActionListener(e -> System.exit(0));
        restartItem.addActionListener(e -> restartApplication());
        usageHelpItem.addActionListener(e -> showHtmlHelp());
        aboutItem.addActionListener(e -> showAbout());

        setVisible(true);
    }

    private void openFile() {
        JFileChooser fileChooser = new JFileChooser();
        int option = fileChooser.showOpenDialog(this);
        if (option == JFileChooser.APPROVE_OPTION) {
            File file = fileChooser.getSelectedFile();
            try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
                textArea.setText("");
                String line;
                while ((line = reader.readLine()) != null) {
                    textArea.append(line + "\n");
                }
            } catch (IOException e) {
                showError("Помилка відкриття файлу.");
            }
        }
    }

    private void saveFile() {
        JFileChooser fileChooser = new JFileChooser();
        fileChooser.setDialogTitle("Зберегти як");
        int option = fileChooser.showSaveDialog(this);
        if (option == JFileChooser.APPROVE_OPTION) {
            File file = fileChooser.getSelectedFile();
            if (!file.getName().toLowerCase().endsWith(".txt")) {
                file = new File(file.getAbsolutePath() + ".txt");
            }
            try (BufferedWriter writer = new BufferedWriter(new FileWriter(file))) {
                writer.write(textArea.getText());
            } catch (IOException e) {
                showError("Помилка збереження файлу.");
            }
        }
    }

    private void restartApplication() {
        dispose();
        SwingUtilities.invokeLater(SimpleTextEditor::new);
    }

    private void showHtmlHelp() {
        JFrame helpFrame = new JFrame("Довідка по редактору");
        helpFrame.setSize(600, 400);
        helpFrame.setLocationRelativeTo(null);

        JTextPane helpPane = new JTextPane();
        helpPane.setContentType("text/html");
        helpPane.setEditable(false);

        try {
            helpPane.setPage(getClass().getResource("help.html"));
        } catch (IOException e) {
            helpPane.setText("<html><body><h2>Не вдалося завантажити довідку.</h2></body></html>");
        }

        helpFrame.add(new JScrollPane(helpPane));
        helpFrame.setVisible(true);
    }

    private void showAbout() {
        JOptionPane.showMessageDialog(this,
                "Простий текстовий редактор\nРозроблено у 2025 році",
                "Про програму", JOptionPane.INFORMATION_MESSAGE);
    }

    private void showError(String message) {
        JOptionPane.showMessageDialog(this, message, "Помилка", JOptionPane.ERROR_MESSAGE);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(SimpleTextEditor::new);
    }
}
