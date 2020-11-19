# Tarea 2

1. **¿Cuáles de las siguientes proposiciones son verdaderas y cuáles falsas?**

Justifique su respuesta.

1. $\empty \in \empty$ **Falso**. El conjunto vacío no contiene elementos por lo tanto el $\emptyset \notin \emptyset $.
2. $\empty \notin \empty$ **Verdadero**. Ningún elemento está contenido en el conjunto vacío. 
3. $\empty \subseteq \empty$ **Verdadero**. Podemos ver la contención como, todos los elementos del conjunto $A$ están contenidos en el conjunto $B$, es decir $A \subseteq B$. Por vacuidad el conjunto vacío está contenido es si mismo. 
4. $\empty \subset \empty$  **Verdadero**. Podemos ver la contención como, todos los elementos del conjunto $A$ están contenidos en el conjunto $B$, es decir $A \subseteq B$. Por vacuidad el conjunto vacío está contenido es si mismo.
5. $\empty \in \{\empty\}$ **Verdadero**. El conjunto unitario del vacío tiene un  elemento, a el vacío.
6. $\empty \notin \{\empty\} $ **Falso**. El vacío es elemento del conjunto unitario del vacío  
7. $\empty \subset \{\empty\}$ **Verdadero**. El vacío está contenido en el conjunto unitario del vacío. 
8. $\empty \subseteq \{\empty\} $ **Verdadero**. El vacío está contenido en el conjunto unitario del vacío. 
9. $\empty = \{\{\empty\}\}$ **Falso**. Podemos ver que el conjunto unitario del unitario del vacío contiene un elemento a el unitario del vacío, mientras que el vacío no tiene elementos.  
10. $\{\{\empty\}\} \subseteq \{\{\empty\},\empty\}$ **Verdadero**. El unitario del unitario del vacío está contenido en el conjunto que contiene al unitario del vacío y al vacío.   
11. $\empty=\{\emptyset\}$ **Falso**: El unitario del vacío contiene al vacío, mientras que el vacío no contiene elementos.
12. $\{\{\empty\}, \empty\} \subseteq \{\empty,\{\empty\},\{\{\empty\}\}\}$ **Verdadero**. El unitario del vacío y el vacío se encuentran contenidos en el conjunto que contiene a el vacío, a el unitario del vacío y a el unitario del unitario del vacío.  
13. $\{\{\empty\},\empty\}\in \{\empty,\{\empty\},\{\{\empty\}\}\}$ **Falso**. El conjunto que está compuesto por el unitario del vacío y el vacío no es elemento del conjunto que contiene a el vacío, a el unitario del vacío y a el unitario del unitario del vacío.

2. **Demuestre usando dos esquemas diferentes de prueba que $A \subseteq C$ si y sólo si $A\cup(B\cap C)=(A\cup B)\cap C$**

*Prueba directa*
$$
\begin{split}
A \cup (B\cap C) \\
&= x \in A \or (x\in B \and x \in C) \\
&= x \in A \or x\in B \and x \in A \or x \in C \quad \text {Distribución} \\
&= (A \cup B) \cap(A \cup C) \\
\text {Como } A \subseteq C\text { por lo tanto }& A\cup C = C \text {, tenemos que } \\
&= (A \cup B) \cap C \quad \blacksquare
\end{split}
$$


3. **Diferencia de conjuntos. Sean $A,B,C$ conjuntos, Muestre los siguientes hechos**

* $A\setminus B=(A\cup B)\setminus B$
  $$
  \begin{split}
  A \setminus B &= (A \cup B) \setminus B\\
  &= (x\in A \or x \in B)\and x \notin B  \\
  &= (x\notin B \and x\in B) \or (x\notin B \and x \in A) \quad \text {Distribución} \\
  &= \bot \or (x\notin B \and x \in A)\\
  &= x\notin B \and x \in A \\
  &= x \in A \and  x\notin B \\
  &= A \setminus B
  \end{split}
  $$

  $$
  \begin{split}
  (A \cup B) \setminus B &=A \setminus B\\
  &= x \in A \and  x\notin B \\
  &= (x\notin B \and x\in B) \or (x \in A \and x\notin B)\quad \bot \or p\equiv p\\
  &= (x\in A \or x \in B)\and x \notin B \quad \text {Distribución}\\
  &= (A \cup B) \setminus B
  \end{split}
  $$

  

