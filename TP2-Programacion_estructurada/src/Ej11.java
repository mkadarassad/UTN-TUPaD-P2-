
import java.util.Scanner;


public class Ej11 {
// Variable "global" de clase
    static double descuentoGlobal = 0.10; // 10%

    // Método para calcular descuento especial
    public static void calcularDescuentoEspecial(double precio) {
        // Variable local
        double descuentoAplicado = precio * descuentoGlobal;
        double precioFinal = precio - descuentoAplicado;

        System.out.println("El descuento especial aplicado es: " + descuentoAplicado);
        System.out.println("El precio final con descuento es: " + precioFinal);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Ingrese el precio del producto: ");
        double precio = sc.nextDouble();

        calcularDescuentoEspecial(precio);

    }
}
