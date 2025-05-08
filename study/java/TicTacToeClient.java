import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.net.*;

public class TicTacToeClient extends JFrame {
    private JButton[][] buttons = new JButton[3][3];
    private BufferedReader in;
    private PrintWriter out;

    public TicTacToeClient() {
        setTitle("Хрестики-нулики");
        setSize(300, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridLayout(3, 3));

        try {
            Socket socket = new Socket("localhost", 5000);
            in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            out = new PrintWriter(socket.getOutputStream(), true);
        } catch (IOException e) {
            JOptionPane.showMessageDialog(this, "Помилка підключення: " + e.getMessage());
            System.exit(1);
        }

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                JButton btn = new JButton("");
                btn.setFont(new Font(Font.SANS_SERIF, Font.BOLD, 40));
                final int row = i, col = j;
                btn.addActionListener(e -> handleClick(btn, row, col));
                buttons[i][j] = btn;
                add(btn);
            }
        }

        setVisible(true);
    }

    private void handleClick(JButton btn, int row, int col) {
        if (!btn.getText().equals("")) return;

        out.println(row + "," + col);

        // Окремий потік для обробки відповідей
        new Thread(() -> {
            try {
                while (true) {
                    String line = in.readLine();
                    if (line == null) break;

                    if (line.startsWith("UPDATE")) {
                        String[] parts = line.split(",");
                        String symbol = parts[1];
                        int r = Integer.parseInt(parts[2]);
                        int c = Integer.parseInt(parts[3]);
                        SwingUtilities.invokeLater(() -> {
                            buttons[r][c].setText(symbol);
                            buttons[r][c].setEnabled(false);
                        });
                    } else if (line.equals("WIN")) {
                        SwingUtilities.invokeLater(() -> {
                            JOptionPane.showMessageDialog(this, "Ви перемогли!");
                            System.exit(0);
                        });
                        break;
                    } else if (line.equals("LOSE")) {
                        SwingUtilities.invokeLater(() -> {
                            JOptionPane.showMessageDialog(this, "Ви програли!");
                            System.exit(0);
                        });
                        break;
                    } else if (line.equals("DRAW")) {
                        SwingUtilities.invokeLater(() -> {
                            JOptionPane.showMessageDialog(this, "Нічия!");
                            System.exit(0);
                        });
                        break;
                    } else {
                        break;
                    }
                }
            } catch (IOException e) {
                SwingUtilities.invokeLater(() ->
                        JOptionPane.showMessageDialog(this, "Помилка зв'язку: " + e.getMessage())
                );
            }
        }).start();
    }


    public static void main(String[] args) {
        SwingUtilities.invokeLater(TicTacToeClient::new);
    }
}
