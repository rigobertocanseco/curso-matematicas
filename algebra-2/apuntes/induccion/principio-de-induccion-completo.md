**Principio de inducción matemático, $PI$**

Sea $P(n)$ un enunciado en el dominio de los números naturales.
	i. $P(0)$ es verdadera y 
	ii. Para todo $n\in \N$, $P(n)$ es verdadera, entonces $P(n+1)$ es verdadera  

Entonces $P(n)$ es verdadera parar todo $n \in \N$

**Principio de inducción fuerte(completo), $PIF$**

Sea $P(n)$ un enunciado en el dominio de los números naturales.
	i. $P(0)$ es verdadera y 
	ii. Para todo $n\in \N$, Si $P(1),...,P(n-1),P(n)$ son todas verdaderas, entonces $P(n+1)$ es verdadera  

Entonces $P(n)$ es verdadera parar todo $n \in \N$ 

**$\bf {PIC \Rightarrow PI}$**

El principio de inducción completo implica el principio de inducción 

El enunciado $C$ se deduce a partir del enunciado $A$, y esto a su vez puede deducir al enunciado $C$ a partir del enunciado $A$ con alguna otra hipótesis adicional $B$.
$$
(A\Rightarrow C) \Rightarrow (A\and B \Rightarrow C) \equiv \text{Tautología}
$$
 Donde 
$$
A= P(n),\quad B=P(0)\and P(1) \and ... \and P(n-1) \quad \text y \quad C = P(n+1)
$$
Es decir, se puede usar el $PI$ para demostrar $PIC$. Supongamos que asumimos como cierto el $PI$ y queremos demostrar $PIC$. 

Sea $P(n) \in \N$ que satisface *(i)* y *(ii)*.

Queremos demostrar que $P(n)$ es verdadero para todo $n \in \N$, usando solo $PI$.

Para esto creamos otro enunciado $Q(n)$ tal que
$$
Q(n) = P(0)\and P(1) \and ... \and P(n)
$$
 Tenemos que $Q(1) = P(1)$ y por *(ii)* 
$$
Q(n) \Rightarrow P(n+1)
$$
Pero sabemos que 
$$
Q(n) =P(1) \and P(2) \and...\and P(n)
$$
y también conocemos $P(n+1)$

Entonces conocemos 
$$
P(1)\and P(2) \and ... \and P(n) \and P(n+1) = Q(n+1)
$$
Entonces $Q(1)$ se cumple y para todo $n$, $Q(n) \Rightarrow Q(n+1)$

Entonce por el principio de inducción, $Q(n)$ se cumple para toda $n$ por tanto, $P(n)$ se cumple para todo $n$ 

