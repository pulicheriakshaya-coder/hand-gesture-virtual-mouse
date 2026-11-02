import java.util.*;
class GradeDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(), b = sc.nextInt();
        int c = sc.nextInt(), d = sc.nextInt();

        double avg = (a + b + c + d) / 4.0;
        System.out.println("Average = " + avg);

        if (avg >= 70)
            System.out.println("Distinction");
        else if (avg >= 60)
            System.out.println("First Class");
        else if (avg >= 50)
            System.out.println("Second Class");
        else if (avg >= 40)
            System.out.println("Second Class");
        else
            System.out.println("Fail");
    }
}
