
package tp8;

import java.util.ArrayList;
import java.util.List;

public class Pedido implements Pagable {
    private final List<Producto> productos = new ArrayList<>();
    private EstadoPedido estado = EstadoPedido.NUEVO;
    private final Cliente cliente;

    public Pedido(Cliente cliente) { this.cliente = cliente; }

    public void agregarProducto(Producto p) {
        productos.add(p);
        notificar("Se agregó el producto: " + p.getNombre());
    }

    @Override
    public double calcularTotal() {
        return productos.stream().mapToDouble(Producto::calcularTotal).sum();
    }

    public void cambiarEstado(EstadoPedido nuevo) {
        this.estado = nuevo;
        notificar("Estado del pedido: " + estado);
    }

    private void notificar(String msg) {
        if (cliente != null) cliente.notificar(msg);
    }

    public boolean pagar(Pago pago) {
        double monto = calcularTotal();
        if (pago instanceof PagoConDescuento) {
            monto = ((PagoConDescuento) pago).aplicarDescuento(monto);
        }
        boolean ok = pago.procesarPago(monto);
        if (ok) cambiarEstado(EstadoPedido.PAGADO);
        return ok;
    }
}
