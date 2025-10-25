
package tp8;

public class TarjetaCredito implements PagoConDescuento {
    private final String nro;
    private final double descuentoPct;

    public TarjetaCredito(String nro, double descuentoPct) {
        this.nro = nro;
        this.descuentoPct = descuentoPct;
    }

    @Override
    public double aplicarDescuento(double monto) {
        return monto * (1 - descuentoPct / 100.0);
    }

    @Override
    public boolean procesarPago(double monto) {
        System.out.println("Pagando con Tarjeta " + nro + " por $" + monto);
        return true;
    }
}
