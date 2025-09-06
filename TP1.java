
import java.util.Scanner;

public class HolaMundo {
    
 
    public static void main(String args[]) {
         //Punto 2 Unidad 1
        System.out.println("¡Hola, Java!");
        
        
        //Punto 3 Unidad 1 
        
    String nombre = "Martin";
    int edad = 32;
    double altura = 1.61;
    boolean estudiante = true;

System.out.println(nombre + "\n" + edad + "\n" + altura + "\n" + estudiante);

        
        //Punto 4 Unidad 1
        
       
        
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Ingrese su nombre: ");
        
        String nombreUsuario = sc.nextLine();
        
        System.out.println("Ingrese su edad");
        int edadUsuario = Integer.parseInt(sc.nextLine()) ;
        
        System.out.println("Nombre: " + nombreUsuario + "\n" + "Edad: " + edadUsuario);
      
        
        //Punto 5 Unidad 1
        
        
        
        System.out.println("Ingrese el numero 1: ");
        
        int numero1 = Integer.parseInt(sc.nextLine());
                
        System.out.println("Ingrese el numero 2: ");
        
        int numero2 = Integer.parseInt(sc.nextLine());
        
        int suma = numero1 + numero2;
        int resta = numero1 - numero2;
        int multiplicacion = numero1 * numero2;
        double division = numero1 / numero2;
        
        
        System.out.println("Suma: " + suma + "\n" + "Resta: " + resta + "\n" + "Multiplicacion: " + multiplicacion + "\n" + "Division: " + division);
        
        
        //Punto 6 Unidad 1
        
        String nombrePunto6 = "Juan Pérez";
        int edadPunto6 = 30;
        String direccionPunto6 = "Calle Falsa 123";
        
        System.out.println("Nombre: " + nombrePunto6 + "\n" + "Edad: " + edadPunto6 + "\n" + "Direccion: " + "\"" + direccionPunto6 + "\"");
        
        
        /**Punto 7 Unidad 1
         * 
         * En el código dado, cada línea es una instrucción porque realiza una acción: la línea 1 declara e inicializa la variable x, 
         * la línea 2 asigna un nuevo valor a x y la línea 3 imprime el valor de x en pantalla. 
         * Dentro de estas instrucciones hay expresiones, que son fragmentos de código que producen un valor: en la línea 1, 10 es una expresión literal; 
         * en la línea 2, x + 5 es una expresión que calcula un valor;
         * y en la línea 3, x es una expresión que representa el valor de la variable. 
         * La diferencia principal es que las expresiones devuelven un valor, mientras que las instrucciones ejecutan una acción.
         */
        
        
        //Punto 8 Unidad 1 
        
        //Punto a
        
        System.out.println("Punto a");
        
         System.out.println("Ingrese un numero entero: ");
        
        int numeroEntero1_a = Integer.parseInt(sc.nextLine());
                
        System.out.println("Ingrese otro numero entero: ");
        
        int numeroEntero2_a = Integer.parseInt(sc.nextLine());
        
        
        int divisionPunto8_a = (numeroEntero1_a / numeroEntero2_a);
        
        System.out.println("Division: " + divisionPunto8_a);
        
        //Punto b
        
        System.out.println("Punto b");
        
         System.out.println("Ingrese un numero entero: ");
        
        double numeroEntero1_b = Integer.parseInt(sc.nextLine());
                
        System.out.println("Ingrese otro numero entero: ");
        
        double numeroEntero2_b = Integer.parseInt(sc.nextLine());
        
        
        double divisionPunto8_b = (numeroEntero1_b / numeroEntero2_b);
        
        System.out.println("Division: " + divisionPunto8_b);
        
        //Conclusion: cargando varios valores, note que con int el resultado se redondea hacia abajo al entero más cercano y con double, el resultado conserva los decimales y es más preciso.
        
        
        //Punto 9 Unidad 1
        
        //El error radica en el momento que se declara e inicializa la variable "nombre", dado que se declara como una cadena de caracteres pero se pide ingresar como un numero entero, la solucion seria ingresarla ocmo un string cn el comando "scanner.nextLine()"
    }
}
