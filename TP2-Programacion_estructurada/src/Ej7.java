
import java.util.Scanner;

public class Ej7 {
        public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int nota;
        
            System.out.print("Ingrese una nota (0-10): ");
            nota = sc.nextInt();
                    
            if (nota < 0 || nota > 10){
            do {
                System.out.print("Error: Nota inválida. Ingrese una nota entre 0 y 10: ");
                nota = sc.nextInt();
            } while (nota < 0 && nota > 10);
            }
            System.out.println("Nota guardada correctamente.");
        }
        
}
