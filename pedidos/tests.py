from django.test import TestCase
from django.contrib.auth import get_user_model
from tienda.models import Producto
from .models import Pedido, LineaPedido

User = get_user_model()


#Test clase Pedido y clase LineaPedido

class PedidoModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.producto = Producto.objects.create(
            nombre="Producto de prueba", precio=10.0
        )
        self.pedido = Pedido.objects.create(user=self.user)

    def test_pedido_creation(self):
        self.assertIsInstance(self.pedido, Pedido)
        self.assertEqual(self.pedido.__str__(), str(self.pedido.id))

    def test_pedido_total(self):
        LineaPedido.objects.create(
            user=self.user, producto=self.producto, pedido=self.pedido, cantidad=2
        )
        self.assertEqual(self.pedido.total, 20.0)


class LineaPedidoModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.producto = Producto.objects.create(
            nombre="Producto de prueba", precio=10.0
        )
        self.pedido = Pedido.objects.create(user=self.user)
        self.linea_pedido = LineaPedido.objects.create(
            user=self.user, producto=self.producto, pedido=self.pedido, cantidad=2
        )

    def test_linea_pedido_creation(self):
        self.assertIsInstance(self.linea_pedido, LineaPedido)
        self.assertEqual(
            self.linea_pedido.__str__(),
            f"{self.linea_pedido.cantidad} unidades de {self.linea_pedido.producto.nombre}",
        )
