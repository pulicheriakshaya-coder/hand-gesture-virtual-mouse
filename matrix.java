import java.util.*;
class MatrixDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt(), n = sc.nextInt();
        int p = sc.nextInt(), q = sc.nextInt();

        if (n != p) {
            System.out.println("Multiplication not possible");
            return;
        }

        int[][] a = new int[m][n];
        int[][] b = new int[p][q];
        int[][] c = new int[m][q];

        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                a[i][j] = sc.nextInt();

        for (int i = 0; i < p; i++)
            for (int j = 0; j < q; j++)
                b[i][j] = sc.nextInt();

        for (int i = 0; i < m; i++)
            for (int j = 0; j < q; j++)
                for (int k = 0; k < n; k++)
                    c[i][j] += a[i][k] * b[k][j];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < q; j++)
                System.out.print(c[i][j] + " ");
            System.out.println();
        }
    }
}
