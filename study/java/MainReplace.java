public class MainReplace {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Будь ласка, передайте рядок як аргумент командного рядка.");
            return;
        }

        String input = args[0];
        String result = ConsonantReplacer.replaceConsonants(input);

        System.out.println("Оригінальний рядок: " + input);
        System.out.println("Модифікований рядок: " + result);
    }
}
