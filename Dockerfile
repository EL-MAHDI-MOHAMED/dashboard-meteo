FROM eclipse-temurin:17-jdk-jammy

# Versions
ENV SPARK_VERSION=3.5.7
ENV HADOOP_VERSION=3
ENV SPARK_HOME=/opt/spark
ENV PATH="$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin"

# Installer Python + curl (nécessaire pour télécharger Spark)
RUN apt-get update && apt-get install -y curl python3 python3-pip bash procps && apt-get clean

# Télécharger Spark 3.5.7
RUN curl -L https://dlcdn.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
    | tar -xz -C /opt/ \
    && mv /opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} $SPARK_HOME

# Corrige le problème "python: No such file or directory"
RUN ln -s /usr/bin/python3 /usr/bin/python

# Créer le répertoire des logs
RUN mkdir -p $SPARK_HOME/logs

WORKDIR $SPARK_HOME