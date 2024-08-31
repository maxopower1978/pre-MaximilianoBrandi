from django.db import models


class Cliente(models.Model):
    """Alta de clientes"""

    dni = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=30, blank=True, null=True)

    # class Meta:
    #     verbose_name = 'ModelName'
    #     verbose_name_plural = 'ModelNames'

    def __str__(self):
        return (
            f"{self.apellido}, {self.nombre} ({self.dni}) - Telefono: {self.telefono}"
        )


class Asesoramiento(models.Model):
    """Alta de asesoramientos en derechos"""

    derecho = models.CharField(max_length=30, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    disponible = models.BooleanField(default=True)

    # class Meta:
    #     '''Meta definition for ModelName.'''

    #     verbose_name = 'ModelName'
    #     verbose_name_plural = 'ModelNames'

    def __str__(self):
        return f"{self.derecho}: {self.descripcion}"


class Cita(models.Model):
    """Muestra la agenda de citas"""

    class Estado(models.TextChoices):
        """Estado de la cita"""

        PENDIENTE = "PENDIENTE", "Pendiente"
        AGENDADA = "AGENDADA", "Agendada"
        ATENDIDO = "ATENDIDO", "Atendido"

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    derecho = models.ForeignKey(Asesoramiento, on_delete=models.CASCADE)
    motivo_consulta = models.TextField()
    fecha_solicitud = models.DateField(auto_now_add=True)
    fecha_cita = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    estado = models.CharField(
        max_length=20, choices=Estado.choices, default=Estado.PENDIENTE
    )

    def __str__(self):
        return f"{self.cliente} - solicito asesoramiento en {self.derecho} - Consultando por: {self.motivo_consulta}, y quiere una cita para el {self.fecha_solicitud} / Agendada {self.fecha_cita} {self.hora}- Estado: {self.estado}"
