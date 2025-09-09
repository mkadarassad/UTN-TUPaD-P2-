
import java.util.Scanner;


public class Ej3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
   int edad;
   
        System.out.println("Ingrese su edad: ");
        edad = sc.nextInt();
        
        if (edad < 12 && 0 <= edad) {
            System.out.println("Eres un Niño");
        } else if (edad > 11 && edad <= 17) {
            System.out.println("Eres un Adolescente");
        } else if (edad > 17 && edad <= 59) {
            System.out.println("Eres un Adulto");
        } else if (edad > 59) {
            System.out.println("Eres un Adulto mayor");
        } else {
            System.out.println("Ingresó una edad inválida.");
        }
   }
}
