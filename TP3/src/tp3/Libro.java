package tp3;

import java.time.Year;

public class Libro {
    private String titulo;
    private String autor;
    private int anioPublicacion;

    // --- Getters requeridos ---
    public String getTitulo()          { return titulo; }
    public String getAutor()           { return autor; }
    public int getAnioPublicacion()    { return anioPublicacion; }

    // --- Setters (con validación en año) ---
    public void setTitulo(String titulo) { this.titulo = titulo; }
    public void setAutor(String autor)   { this.autor = autor; }

    public void setAnioPublicacion(int anio) {
        int actual = Year.now().getValue();
        // rango razonable para libros impresos
        if (anio >= 1450 && anio <= actual) {
            this.anioPublicacion = anio;
        } else {
            System.out.println("Año inválido: " + anio + ". Debe estar entre 1450 y " + actual + ".");
        }
    }

    // ayuda para mostrar
    public void mostrarInfo() {
        System.out.println("Título: " + titulo);
        System.out.println("Autor: " + autor);
        System.out.println("Año: " + anioPublicacion);
    }
}