* $(A\setminus C)\setminus (B\setminus C) = (A \setminus B)\setminus C$
  $$
  \begin{split}
  (A\setminus C)\setminus (B\setminus C) &= (A \setminus B)\setminus C \\
  &= (x \in A \and  x\notin B) \and\notin C \\
  &= (x \in A \and  x\notin B \and x \notin C) \\
  &= (x \in A  \and x\notin B  \and  x\notin C) \or (x \in A  \and x \in C\and  x\notin C)\\
  &=( x \in A  \and x\notin B \or x \in A  \and x \in C )\and  x\notin C\\
  &= x \in A  \and (x\notin B \or x \in C) \and  x\notin C\\
  &= (x \in A \and  x\notin C) \and (x\notin B \or x \in C) \\
  &= (x \in A \and  x\notin C) \and \neg (x\in B \and x\notin C) \\
  &= (A\setminus C)\setminus (B\setminus C) 
  \end{split}
  $$

  $$
  \begin{split}
  (A \setminus B)\setminus C &= (A\setminus C)\setminus (B\setminus C)\\
  &= (x \in A \and  x\notin C) \and \neg (x\in B \and x\notin C) \\
  &= (x \in A \and  x\notin C) \and (x\notin B \or x \in C) \\
  &= x \in A  \and (x\notin B \or x \in C) \and  x\notin C\\
  &=( x \in A  \and x\notin B \or x \in A  \and x \in C )\and  x\notin C\\
  &= (x \in A  \and x\notin B  \and  x\notin C) \or (x \in A  \and x \in C\and  x\notin C)\\
  &= (x \in A  \and x\notin B  \and  x\notin C) \or \bot \\
  &= x \in A  \and x\notin B  \and  x\notin C  \\
  &=(A \setminus B)\setminus C 
  \end{split}
  $$

  

4. **Sean $A,B,C,D$ conjuntos. Demuestre especificando el tipo de prueba usada los siguientes hechos**

* $(A\times C)\cap(B\times D)=(A \cap B)\times(C\cap D)$ 
  $$
  \begin{split}
  (A\times C)\cap(B\times D)&=(A \cap B)\times(C\cap D) \\
  &= (x,y) \in (A \cap B)\times(C\cap D)  \\
  &= (x \in A \and x \in B)\and(y \in C \and y \in D) \\
  &= x \in A \and x \in B\and y \in C \and y \in D \\
  &= (x \in A \and y \in C) \and (x \in B\and  y \in D) \\
  &= (x,y) \in A \times C \and (x,y) \in B \times D \\
  &= (A \times C) \cap (B \times D)
  \end{split}
  $$

  $$
  \begin{split}
  (A \cap B)\times(C\cap D) &= (A\times C)\cap(B\times D)\\
  &= (x,y) \in A \times C \and (x,y) \in B \times D \\
  &= (x \in A \and y \in C) \and (x \in B\and  y \in D) \\
  &= x \in A \and x \in B\and y \in C \and y \in D \\
  &= (x \in A \and x \in B)\and(y \in C \and y \in D) \\
  &= (x,y) \in (A \cap B)\times(C\cap D)  \\
  &= (A \cap B)\times(C\cap D)
  \end{split}
  $$

  

* $(A\times C)\cup(B\times D)=(A \cup B)\times(C\cup D)$ Muestra que es posible que no se dé la igualdad
  $$
  \begin{split}
  (A\times C)\cup(B\times D)&=(A \cup B)\times(C\cup D) \\
  &(x,y) \in (A\cup B) \times(C \cup D) \iff\\
  &(x \in A \or x \in B) \and (y \in C \or y \in D) \iff\\
  &(x \in A \or x \in B) \and (y \in C \or y \in D) \Rightarrow\\
  &(x \in A \and y \in C) \or (x\in B \and y \in D) \Rightarrow \\
  &(x,y) \in A \times C \cup (x,y) \in B \times D  \Rightarrow \\
  &(A \times C )\cup (B \times D )
  \end{split}
  $$

  $$
  \begin{split}
  (A \cup B)\times(C\cup D) &= (A\times C)\cup(B\times D)\\
  &((x,y) \in A\times C) \cup ((x,y) \in B \times D) \iff\\
  &(x \in A \and y \in C) \or (x \in B \and y \in D) \iff\\
  &(x \in A \or x \in B) \and (y \in C \or y \in D)  \Rightarrow\\
  &(x,y)\in( A \cup  B) \times ( C \cup D)  \Rightarrow \\
  &( A \cup  B) \times ( C \cup D) 
  \end{split}
  $$

  

5. **Sean $\{A_i:i\in I\}$ y $\{B_j:j\in J\}$ familias indexadas de conjuntos. Muestre que $[ \bigcap_{i\in I} A_i ]\times[ \bigcap_{j\in J} B_j ]= \bigcap\{A_i\times B_j:(i,j)\in I\times J\} $**

* Sea $(x,y) \in \left[ \bigcap_{i\in I} A_i \right]\times\left[ \bigcap_{j\in J} B_j \right]$ , entonces $x \in \left[ \bigcap_{i\in I} A_i \right] \and y\in \left[ \bigcap_{j\in J} B_j \right]$, donde $\forall i_0 \in I$ y $\forall j_0 \in J$ tales que, $ x \in A_{i_0}$ , y $ y \in B_{j_0}$. Como
  $(i_0,j_0) \in I \times J$, $\forall(i_0,j_0) \in I \times J$ tal que $x \in A_{i_0}$ y  $y \in B_{j_0}$, donde $(x,y) \in  \bigcap\{A_i\times B_j:(i,j)\in I\times J\}$
