
import java.util.Scanner;


public class Ej6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
     int positivos = 0;
     int negativos = 0;
     int ceros = 0;
     int num = 0;
     
        for (int i = 1; i <= 10; i++) {
            System.out.print("Ingrese el número " + i + ": ");
            num = sc.nextInt();
            
            if (num == 0){
                ceros += 1;
            } else if (num < 0) {
                negativos += 1;
            } else {
                positivos += 1;
            }
        }
            System.out.println("Resultados:");
            System.out.println("Positivos: " + positivos);
            System.out.println("Negativos: " + negativos);
            System.out.println("Ceros: " + ceros);
    }
}
