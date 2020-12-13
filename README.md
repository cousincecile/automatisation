# **Automatisation Infrastructure De Données**

Ce repos recense les codes sources, et les builds Spark permettant la mise en place de l'architecture et de l'automatisation de traitement et de stockage de données.

Le repos permettant l'automatisation notamment via Airflow est ici : https://github.com/kmalki/automatisation_airflow

Comme expliqué par mail, et sur le repos d'Airflow, nos jobs Spark fonctionnent à 100% sur notre edgenode, de la récupération des données brutes de Spotify, à l'écriture dans Hive en passant par la case transformation en parquet.

Par contre, nous avons une erreur que nous n'avons pas réussi à corriger lors de l'automatisation d'Airflow au stade de l'écriture dans Hive. Après avoir googlé l'erreur, nousn n'avous pu trouvé de plus amples informations.

`[2020-12-11 15:22:53,690] {bash_operator.py:157} INFO - 	 diagnostics: User class threw exception: org.apache.spark.sql.AnalysisException: org.apache.hadoop.hive.ql.metadata.HiveException: Unable to fetch table spotify_playlists. Invalid method name: 'get_table_req';
`

Le reste de l'automatisation fonctionne. C'est la seule étape qui ne fonctionne pas dans notre automatisation Airflow.

Fraicheur des données : Dimanche 13 décembre 2020
Partitions : 3 => 11/12/13 décembre 2020
