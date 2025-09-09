
import java.util.Scanner;


public class Ej5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
    int num = 1;
    int numPar = 0;
    
        while (num != 0) {            
            System.out.print("Ingrese un número (0 para terminar): ");
            num = sc.nextInt();
            
            if (num % 2 == 0) {
            numPar += num;  
            }
            
        }
            System.out.println("La suma de los números pares es: " + numPar);
        
        
        
    }
}
