import java.io.*;
import java.net.*;

public class TicTacToeServer {
    private static char[][] board = new char[3][3];
    private static PrintWriter out;

    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(5000);
        System.out.println("Сервер очікує підключення...");
        Socket clientSocket = serverSocket.accept();
        System.out.println("Клієнт підключився");

        BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
        out = new PrintWriter(clientSocket.getOutputStream(), true);

        initBoard();

        String inputLine;
        while ((inputLine = in.readLine()) != null) {
            String[] parts = inputLine.split(",");
            int row = Integer.parseInt(parts[0]);
            int col = Integer.parseInt(parts[1]);

            if (board[row][col] == '-') {
                board[row][col] = 'X';
                out.println("UPDATE,X," + row + "," + col);

                if (checkWin('X')) {
                    out.println("WIN");
                    break;
                }

                int[] move = bestMove();
                if (move != null) {
                    board[move[0]][move[1]] = 'O';
                    out.println("UPDATE,O," + move[0] + "," + move[1]);
                    if (checkWin('O')) {
                        out.println("LOSE");
                        break;
                    }
                } else {
                    out.println("DRAW");
                    break;
                }
            }
        }

            clientSocket.close();
        serverSocket.close();
    }

    private static void initBoard() {
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                board[i][j] = '-';
    }

    private static boolean checkWin(char player) {
        for (int i = 0; i < 3; i++)
            if (board[i][0] == player && board[i][1] == player && board[i][2] == player)
                return true;

        for (int i = 0; i < 3; i++)
            if (board[0][i] == player && board[1][i] == player && board[2][i] == player)
                return true;

        if (board[0][0] == player && board[1][1] == player && board[2][2] == player)
            return true;

        if (board[0][2] == player && board[1][1] == player && board[2][0] == player)
            return true;

        return false;
    }

    private static int[] bestMove() {
        // Спроба виграти
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (board[i][j] == '-') {
                    board[i][j] = 'O';
                    if (checkWin('O')) {
                        board[i][j] = '-';
                        return new int[]{i, j};
                    }
                    board[i][j] = '-';
                }

        // Спроба заблокувати 'X'
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (board[i][j] == '-') {
                    board[i][j] = 'X';
                    if (checkWin('X')) {
                        board[i][j] = '-';
                        return new int[]{i, j};
                    }
                    board[i][j] = '-';
                }

        // Перший вільний хід
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (board[i][j] == '-')
                    return new int[]{i, j};

        return null;
    }
}