* Sea $(x,y)\in  \bigcap\{A_i\times B_j:(i,j)\in I\times J\} $, entonces $\forall(i_0,j_0) \in I\times J$ tal que $(x,y)\in A_{i_0}  \times  B_{j_0}$, es decir $\forall i_0 \in I$, $x \in  A_{i_0}$ y $\forall j_0 \in J, y \in B_{j_0}$, es decir $x \in [ \bigcap_{i\in I} A_i ] \and y\in [ \bigcap_{j\in J} B_j ]$ , y $(i_0,j_0)\in I \times J$, donde $(x,y) \in \left[ \bigcap_{i\in I} A_i \right]\times\left[ \bigcap_{j\in J} B_j \right]$

6. **Sean $f:A \to B$ y $g:B\to C$ funciones. Pruebe que si $C'\subseteq C$, entonces $(g\circ f)^{-1}(C')=f^{-1}(g^{-1}(C'))$**

$$
(g\circ f)^{-1}=(g\circ f)=\{(x,z):\exist y \text{ para el cual }(x,y) \in g, (y,z) \in f\} \\
=((x,z):\exist y \text{ para el cual }(x,y) \in g, (y,z) \in f )^{-1}(C') \\
=x\in A:(x,y)\in g,\text{ para algún } y \in C' \\
\\ \ \\

f^{-1}(C')=x \in A: (x,y)\in f, \text{ para algún } y \in C' \\
=x \in A : f(x) \in C' 
\\ \ \\
g^{-1}(C')=x \in B: (x,y)\in g, \text{ para algún } y \in C' \\
f^{-1}(x \in B: (x,y)\in g, \text{ para algún } y \in C')
$$



7. **Sean $f:A \to B$ y $g:B \to C$ funciones**

* Si $g\circ f$ es inyectiva, qué se puede decir de la inyectividad de $f$ y $g$ 
  La función $f$ es inyectiva pero $g$ no necesariamente lo es.

  Como $g\circ f$ es inyectiva. Para demostrar de que la función $f$ es inyectiva se sigue a continuación:

  Consideremos a $x_1,x_2 \in A$ tales que $f(x_1)=f(x_2)$. Notemos que $f(x_1),f(x_2) \in B$ pues $Ran(f)=B$. Así evaluando la función $g$ obtenemos $g(f(x_1))=g(f(x_2))$, es decir $(g \circ f)(x_1)=(g\circ f)(x_2)$.

  Como sabemos que $(g\circ f)$ es inyectiva, obtenemos que $x_1=x_2$, por lo tanto $f$ también es inyectiva

  

* Si $g\circ f$ es sobreyectiva, qué se puede decir de la sobreyectividad de $f$ y $g$
  Entonces $g$ es sobreyectiva pero $f$ no necesariamente lo es.
  Como $g\circ f$ es sobreyectiva.  Para demostrar de que la función $g$ es sobreyectiva se sigue a continuación:

  Consideremos  $\forall y\in B, \  \exist x \in A$ tal que $y=g(x)$.  Notemos que $x \in A$ pues $Dom(g)=A$. Así evaluando la función $f$ obtenemos $y=g(f(x))$, es decir $(g\circ f)(x)=y$.

  Como sabemos que $(g\circ f)$ es sobreyectiva, obtenemos que $y=f(x)$, por lo tanto 
  
  
  Una función $f: A \to B$ es sobreyectiva si, $\forall y\in B, \  \exist x \in A$ tal que $y=f(x)$ 

8. **Sean $f: A \to B$ y $g: B \to C$ funciones. Demostrar que existe una función $h: B \to C$ tal que $f=h \circ g$ si y sólo si para cada $x,y \in A \ g(x)=g(y)$ implica $f(x)=f(y)$.**

9. **Brinde los siguientes ejemplos:**

* Dar un ejemplo de una función que tenga inversa izquierda pero no inversa derecha
* Dar un ejemplo de una función que tenga inversa derecha pero no inversa izquierda 

10. **Muestre que si $f:A \to B$ y $g:B \to C$ son funciones biyectivas, entonces $(g \circ f) ^{-1} = f^{-1}\circ g^{-1}$**

    Una función se dice biyectiva si cumple que es una función inyectiva y sobreyectiva

    * Una función $f: A \to B$ es inyecta si, $\forall x_1,x_2 \in A$ tal que $x_1\ne x_2 \Rightarrow f(x_1) \ne f(x_2)$
    * Una función $f: A \to B$ es sobreyectiva si, $\forall y\in B, \  \exist x \in A$ tal que $y=f(x)$ 

11. **Las funciones $f$ y $g$ son compatibles si y sólo si $f|_{dom \ f\cap dom \ g} = g|_{dom \ f \cap dom \ g}$, donde para $h:A \to B$, y $A' \subseteq A$, $h|_{A'}=\{(x,y):x \in A' \}$**

