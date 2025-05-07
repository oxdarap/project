import java.util.Random;

/**
 *  Клас для операцій над матрицями та векторами.
 */
public class matrixmulti {

    /**
     * Генерує вектор заданої довжини зі значеннями у діапазоні [0, 1).
     * @param length довжина вектора
     * @return масив з випадковими значеннями
     */
    public static double[] generateRandomVector(int length) {
        double[] vector = new double[length];
        Random rand = new Random();
        for (int i = 0; i < length; i++) {
            vector[i] = rand.nextDouble();
        }
        return vector;
    }

    /**
     * Генерує матрицю розмірності n × m з випадковими значеннями [0, 1).
     * @param n кількість рядків
     * @param m кількість стовпців
     * @return двовимірний масив
     */
    public static double[][] generateRandomMatrix(int n, int m) {
        double[][] matrix = new double[n][m];
        Random rand = new Random();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                matrix[i][j] = rand.nextDouble();
            }
        }
        return matrix;
    }

    /**
     * Множить вектор (1×n) на матрицю (n×m), результат — вектор (1×m).
     * @param vector вхідний вектор
     * @param matrix вхідна матриця
     * @return результат множення у вигляді вектора
     */
    public static double[] multiplyVectorByMatrix(double[] vector, double[][] matrix) {
        int m = matrix[0].length;
        double[] result = new double[m];

        for (int j = 0; j < m; j++) {
            for (int i = 0; i < vector.length; i++) {
                result[j] += vector[i] * matrix[i][j];
            }
        }
        return result;
    }

    /**
     * Виводить вектор у консоль.
     * @param vector вектор
     */
    public static void printVector(double[] vector) {
        for (double v : vector) {
            System.out.printf("%.4f ", v);
        }
        System.out.println();
    }

    /**
     * Виводить матрицю у консоль.
     * @param matrix матриця
     */
    public static void printMatrix(double[][] matrix) {
        for (double[] row : matrix) {
            for (double val : row) {
                System.out.printf("%.4f ", val);
            }
            System.out.println();
        }
    }
}
