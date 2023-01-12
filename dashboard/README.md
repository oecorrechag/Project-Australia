# Project-Australia

# <center> Application of RFM - Kmeans - Kmedoids

**RFM** RFM is abbreviation for Recency, Frequency and Monetary. It is a technique that helps determine marketing and sales strategies based on customers' buying habits.

  * Recency: Time passed since the customer's last purchase.
  * Frequency: Total number of purchases.
  * Monetary:  Total spending by the customer.

<a href="https://drive.google.com/uc?export=view&id=1reVlQHim8OTvoKDjDj68ktt3b-Rg_Upl"><img src="https://drive.google.com/uc?export=view&id=1reVlQHim8OTvoKDjDj68ktt3b-Rg_Upl" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture"/>

# Diseño de experimento:

100,000 transactions were simulated with the following characteristics:

   * Space of time: 2 years
   * Number of clients: 33.004
   * Number of products: 24
   * Number of products prices: 5

# Problema

There are transactions from a store, we want to know who are our best customers, and determine marketing and sales strategies.

# Objetivo

Quick sorting of shop customers.

# Resultados y conclusiones

Using rfm:

- 8. Champions                 0.11 <br>
- 7. Potential                 0.27 <br>
- 6. New Customers higt        0.13 <br>
- 5. New Customers             0.11 <br>
- 4. Need Attention            0.09 <br>
- 3. At Risk                   0.14 <br>
- 2. About to Sleep            0.08 <br>
- 1. Hibernating               0.04 <br>

**RFM-score** (from best to worst) as: 8-7-6-5-4-3-2-1

Using kmeans:

- 0. Champions         0.40 <br>
- 1. Hibernating       0.11 <br>
- 2. New Customers     0.22 <br>
- 3. Potential         0.26 <br>

**Kmeans** (from best to worst) as: 0-3-2-1

note: numbers of groups was random.

Using kmedoids:

- 0. Champions         0.39 <br>
- 1. Potential         0.23 <br>
- 2. Hibernating       0.13 <br>
- 3. New Customers     0.24 <br>

**kmedoids** (from best to worst) as: 0-1-3-2

note: numbers of groups was random.

APP: https://segmentation-project.onrender.com

# Bibliografia

Busra Y. (Jul 6, 2020). RFM Analysis for Customer Segmentation. Medium. Recuperado de:  
https://medium.com/@yamanbsr/rfm-analysis-for-customer-segmentation-29c8c7e04f5c
Application of RFM