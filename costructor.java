class Student {
    int roll;
    String name;
    double avg;

    Student(int r, String n, double a) {
        roll = r;
        name = n;
        avg = a;
    }

    void display() {
        System.out.println(roll + " " + name + " " + avg);
    }

    public static void main(String[] args) {
        Student s = new Student(101, "Akshaya", 85.5);
        s.display();
    }
}