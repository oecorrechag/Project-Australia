# Project-Australian

# <center> Application of RFM

**RFM** es la abreviatura de Recency, Frequency y Monetary. 
Es una técnica que ayuda a determinar las estrategias de marketing y ventas en función de los hábitos de compra de los clientes.

  * Recency: Ultima compra en días
  * Frequency: Número de compras
  * Monetary: Total de dinero gastado

<a href="https://drive.google.com/uc?export=view&id=1reVlQHim8OTvoKDjDj68ktt3b-Rg_Upl"><img src="https://drive.google.com/uc?export=view&id=1reVlQHim8OTvoKDjDj68ktt3b-Rg_Upl" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture"/>

# Diseño de experimento:

Se simulo 100.000 transacciones con las siguientes caracteristicas:

   * Tiempo de 2 años
   * 1000 clientes
   * 1000 articulos
   * 5 posibles precios (valores)

# Problema

Se tienen transacciones de una tienda, y queremos saber quienes son nuestros mejores clientes, para realizar campañas personalisadas.

# Objetivo

Clasificacion rapida de los clientes de la tienda. [Clusters por indicadores]

# Resultados y conclusiones

Using rfm v1:

- New Customers             0.28 <br>
- Need Attention            0.20 <br>
- About to Sleep            0.18 <br>
- Potential higt            0.11 <br>
- Hibernating               0.07 <br>
- Champions                 0.05 <br>
- At Risk                   0.05 <br>
- New Customers higt        0.02 <br>
- Potential low             0.02 <br>
- Unique higt - Promising   0.01 <br>

Se obtiene que dados los parametros dados para la simulacion, de nuestros clientes 17281 (52%) se encuentran en categorias bajas y 15723 (48%) en categorias altas. Dados estos grupos se podran realizar campañas de mercadeo dirigidas y particulares.

Using rfm v2:

- 1         0.13 <br>
- 2         0.14 <br>
- 3         0.19 <br>
- 4         0.10 <br>
- 5         0.10 <br>
- 6         0.10 <br>
- 7         0.18 <br>
- 8         0.06 <br>

note: numbers of groups was random.


# Bibliografia

Busra Y. (Jul 6, 2020). RFM Analysis for Customer Segmentation. Medium. Recuperado de:  
https://medium.com/@yamanbsr/rfm-analysis-for-customer-segmentation-29c8c7e04f5c
Application of RFM