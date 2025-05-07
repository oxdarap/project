public class ConsonantReplacer {

    /**
     * Перевіряє, чи символ є приголосною буквою (латиниця або кирилиця).
     */
    public static boolean isConsonant(char c) {
        c = Character.toLowerCase(c);
        return (("bcdfghjklmnpqrstvwxyz".indexOf(c) >= 0) ||  // латинські приголосні
                ("бвгґджзйклмнпрстфхцчшщ".indexOf(c) >= 0));  // українські приголосні
    }

    /**
     * Замінює усі приголосні символи у вхідному рядку на '*'.
     */
    public static String replaceConsonants(String input) {
        StringBuilder result = new StringBuilder();
        for (char ch : input.toCharArray()) {
            if (isConsonant(ch)) {
                result.append('*');
            } else {
                result.append(ch);
            }
        }
        return result.toString();
    }
}