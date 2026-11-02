class Emp {
    int id;
    String name;

    Emp(int id, String name) {
        this.id = id;
        this.name = name;
    }
}

class Salary extends Emp {
    String designation;
    double sal;

    Salary(int id, String name, String d, double s) {
        super(id, name);
        designation = d;
        sal = s;
    }

    void display() {
        System.out.println(id + " " + name + " " + designation + " " + sal);
    }

    public static void main(String[] args) {
        Salary a = new Salary(101, "Ravi", "Developer", 40000);
        Salary b = new Salary(102, "Sita", "Tester", 25000);

        if (a.sal > 30000) a.display();
        if (b.sal > 30000) b.display();
    }
}