
import java.util.Scanner;


public class Ej9 {
    public static double calcularCostoEnvio(double peso, String zona) {
        double costo = 0.0;

        if (zona.equalsIgnoreCase("Nacional")) {
            costo = peso * 5;
        } else if (zona.equalsIgnoreCase("Internacional")) {
            costo = peso * 10;
        } else {
            System.out.println("Zona inválida. Se asumirá Nacional.");
            costo = peso * 5;
        }

        return costo;
    }

    public static double calcularTotalCompra(double precioProducto, double costoEnvio) {
        return precioProducto + costoEnvio;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Ingrese el precio del producto: ");
        double precioProducto = sc.nextDouble();

        System.out.print("Ingrese el peso del paquete en kg: ");
        double peso = sc.nextDouble();

        sc.nextLine();
        System.out.print("Ingrese la zona de envío (Nacional/Internacional): ");
        String zona = sc.nextLine();

        double costoEnvio = calcularCostoEnvio(peso, zona);
        double total = calcularTotalCompra(precioProducto, costoEnvio);

        System.out.println("El costo de envío es: " + costoEnvio);
        System.out.println("El total a pagar es: " + total);
    }
}