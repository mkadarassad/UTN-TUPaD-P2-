public class Empleado {

    // Atributos
    private int id;
    private String nombre;
    private String puesto;
    private double salario;

    // Atributos de clase
    private static int totalEmpleados = 0;
    private static int nextId = 1;
    private static final double SALARIO_POR_DEFECTO = 100000.0;

  

    // Constructor con todos los atributos
    public Empleado(int id, String nombre, String puesto, double salario) {
        this.id = id;
        this.nombre = nombre;
        this.puesto = puesto;
        this.salario = salario;
        totalEmpleados++;
    }

    // Constructor con  solo nombre y puesto (id auto + salario por defecto)
    public Empleado(String nombre, String puesto) {
        this.id = nextId++;
        this.nombre = nombre;
        this.puesto = puesto;
        this.salario = SALARIO_POR_DEFECTO;
        totalEmpleados++;
    }

    // Getters y setters
    public int getId() { return id; }

    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }

    public String getPuesto() { return puesto; }
    public void setPuesto(String puesto) { this.puesto = puesto; }

    public double getSalario() { return salario; }
    public void setSalario(double salario) { this.salario = salario; }

    //aumenta por porcentaje
    public void actualizarSalario(int porcentaje) {
        salario = salario + salario * (porcentaje / 100.0);
    }

    // aumenta por monto fijo
    public void actualizarSalario(double montoFijo) {
        salario = salario + montoFijo;
    }

    
    @Override
    public String toString() {
        return "Empleado{id=" + id
                + ", nombre='" + nombre + '\''
                + ", puesto='" + puesto + '\''
                + ", salario=" + salario + "}";
    }

   
    public static int mostrarTotalEmpleados() {
        return totalEmpleados;
    }
}
