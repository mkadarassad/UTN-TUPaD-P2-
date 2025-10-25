
package tp8;

public class Cliente implements Notificable {
    private final String nombre;
    private final String email;

    public Cliente(String nombre, String email) {
        this.nombre = nombre;
        this.email = email;
    }

    @Override
    public void notificar(String mensaje) {
        System.out.println("[Notificación a " + nombre + "] " + mensaje);
    }
}
