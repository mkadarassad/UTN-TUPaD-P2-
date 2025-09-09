
import java.util.Scanner;


public class Ej4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
     
        int precio;
        String categoria;
        double descuento = 0.0;
        
        System.out.print("Ingrese el precio del producto: ");
        precio = sc.nextInt();
        
        sc.nextLine();
        System.out.print("Ingrese la categoría del producto (A, B o C): ");
        categoria = sc.nextLine();
        
        if (categoria.equals("A") || categoria.equals("a")) {
        descuento =  0.1;   
        } else if (categoria.equals("B") || categoria.equals("b")){
        descuento = 0.15;
        } else if (categoria.equals("C") || categoria.equals("c")){
        descuento = 0.2;
        } else {System.out.println("Categoría inválida. Vuelva a correr el programa.");}
        
        System.out.println("Descuento aplicado: " + ((double)descuento * 100) + "%" );
        
        System.out.println("Precio final: $" + (precio * (1- descuento)));
        
        
        
        }
        
        
    }

