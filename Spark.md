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
