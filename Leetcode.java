public class Leetcode {
    public static void main(String[] args) {
        int rows = 10;
        int[][] a = new int[rows][];

        for (int i = 0; i < rows; i++) {
            a[i] = new int[i + 1];

            for (int j = 0; j <= i; j++) {
                if (j == 0 || j == i) {
                    a[i][j] = 1;
                } else {
                    a[i][j] = a[i - 1][j] + a[i - 1][j - 1];
                }
            }
        }
        for (int i = 0; i < rows; i++) {
            for (int k = 0; k < rows - i; k++) {
                System.out.print("  ");
            }
            for (int j = 0; j <= i; j++) {
                System.out.printf("%4d", a[i][j]);
            }
            System.out.println();
        }
    }
}