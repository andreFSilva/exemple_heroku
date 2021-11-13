from django.db import models


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data_admissao = models.DateField()
    data_demissao = models.DateField(null=True, blank=True)
    salario = models.DecimalField(max_digits=7, decimal_places=2)
    cargo = models.ForeignKey('Departamento', on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return self.nome


class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nome