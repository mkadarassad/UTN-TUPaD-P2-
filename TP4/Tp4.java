public class Tp4 {
    public static void main(String[] args) {
        Empleado e1 = new Empleado(101, "Ana Pérez", "Desarrolladora", 150000);
        Empleado e2 = new Empleado("Bruno López", "QA");
        Empleado e3 = new Empleado("Carla Gómez", "DevOps");

        e1.actualizarSalario(10);        // +10%
        e2.actualizarSalario(20000.0);   // +$20.000
        e3.actualizarSalario(15);        // +15%
        e3.actualizarSalario(10000.0);   // +$10.000

        System.out.println(e1);
        System.out.println(e2);
        System.out.println(e3);

        System.out.println("Total empleados: " + Empleado.mostrarTotalEmpleados());
    }
}
