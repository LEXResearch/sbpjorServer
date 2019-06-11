from django.db import models

# classes auxiliares

# diz qual evento um trabalho faz parte
class Evento(models.Model):
    titulo = models.CharField(max_length=250)

    def __str__(self):
        return self.titulo

# diz qual a categoria da atividade, para informar a cor no app
class CategoriaAtividade(models.Model):
    titulo = models.CharField(max_length=250)
    cor_hex = models.CharField(max_length=250)
    cor_nome = models.CharField(max_length=250)
    cor_background = models.CharField(max_length=250)

    def __str__(self):
        return self.titulo

# classes principais

# define o cronograma
class Cronograma(models.Model):
    titulo = models.CharField(max_length=250)
    data = models.DateTimeField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.titulo

# define os dias do cronograma
class Dia(models.Model):
    dia = models.IntegerField()
    semana = models.CharField(max_length=3)
    cronograma = models.ForeignKey(Cronograma, related_name="dias", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.dia) + " " + self.semana

# define as atividades do dia
class Atividade(models.Model):
    dia = models.ForeignKey(Dia, related_name="atividades", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=250)
    descricao = models.TextField()
    local = models.CharField(max_length=250)
    hora = models.DateTimeField()
    categoria = models.ForeignKey(CategoriaAtividade, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

# define as mesas da atividade, podendo uma atividade não ter nenhuma mesa relacionada
class Mesa(models.Model):
    numero = models.IntegerField()
    titulo = models.CharField(max_length=250)
    coordenada = models.BooleanField()
    descricao = models.TextField(blank=True)
    atividade = models.ForeignKey(Atividade, related_name="mesas", on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

# define os trabalhos da mesa
class Trabalho(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    numero = models.IntegerField()
    titulo = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    autores = models.CharField(max_length=250)
    mesa = models.ForeignKey(Mesa, related_name="trabalhos", on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
