
import java.util.Scanner;


public class Ej8 {
        public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int precioBase;
        double descuento;
        double impuesto;
        double precioFinal;
        
            System.out.print("Ingrese el precio base del producto: ");
            precioBase = sc.nextInt();
            System.out.print("Ingrese el impuesto en porcentaje (Ejemplo 10 para 10%): ");
            impuesto = sc.nextDouble() / 100;
            System.out.print("Ingrese el descuento en porcentaje (Ejemplo 10 para 10%): ");
            descuento = sc.nextDouble() / 100;
            
            precioFinal = precioBase + (precioBase * impuesto) - (precioBase * descuento);
            
            System.out.println("El precio final del producto es: " + precioFinal);
        
        
        }
}
