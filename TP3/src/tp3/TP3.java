package tp3;

public class TP3 {
    public static void main(String[] args) {
        Estudiante estudiante = new Estudiante();
        estudiante.setNombre("Lucía");
        estudiante.setApellido("Gómez");
        estudiante.setCurso("Programación II");
        estudiante.setCalificacion(6);

        estudiante.mostrarInfo();

        System.out.println("\nSubiendo calificación +2...");
        estudiante.subirCalificacion(2);
        estudiante.mostrarInfo();

        System.out.println("\nBajando calificación -3...");
        estudiante.bajarCalificacion(3);
        estudiante.mostrarInfo();

     
        System.out.println("\nNombre del estudiante: " + estudiante.getNombre());
        
        
        Mascota m1 = new Mascota();
        m1.setNombre("Roco");
        m1.setEspecie("Perro");
        m1.setEdad(3);

        m1.mostrarInfo();

        System.out.println("\nCumpliendo años...");
        m1.cumplirAnios();
        m1.mostrarInfo();

        
        Libro libro = new Libro();
        libro.setTitulo("Martin Fierro");
        libro.setAutor("José Hernández");

        libro.setAnioPublicacion(3000); // inválido → no cambia
        libro.setAnioPublicacion(1879); // válido

        libro.mostrarInfo();

    }
}
