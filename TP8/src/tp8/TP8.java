package tp8;

import java.io.*;

public class TP8 {

    static class EdadInvalidaException extends Exception {
        public EdadInvalidaException(String msg) { super(msg); }
    }

    static void validarEdad(int edad) throws EdadInvalidaException {
        if (edad < 0 || edad > 120) throw new EdadInvalidaException("Edad fuera de rango: " + edad);
    }

    public static void main(String[] args) {

        System.out.println("== 1) Division segura ==");
        try {
            int a = 10, b = 0;
            int r = a / b;
            System.out.println("Resultado: " + r);
        } catch (ArithmeticException e) {
            System.out.println("Error: divisor en cero.");
        }

        System.out.println("\n== 2) Parse de entero ==");
        String texto = "12x";
        try {
            int n = Integer.parseInt(texto);
            System.out.println("OK: " + n);
        } catch (NumberFormatException e) {
            System.out.println("Entrada inválida: " + texto);
        }

        System.out.println("\n== 3) Lectura de archivo ==");
        try {
            BufferedReader br = new BufferedReader(new FileReader("no_existe.txt"));
            System.out.println(br.readLine());
            br.close();
        } catch (FileNotFoundException e) {
            System.out.println("Archivo no encontrado.");
        } catch (IOException e) {
            System.out.println("Error de E/S: " + e.getMessage());
        }

        System.out.println("\n== 4) Excepcion personalizada ==");
        try {
            validarEdad(150);
            System.out.println("Edad válida.");
        } catch (EdadInvalidaException e) {
            System.out.println("Error: " + e.getMessage());
        }

        System.out.println("\n== 5) Try-with-resources ==");
        String ruta = "archivo.txt";
        try (BufferedReader br = new BufferedReader(new FileReader(ruta))) {
            String linea;
            while ((linea = br.readLine()) != null) {
                System.out.println(linea);
            }
        } catch (IOException e) {
            System.out.println("Problema leyendo el archivo: " + e.getMessage());
        }
    }
}
