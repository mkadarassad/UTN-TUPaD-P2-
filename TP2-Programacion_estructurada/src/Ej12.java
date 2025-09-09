
import java.util.Scanner;


public class Ej12 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
     
        double [] precios = {199.99,299.5,149.75};
        
        for (int i = 0; i < precios.length; i++) {
            System.out.println("Precio: " + precios[i]);
            
        }
        
        precios[2] = 1.1;
        System.out.println("Precio modificado: " + precios[2]);
        
        for (int i = 0; i < precios.length; i++) {
            System.out.println("Precio: " + precios[i]);
            
        }
        
    }
}
