## 1.Sea $A$ y $B$ subconjuntos de $R$, $A \ne \emptyset$ y $B\ne \emptyset$, acotados. Sea $C=\{a-b \ |\ a \in A \text { y } b \in B\}$. Probar que $sup \ C = sup \ A - inf \ B$

Supongamos que $A$ tenga superior y $B$ tenga inferior. Si $c \in C$, entonces $c= a-b$, donde $a \in A$ y $b \in B$. Por consiguiente $c = sup \ A - inf \ B$; de modo que $sup \ A - inf \ B $ es una cota superior de $C$. esto demuestra que $C$  tiene extremo superior y que $sup \ C = sup \ A - inf \ B $.

Sea ahora $n$ un entero positivo cualquiera. Según las Propiedades fundamentales del extremo superior tenemos: 

Existe un $a$ en $A$ y un $b$ en $B$ tales que $a>sup \ A - 1/n$, y  $inf \ B+1/n>b$

Sumando la desigualdad obtenemos que 
$$
a+inf \ B + 1/n>sup \ A - 1/n + b \\
a- b + 1/n>sup \ A - 1/n - inf \ B \\
a- b >sup \ A - 1/n - inf \ B -  1/n\\
a- b >sup \ A - inf \ B -  2/n\\
$$
O bien $sup \ A - inf \ B < a-b+2/n \le sup \ C+ 2/n$ puesto que $a-b\le sup \ C$. Por consiguiente hemos demostrado que
$$
sup \ C \le sup \ A - inf \ B < sup \ C + 2/n
$$
 para todo entero $n\ge 1$. En virtud del principio de Arquímedes, debe de ser $sup \ C = sup \ A - inf \ B$.

## 2. Sea $S= \{1/n +1 | n \in \N\}$

### a) ¿Tiene $S$ ínfimo?En caso afirmativo encontrarlo y demostrar que es el ínfimo

Como $S=\{ 2, 1\ \frac{1}{2}, 1 \ \frac{1}{3}, ... \}$ para $n \in \N$

   * **Demostración que $S$ no tiene mínimo**

     Supongamos que $\alpha = min \ S$, por lo tanto
     $$
     \alpha \le 1/n +1 \ \forall n \in \N, \ \ \ \alpha \in S
     $$
     Entonces existe $m \in \N$ tal que $\alpha = 1/m$

     Como 
     $$
     m +1 > m \\
     1/(m+1) < 1/m = \alpha
     $$
      Pero $1/(m+1) \in S$, por lo que contradice que $\alpha$ sea el mínimo, por lo tanto no tiene mínimo.

   * **Demostrar que $inf \ S = 1$**

     Como $1 < 1/n +1 \ \forall n \in \N$ 

     Entonces $1$ es la cota inferior de $S$

     Sea $\beta$ cualquier cota inferior de $S$ por demostrar $\beta \le 1$

     Supongamos que $\beta > 1 $. Por ser cota inferior de $S$ tenemos $\beta < 1/n+1 \ \forall n \in \N$

     Por el principio de Arquímedes tenemos que existe $m \in \N$ tal que $1/\beta < m$ donde $1 < 1/m < \beta$, pero $1/m \in S$, lo cual contradice que $\beta$ sea cota inferior de $S$.

     Entonces $\beta \le 1$ por lo tanto tenemos que $inf \ S = 1$

### b) ¿Tiene $S$ supremo?En caso afirmativo encontrarlo y demostrar que es el supremo

**Demostración $max \ S = 2 = sup \ 2$**

Como $S=\{ 2, 1\ \frac{1}{2}, 1 \ \frac{1}{3}, ... \}$ para $n \in \N$

Por lo tanto $1 < 1/n + 1 \le 2$

La cota superior es $2$ y como $2 \in S$ entonces $max  \ S = 2 = sup \ S$



