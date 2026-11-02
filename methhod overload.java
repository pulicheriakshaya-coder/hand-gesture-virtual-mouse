class Volume {
    final double PI = 3.142;

    double getVolume(double r) {
        return 4.0 / 3 * PI * r * r * r;
    }

    double getVolume(double r, double h) {
        return PI * r * r * h;
    }

    double getVolume(int r, int h) {
        return 1.0 / 3 * PI * r * r * h;
    }

    public static void main(String[] args) {
        Volume v = new Volume();
        System.out.println(v.getVolume(3.0));
        System.out.println(v.getVolume(5.0, 8.0));
        System.out.println(v.getVolume(6, 9));
    }
}
