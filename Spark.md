Ejemplo do Spark
path = "C:/Users/BlueShift/Documents/Spark Treinamento/Dia 1/rddExample.csv"
rdd1 = sc.textFile(path)

rdd1.count()

rdd1.toDebugString()

rdd1.take(2)

rdd1Total = sc.wholeTextFiles(path)

rdd1 = sc.textFile(path)


def filtro_header(x):
    return 'id|first_name|last_name|email|gender|ip_address' != x


rdd2 = rdd1.filter(filtro_header)

header = rdd1.take(1)[0]

rdd3 = rdd2.map(lambda x: x.split("|"))

rdd4 = rdd3.keyBy(lambda x: x[4])

rdd4.countByKey().items()


rdd5 = rdd4.groupByKey()

rdd5.map(lambda x: (x[0], len(x[1]))).collect()

df = spark.read.csv(path, sep='|', header=True)

df.show()

# TASK 1: Tratamentos iniciais
#1. Relacionar o Json de usuários com o csv de usuários pelo campo "id"#
#Declarar el camino
pathJason = path + "users_json.json"
#Permitir la lectura
dfJson = spark.read.json(path + "users_json.json")



#Importar el directorio necesario  

from pyspark.sql.types import *
from pyspark.sql.functions import *


#Definir el camino de los archivos
path = "C:/Users/BlueShift/Documents/Spark Treinamento/Dia 2/"
pathCSV = path + "users_info.csv"
pathJson = path + "users_json.json"


#Definir el schema 
from pyspark.sql.types import * 
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("first_name", StringType(), True),
    StructField("last_name", StringType(), True),
    StructField("gender", StringType(), True),
    StructField("vip", StringType(), True),
    StructField("balance", DecimalType(20,2), True),
    ])

#Definir el schema a ser usado por el dfCSV

dfCSV = spark.read.csv(pathCSV, schema=schema, header=True, sep=",")

#Definir el schema a ser usado por el JSON

dfJson = spark.read.json(pathJson, multiLine=True)
dfJson2 = dfJson.select("Users.*")

#Combinar com a outra tabela 
UsersJoin = dfJson2.join(dfCsv, "id")
UsersJoin1 = UsersJoin.fillna({'balance': 0})

UsersNaoVIP = UsersJoin1.where(UsersJoin1.vip == "false")
UsersSimVIP = UsersJoin1.where(UsersJoin1.vip == "true")
#NOTA:
#Recuerda mostrar los archivos, cada vez que sea necesario para poder comprobar que la información este correcto. 

UsersSimVIP.show()
UsersNaoVIP.show()

#etc
#----
