package tp3;

public class NaveEspacial {
    private String nombre;
    private int combustible;
    private int capacidadMaxima = 100; // tope de combustible

    public void despegar() {
        if (combustible > 0) {
            System.out.println(nombre + " despegó.");
        } else {
            System.out.println("No hay combustible para despegar.");
        }
    }

    public void avanzar(int distancia) {
        if (combustible >= distancia) {
            combustible = combustible - distancia;
            System.out.println(nombre + " avanzó " + distancia + " unidades.");
        } else {
            System.out.println("Combustible insuficiente para avanzar " + distancia);
        }
    }

    public void recargarCombustible(int cantidad) {
        if (combustible + cantidad > capacidadMaxima) {
            combustible = capacidadMaxima;
            System.out.println("Se recargó al máximo (" + capacidadMaxima + ")");
        } else {
            combustible = combustible + cantidad;
            System.out.println("Recarga exitosa. Combustible actual: " + combustible);
        }
    }

    public void mostrarEstado() {
        System.out.println("Nave: " + nombre + " | Combustible: " + combustible + "/" + capacidadMaxima);
    }

   
    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getCombustible() {
        return combustible;
    }
    public void setCombustible(int combustible) {
        this.combustible = combustible;
    }

    public int getCapacidadMaxima() {
        return capacidadMaxima;
    }
    public void setCapacidadMaxima(int capacidadMaxima) {
        this.capacidadMaxima = capacidadMaxima;
    }
}
