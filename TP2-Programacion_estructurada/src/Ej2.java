
import java.util.Scanner;


public class Ej2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
     int numero1;
     int numero2;
     int numero3;
     
        System.out.print("Ingrese un número: ");
        numero1 = sc.nextInt();
        
        System.out.print("Ingrese otro número: ");
        numero2 = sc.nextInt();
        
        System.out.print("Ingrese otro número: ");
        numero3 = sc.nextInt();
    
    int mayor = numero1;
        
        if (numero2 >= mayor) {
            mayor = numero2;          
        } 
        if (numero3 >= mayor) {
            mayor = numero3;
        }
        
        System.out.println("El mayor es: " + mayor);
    }
}
