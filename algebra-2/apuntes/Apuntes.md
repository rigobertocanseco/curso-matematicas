# Álgebra superior II

***

## Temas

1. [Operaciones binarias](#operaciones-binarias)
2. [Estructuras albegraicas](#estructuras-algebraicas)

### [Operaciones binarias](#operaciones-binarias)

> **Definición:** Sea $A$ un conjunto no vacío. Una *operación binaria* en $A$ es una función $f:A \times A$.

Observemos que:

1. El domino de $f$ es $A\times A$ y, al ser función debe estar bien definida, es decir, la operación asigna un elemento de $A$ a todo par de elementos de $A$.
2. Por ser función. $f$ asigna solamente un elemento a cada pareja.

Decimos entonces que una operación binaria es una regla que asocia a cada par ordenado de elementos de $A$, un único elemento de $A$.

Las operaciones binarias son muy usadas y estudiadas en matemáticas.

Existe la convención de no denotarlas como funciones, es decir, en lugar de referirnos a la imagen de la pareja $(a,b)$ como $f(a,b)$, le llamamos
$$
a*b
$$
En conjuntos numéricos lo más común es usar $+$ para indicar suma y $*$ para el producto, pero aunque se usen estos símbolos, no siempre representan a la suma y el producto como los conocemos.

Otra convención, es llamarlas simplemente "operaciones" esto es porque las operaciones binarias son las más comunes, aunque también existen las operaciones "unarias" *de un argumento*, terciarias *tres elementos*, *n-arias para n argumentos*. En este curso solamente estudiaremos operaciones binarias por lo que generalmente les llamaremos, operaciones.

$$
a*b \in A, \forall \ a, b \in A
$$

Esta propiedad se llama **cerradura** de la operación $*$ también se dice que la operación $*$ es **cerrada**. Observa que, al haber definido la operación como función, la cerradura se cumple por definición, así si no es cerradura, no es operación binaria.

> **Definición:** Sean $A$ un conjunto no vacío, $*$ una operación en $A$, y $\emptyset \ne B \subseteq A$, diremos que $B$ es **cerrado bajo** $*$ si:
> $$
> \forall x,y \in B \to x*y\in B
> $$
> Llamamos **la restricción de $*$ sobre $B$** a la operación inducida por $*$ en $B$

* Observa la diferencia entre decir que \* es cerrada y que $B$ es cerrado bajo * 

* Si $B$ no es cerrado bajo \* entonces su restricción sobre $B$ no es una operación binaria en $B$

<div style="background:#f4f4f4">
    <b>Ejemplos:</b>
</div

1. La suma y el producto usuales en $\N$, $\Z$, $\Q$ y en $\R$ son operaciones

2. La división $\div$ en $\R$ no es operación pues por ejemplo $12\div0$, ni está definido

3. La resta $-$ en $\N$ no es operación pues por ejemplo $2-5 \notin  \N$

4. En $\Z$ definimos $a*b$ como un número menor que $a$ y $b$ ¿esta es una operación binaria? *Sí*

5. En $\Z$ definimos $a*b = max\{a.b\}$¿esta es una operación binaria? 

6. Sea $A$ un conjunto no vacío y definamos en $P(A)$ las operaciones:

   1. $V*_\cup W = V \cup W$
   2. $V*_\cap W = V \cap W$

   ¿Son operaciones binarias?

> **Definición:** *Sea $A$ un conjunto no vacío y una  operación en él. Diremos que:*
>
> 1. $*$ Es asociativa si $\forall \ a,b,c \in A \to (a*b)*c = a*(b*c)$
> 2. $*$ Es conmutativo si $\forall \ a,b,c \in A \to a*b = b*a$
> 3. $x \in A$ es un **neutro** de la operación si $\forall \ a \in A \to x*a = a*x=a$

En los ejercicios de operaciones que hemos visto, ¿cuáles son asociativas?¿cuáles son conmutativas? ¿alguna tiene neutro?

Sobre conjuntos finitos con pocos elementos, es fácil definir operaciones binarias mediante el uso de una tabla. Así por ejemplo, si $A=\{a\}$, definimos $a*a=a$ y la describimos con la siguiente tabla
$$
\begin{array} 
{|r|r|}
\hline * & a \\ 
\hline a & a \\ 
\hline  
\end{array}
$$
Ahora, sea $C= \{a,b,c\}$, definimos la operación $*$ con la siguiente tabla:
$$
\begin{array} {|r|r|r|r|}
\hline * & a & b & c \\ 
\hline a & a & b & c \\
\hline b & b & c & a \\
\hline c & c & b & a \\
\hline
\end{array}
$$
Con esta taba estamos indicando el resultado de la operación tomando como primer argumento la fila de la tabla y como segundo argumento la columna.

<div style="background:#f4f4f4"><b>Ejercicios</b></div>

1. Revisa si las operaciones de las tablas son asociativas, conmutativas o tienen neutro.

   $C= \{a,b,c\}$, definimos la operación $*$ con la sigueinte tabla:
   $$
   \begin{array} {|r|r|r|r|}
   \hline * & a & b & c \\ 
   \hline a & a & b & c \\
   \hline b & b & c & a \\
   \hline c & c & b & a \\
   \hline
   \end{array} \\
   a*a=a \quad a*b=b \quad a*c=c \\
   b*a=b \quad b*b=c \quad  b*c=a \\
   c*a=c \quad c*b=b \quad c*c=a
   $$

   * Neutro $a$ 
   * No conmutativa por  $b*c=a$ y $c*b=b$,
   * Asociativa

   $$
   a*(b*c) = (a*b)*c \\
     a*b = b*c \\
     b \neq a
   $$

2. Si $B=\{a,b\}$, define todas las posibles operaciones binarias en $B$ y haz las tablas correspondientes.  

   

<div style="background:#f4f4f4"><b>Ejercicios</b></div>

1. Sean $A$ un conjunto, $B$ un subconjunto de $A$ y $*$ una operación en $A$. ¿Qué es la operación inducida por $B$?¿Bajo qué condiciones tiene sentido hablar de esta operación?

$$
     A = \{a, b\} \\
     B = \{a\}
$$

2. ¿La asignación $f(a,b)=a/b$ define una operación en $\Q$? 

   Sí

3. Determina si la operación definida en la última tabla es asociativa y/o conmutativa y si existe algún neutro de la operación.

4. Sea $A$ un conjunto no vacío, y sea $f:A \times A \to  A$ definida como $f(a,b)=a$. Determina si $f$ es asociativa, conmutativa y si existe algún neutro para $f$(Ojo¿qué pasa si $A$ tiene sólo un elemento?, considere ambos casos)

***

### [Estructuras algebraicas](#estructuras-algebraicas)

> **Definición:** Si $A$  es un conjunto y $*$ es una operación binaria sobre $A$, llamaremos **estructura algebraica binaria(o magma)** al par $\langle A,*\rangle$.

Un conjunto no determina una estructura algebraica por si solo, pues con cada operación distinta que se pueda definir sobre él, se tendrá una estructura distinta.

> **Definición:** Si $A$ es un conjunto y $*$ es una operación binaria sobre $A$, diremos que $\langle A, * \rangle$ es un **semigrupo** si $*$ es una operación asociativa.

<div style="background:#f4f4f4">
   <b>Ejercicios:</b>
</div>

Para los siguientes pares $\langle A, * \rangle$, determina cuáles son semigrupos.

1. Sean $A=\N$, y $*:A\times A \to A$ definida como $n*m=2n+m \ \forall n,m \in \N$.
2. Sean $X$ un conjunto, $A=P(X)$ y $*$ definida como $B*C=B\cap C \quad \forall B,C \in P(X)$.
3. Sean $X$ un conjunto y $A=\{ f \subseteq X \times X | f \ \text{es una función}\}$ y sea $*$ definida como la composición entre funciones $(f*g=f\circ g)$.

***

> **Definición:** Si $A$ es un conjunto y $*$ es una operación binaria sobre $A$, diremos que $\langle A, *\rangle$ es un **monoide** si:
>
> * $*$ es una operación asociativa.
> * $\exist \ e \in \ A \text{ tal que } e*a = a*e=a \quad \forall a \in A$, e se llama **neutro** de $*$ en $A$.
>
> Un monoide es un semigrupo con elemento neutro.

<div style="background:#f4f4f4">
    <b>Ejercicios:</b>
</div>

Determina cuales son los monoides

1. Sean $A = \N \setminus \{\emptyset\}$, y $*: A \times A \to A$ definida como $n*m=n \cdot m \quad \forall n, m \in \N$ (el producto usual en $\N$).
2. Sean $X$ un conjunto, $A=P(X)$ y $*$ definida como $B*C= B \cup C \quad \forall B,C \in P(X)$.
3. Sea $A = \R$ y sea $*$ definida como $a*b=0 \quad \forall a, b \in \R$.
4. Define una magma que no sea semigrupo y un semigrupo que no sea monoide.

***

> **Definición:** Si $A$ es un conjunto y $*$ es una operación binaria sobre $A$, diremos que $\langle A, * \rangle$ es un **grupo** si:
>
> * $*$ es una operación asociativa
> * $\exist \ e \ in A \mid e*a = a*e =a \quad \forall a \in A, e$ se llama **neutro** de $*$ en $A$
> * $\forall x \in A, \exist y \in A \mid x *y = y*x=e$
>
> Además, diremos que el el grupo es **abeliano** si la operación * es conmutativa*

Si sucede $x*y=e$ decimos que $y$ es un **inverso derecho de $x, y$** y que $x$ es un **inverso izquierdo** de y. Cuando $x*y=y*x=e$, decimos que $y$ es un **inverso de** $x$(y, evidentemente, $x$ es un inverso de $y$) Observa que un grupo es un monoide en donde cada elemento tiene un inverso.

<div style="background:#f4f4f4">
    <b>Ejemplos:</b>
</div>

1. Si $A$ es un conjunto cualquiera el conjunto de todas las funciones biyectivas de $A$ en $A$ forma un grupo con la composición de funciones. La función identidad en $A$ sería un elemento neutro (y es una función biyectiva), y para cada biyectiva $f, f^{-1}$ sería el inverso de $f$ en el grupo. ¿Es un grupo abeliano?

2. El conjunto de los número enteros forma un grupo abeliano con la suma: la suma en $Z$ es asociativa y conmutativa. El cero sería un neutro y para cada número entero $a, -a$ es su inverso respecto a la suma, pues $a+(-a)=0$.

3. Sea $A=\{0,1\}$, y definimos $\bigoplus$ como $1\bigoplus1=0, \ 0\bigoplus0=0, 1\bigoplus0=0\bigoplus1=1$. Entonces $\langle A, \bigoplus \rangle$ es un grupo abeliano. El $0$ es el neutro del grupo y $1$ es su propio inverso, la operación es claramente conmutativa.  

> **Teorema 1.1:** Sea $\langle G, *\rangle$ es un grupo. Entonces, existe un único elemento neutro del grupo.
>
> **Demostración:** Por definición, sabemos que existe al menos un elemento neutro $x_0 \in G$. Supongamos que $y_0 \in G$ es otro neutro del grupo, y nuestro objetivo será demostrar que $x_0 = y_0$. Como $x_0$ es un neutro de $*$ en $G$ y $y_0 \in G$, tenemos que.
> $$
> x_0*y_0 = y_0*x_0 = y_0 \text{ en partuclar } y_0 = x_0 * y_0 \tag{1}
> $$
>
> Deforma análoga $y_0$ también es neutro en $G$ y $x_0$ es un elemento de $G$, entonces:
> $$
> x_0 = x_0*y_0 \tag{2}
> $$
> Por lo tanto, de $\eqref{1}$ y $\eqref{2}$ tenemos que 
> $$
> x_0 =x_0*y_0 = y_0 \\
> x_0 = y_0 \quad \blacksquare
> $$

<div style="background:#f4f4f4">
    <b>Ejercicios:</b>
</div>

Demostrar la unicidad de los inversos.

>**Definición:** Sea $\langle G, *\rangle$ un grupo. Diremos que $H \subseteq G$ es un **subgrupo** si $\langle H, *|_H \rangle$ es un grupo. Denotamos como $H \leq G$ la proposición "$H$ es un subgrupo de $G$"

Un **subgrupo** de un grupo $G$ es un subgrupo $H$ de $G$ de forma que $H$ es **cerrado** bajo $*$ y $\langle H, *\rangle$ es un grupo con la misma operación $*$ restringida a $H$.

Notemos que en caso de que $H$ no fuera cerrado bajo $*$, la restricción $*|_H$ no sería una función de $H \times H $ en $H$, pues habría un par de elementos $a,b \in H$ tales que $a*b \notin H$, por lo que $*|_H$ no sería una operación binaria en $H$, y entonces $\langle H,*|_H \rangle$ no podría ser grupo. Entonces, decir que $H$ es cerrado bajo $*$ es equivalente a decir que $*|_H$ es una operación binaria en $H$.

En todas las estructuras algebraicas podemos definir lo que es una **subestructura** de la misma forma. Por ejemplo, un *submonoide* de un monoide $M$, sería un subconjunto de $M$ que sea cerrado bajo la operación del monoide, y que a su vez cumpla la definición de monoide con la misma operación. El trabajo con subestructuras es muy común en el estudio de las estructuras algebraicas (y en las matemáticas en general), y analizando su comportamiento y características se obtiene mucha información sobre la estructura algebraica.

***

<div style="background:#f4f4f4">
    <b>Ejemplos:</b>
</div>

1. Sabemos que $\langle \N, \cdot \rangle$ es un monoide, entonces $A=\{2^k | k \in \N \}$ sería un submonoide de $\N$

   **Demostración:** 1 es el único elemento neutro del producto en $N$, por lo tanto lo que cualquier submonoide de $\N$ debe tener al $1$ como elemento, en este caso, $1=2^0$ por lo que $1 \in A$. Por otro lado, sean $a = 2^k$ y $b=2^l$ dos elementos arbitrarios de $A$, entonces:
   $$
   a\cdot b= (2^k)(2^l)=2^{k+l} \text{ en donde k + l } \in \N
   $$
   Por lo tanto, para cualquier par de elementos $a,b$ de $A$ es un submonoide de $\N$.

2. Sabemos que $\langle \Z, + \rangle$ es un grupo abeliano. Entonces $A=\{3k | k \in \Z\}$ es un subconjunto (abeliano) de $\langle \Z, + \rangle$.

3. Sea $G$ el grupo de todas las funciones biyectivas $R$ en $R$ usando la composición de funciones como operación. Entonces el conjunto $A = \{f \in G | f(0) = 0 \}$ es un subgrupo de $G$.

   **Demostración:** La función identidad, $I$ es el elemento neutro de $G$, por lo que debemos comprobar que la identidad  es elemento de $A$. Claramente $I(0)= 0$. por lo que $I \in A$. Ahora, sean $f,g\in A$, entonces:
   $$
   0 = I(0) = (f^{-1} \circ f)(0) = f^{-1}(f(0)) = f^(-1)(0) 
   $$
   Por lo tanto, $\langle A, \circ \rangle$ es un grupo, es decir que $A$ es un subgrupo de $G$

***

<div style="background:#f4f4f4">
    <b>Ejercicios:</b>
</div>

1. Sea $X$ un conjunto. Sea $G = \mathcal{P}(X)$, el conjunto potencia de $X$. Sea $*:G \times G \to G$ definida como:
   $$
   A*B= A \cap \quad \forall A,B \in P(X)
   $$
   ¿Qué tipo de estructura forma el par $\langle G, *\rangle?$ Describe todas las propiedades que encuentre.

2. Sea $\langle G, * \rangle$ un grupo abeliano y sea $x \in G$. demuestra que el inverso de $x$ respecto a $*$ es único.¿Existen grupos en donde los inversos no sean únicos?

3. Sea $G = \{a,b\}$. ¿Cuántos grupos distintos se pueden definir en $G$?

4. Sea $G=\{a,b,c\}$. Define un par de operaciones $*_1$ y $*_2$ de forma que $\langle G, *_1\rangle$ sea un grupo abeliano pero $\langle G, *_2 \rangle$ sea un grupo no abeliano, y que $a$ sea el neutro en ambos grupos.

***


