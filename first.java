abstract class Shape {
    double base, height;

    Shape(double b, double h) {
        base = b;
        height = h;
    }

    abstract double shapeArea();
}

class Triangle extends Shape {
    Triangle(double b, double h) {
        super(b, h);
    }

    double shapeArea() {
        return 0.5 * base * height;
    }
}

class Rectangle extends Shape {
    Rectangle(double b, double h) {
        super(b, h);
    }

    double shapeArea() {
        return base * height;
    }
}

class AreaDemo {
    public static void main(String[] args) {
        Shape t = new Triangle(10, 5);
        Shape r = new Rectangle(10, 5);

        System.out.println(t.shapeArea());
        System.out.println(r.shapeArea());
    }
}