# Crear un cluster básico
databricks clusters create --json '{
  "cluster_name": "mi-cluster-produccion",
  "spark_version": "13.3.x-scala2.12",
  "node_type_id": "Standard_DS3_v2",
  "autoscale": {
    "min_workers": 2,
    "max_workers": 8
  },
  "autotermination_minutes": 60,
  "spark_conf": {
    "spark.speculation": true
  }
}'