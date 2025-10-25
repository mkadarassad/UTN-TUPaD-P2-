
package tp8;

public class PayPal implements Pago {
    private final String cuenta;

    public PayPal(String cuenta) { this.cuenta = cuenta; }

    @Override
    public boolean procesarPago(double monto) {
        System.out.println("Pagando con PayPal (" + cuenta + ") por $" + monto);
        return true;
    }
}
