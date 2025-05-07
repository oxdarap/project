/**
 * Основний клас для запуску програми множення вектора на матрицю.
 * Аргументи командного рядка:
 * args[0] — розмірність вектора (n)
 * args[1] — кількість стовпців матриці (m)
 */
public class mainmatrix {
    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Використання: java mainmatrix <розмірність вектора n> <кількість стовпців матриці m>");
            return;
        }

        int n = Integer.parseInt(args[0]);
        int m = Integer.parseInt(args[1]);

        // Генерація вектора та матриці
        double[] vector = matrixmulti.generateRandomVector(n);
        double[][] matrix = matrixmulti.generateRandomMatrix(n, m);

        // Вивід вхідних даних
        System.out.println("Вектор:");
        matrixmulti.printVector(vector);

        System.out.println("\nМатриця:");
        matrixmulti.printMatrix(matrix);

        // Множення
        double[] result = matrixmulti.multiplyVectorByMatrix(vector, matrix);

        // Результат
        System.out.println("\nРезультат множення:");
        matrixmulti.printVector(result);
    }
}
