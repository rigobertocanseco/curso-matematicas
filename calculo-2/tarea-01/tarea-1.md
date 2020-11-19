# Cálculo diferencial e integral II

## Tarea 1

##### 1. Si $A=(a, b)$, probar que $A$ no tiene mínimo y sí tienen ínfimo,  $inf \space A = a$.  

   * **Demostración: De que $A$ no tiene mínimo.**

     Si $x \in A$ entonces existe $c$ y es el mínimo, $min A = c$, entonces $c \in (a, b)$ y $c \le x \  \forall x \in (a, b)$.

     Como $c \in(a,b)$ y $a<c$ por lo tanto podemos encontrar un elemento medio en $a$ y $c$ , tenemos que:
     $$
     a < (a+c)/2 < c
     $$
     Esto además es menor a $b$
     $$
     a<(a+c)/2<c<b
     $$
      Como $(a+b)/2$ pertenece al conjunto $A$ , es decir, $(a+c)/2 \in (a,b)$ y además 
     $$
     (a+c)/2 < c
     $$
     Contradicción, porque existe otro elemento del conjunto $A$ que es menor a  $C$, y nosotros habíamos considerado  $c$  cómo el mínimo, por lo tanto no tiene mínimo. 

   

   * **Demostración: De que $A$ tiene ínfimo $inf \ A = a$.**

     Si $x \in A$ entonces $a<x<b$, y se encuentra acotado superiormente por $b$ e inferiormente por $a$.

     Supongamos que existe otra cota inferior de $A$, que llamaremos $\alpha$ , por lo tanto $\alpha \le x \ \forall x \in A$ y además $\alpha > a$.

     Tenemos que $a<\alpha <b$, ahora consideremos un elemento medio en $a$ y $\alpha$
     $$
     a < (a+\alpha)/2 < \alpha < b
     $$
     Como $(a+\alpha)/2 \in A$ y además $(a+\alpha)/2 < \alpha $ encontramos otra cota inferior, lo cual es una contradicción ya que $\alpha$ era cota inferior.

     Por lo tanto $\alpha \le a$ y es la mayor cota inferior. Por lo tanto $inf \  A = a$.

   

##### 2. Si $A=(a, b)$, probar que $A$ no tiene máximo y sí tiene supremo, $sup \space A=b$.

   * **Demostración de que $A$ no tiene máximo.**

     Si $x \in A$ entonces $a<x<b$ se encuentra acotado inferiormente por $a$ y superiormente por $b$.

     Supongamos que existe $c$ y es el máximo, $max \ A = c$entonce $c\ge x \ \forall x \in (a, b)$.

     Como $c \in (a,b)$ por lo tanto $c<b$, podemos encontrar un elemento medio en $c$ y $b$, por lo tanto tenemos que:
     $$
     c< (c+b)/2 <b
     $$
     Además $a<c<(c+b)/2<b$

     Como $(c+b)/2 \in A$ y además encontramos $(c+b)/2>c$, lo cual es una contradicción por que existe otro elemento del conjunto $A$ que es mayor a $c$, y se había considerado a $c$ como el máximo.

     Por lo tanto $A$ no tiene máximo.

   

   * **Demostración de que $A$ tiene supremo, $sup \ A =b$** 

     Si $x \in A$ entonces $a<x<b$, donde $A$ se encuentra acotado inferiormente por $a$  y superiormente por $b$.

     Supongamos que existe una cota superior en $A$ que llamaremos $\beta$, por lo tanto $\beta \ge x \ \forall x \in A$ y además $beta <b$.

     Tenemos que $a<\beta<b$, ahora consideramos un elemento medio en $\beta$ y $b$,
     $$
     a<\beta < (\beta+b)/2 < b
     $$
      Como $(\beta + b)/2 \in A$ y además $(\beta+ b)/2>\beta$ encontramos otra cota superior.

     Lo anterior es una contradicción, ya que $\beta$ era cota superior.

     Por lo tanto $\beta\ge b$ y es la mínima cota superior, $sup \ A = b$.

   

##### 3. Probar que si $S$ tienen mínimo entonces $S$ tiene ínfimo y $inf \ S = min \ S$.    

   * **Demostración de que $inf \ S = min  \ S$**

     Si $x \in S$ y además $a \le x \le b $, como $a= min \ S$, entonces $a \in S$ y $x \ge a \ \forall x \in S$.

     Supongamos que existe $c$ que es $inf \ S$ es decir, $inf \ S=c$, como es el ínfimo cumple que:

     * $c$ es una cota inferior de $S$
     * ningún número mayor que $c$ es cota inferior para $A$

     Por lo tanto tenemos que, $x \ge c \ \forall x \in S$ y $c \in S$, entonces,

      $x \ge a$ y $x \ge c$, por lo tanto $a, c$ debe de ser los mismo.

     $a = c$

     Tenemos que el $inf \ S = a$ y $a = min \ S$. Por lo tanto queda demostrado que $inf \ S = min \ S$.

     

##### 4. Probar que el ínfimo de un conjunto es único.

   * **Demostración**

     Sean $a$ y $a'$ dos extremos inferiores(ínfimos) para el conjunto $L$ por lo tanto cumple que ningún número mayor que $a$ es cota inferior para $L$, $a \le a'$ 

     Pero también cumple que ningún número mayor que $a'$ es cota inferior para $L$, $a'\le a$. 

     Por lo tanto $a=a'$

     

##### 5. Probar que el axioma de ínfimo implica el teorema del supremo

   * **Axioma del ínfimo:** *Todo conjunto $L \in \R, L \ne \emptyset$ acotado inferiormente tiene ínfimo, es decir, existe $a \in \R$ tal que $a = Inf \ L$.*

   * **Teorema del supremo:** *Todo conjunto no vacío $L \in \R$, acotado superiormente tiene supremo, es decir, existe $c$ tal que $c \in \R, c= sup \ L$.* 

   * **Demostración:**

     Sea $-L = \{ x | x \in L\}$ y $L \ne \emptyset$, como $L$ está acotado superiormente existe $N \in \R$ tal que
     $$
     N \ge x \ \forall x \in L \\
     -N \le -x \ \forall x \in L 
     $$
     El conjunto $-L$ está acotado inferiormente por el axioma del ínfimo existe $\beta$ es el ínfimo de $-L$, es decir $\beta = inf(-L)$.

     Por demostrar $-\beta = sup \ L$

     Como $\beta = inf(-L)$ entonces
     $$
     -x \ge \beta \ \forall x \in L \\
     x \le -\beta \ \forall x \in L
     $$
     Es decir $-\beta$ es cota superior de $L$. Por probar que es la mínima cota superior

     Sea $\alpha$ una cota superior de $L$, entonces
     $$
     \alpha \ge x \ \forall x \in L \\
     -\alpha \le -x \ \forall x \in L
     $$
     Es decir, $-\alpha$ es cota inferior de $-L$. Como $\beta = inf(-L)$ entonces $\beta$ es la mayor de las cotas inferiores de $-L$.
     $$
     \beta \ge \alpha \\
     -\beta \le - \alpha
     $$
     Entonces $-\beta$ es la menor de las cotas superiores, es decir $-\beta = sup \ L$

     Entonces $-\beta$ es la $c$ que buscábamos, $c= sup \ L$.

   

##### 6. Probar que:

   * $inf \space (A+B) = inf \space A + inf \space B$   

     Si $x \in C$ entonces $x = a + b$ con $a \in A$ y $b \in B$ por lo tanto tenemos que $inf A \le a$ y $inf B \le b$
     $$
     inf A + inf B \le a+b = x
     $$
     Es decir $inf \ A + inf \ B$ es cota inferior de $C$ por lo tanto $C$ tiene ínfimo y además
     $$
     inf \ A + inf \ B \le inf \ C \space\space\space\space\space (1)
     $$
     Sea ahora $n$ un número positivo cualquiera, según el teorema que dice: *Sea $h$ un número positivo dado y $S$ un conjunto de números reales.*

     * *Si $S$ tiene ínfimo, para un cierto $x$ de $S$ se tiene $x \le inf \ S + h$*

     Tenemos un $h= 1/n$ y existe un $a$ en $A$ y un $b$ en $B$ tales que
     $$
     a < inf \ A + 1/n \ \ \ \ \ , \ \ \ \ \ b < inf \ B + 1/n
     $$
     Sumando las desigualdades
     $$
     a+b < inf \ A + inf \ B + 2/n
     $$
     Es igual a 
     $$
     -2/n + inf \ C \le - 2/n + a+b< inf \ A + inf \ B \\
     -2/n + inf \ C< -2/n + a+b < inf \ A + inf \ B \\
     -2/n < inf \ A + inf \ B - inf \ C \ \ \ \ \ (2)
     $$
     Utilizando la ecuación (1) y (2) tenemos que 
     $$
     -2/n < inf \ A + inf \ B - inf \ C \le 0
     $$
     Es igual a
     $$
     0 \le -inf \ A - inf \ B + inf \ C < 2/n
     $$
     Para todo $n \in \N$ y $n>1$

     Por lo tanto $inf \ C = inf \ A + inf \ B$

   * $inf \space cA = c inf \space A \qquad si \space c>0$   

     Sea $c > 0$, 
     $$
     a \ge inf \ A \ \forall a \in A \\
     c a \ge c inf \ A \ \forall a \in A
     $$
     $cinf \ A$ es una cota inferior de $cA$ por lo tanto $inf \ cA \ge cinf \ A \ \ \ (1)$ 

     Como 
     $$
     ca \ge inf \ cA \\
     a \ge 1/c \ inf \ cA 
     $$
     Tenemos que $1/c \ inf \ cA$ es una cota inferior de $A$, por lo tanto
     $$
     inf \ A \ge 1/c inf \ cA \\
     c \ inf \ A \ge inf \ cA \ \ \ \ \ (2)
     $$
     Por lo tanto $inf \ cA = c \ inf \ A$

     

   * $inf \space cA = c inf \space A \qquad si \space c>0$

     Sea $c < 0$, 
     $$
     sup \ A \ge a \ \forall a \in A \\
     c \ sup \ A \le ca \ \forall a \in A
     $$
     Donde $c \ sup \ A$ es cota inferior de $cA$, entonces
     $$
     inf \ c \ A \ge c \ sup \ A \ \ \ \ (1) 
     $$
     Tenemos que 
     $$
     ca \ge inf \ cA \ \forall a \in A \\
     a \le 1/c \ inf \ cA
     $$
     Donde $1/c \ inf \ cA$ es cota superior de $A$, entonces
     $$
     1/c \ inf \ cA \\
     inf \ cA \le c \ sup \ A \ \ \ \ (2)
     $$
     De la desigualdad (1) y (2) tenemos que
     $$
     inf \ cA \ge c \ sup \ A
     inf \ cA \le c \ sup \ A
     $$
     Por lo tanto $inf \ cA = c\ sup \ A$

     

##### 7. Sea $S = \{ \frac{1}{n} -1 \mid n \in \mathbb{N}\}$. Encontrar, si existen: el máximo, el mínimo, el supremo y el ínfimo. Probar las afirmaciones. 

   * **Demostración $max \ S = 0 = sup \ 0$**

     Como $S=\{ 0, -1/2, -2/3, -3/4, ... \}$ para $n \in \N$

     Por lo tanto $-1 < 1/n - 1 \le 0$

     La cota superior es $0$ y como $0 \in S$ entonces $max  \ S = 0 = sup \ S$

   * **Demostración que $S$ no tiene mínimo**

     Supongamos que $\alpha = min \ S$, por lo tanto
     $$
     \alpha \le 1/n -1 \ \forall n \in \N, \ \ \ \alpha \in S
     $$
     Entonces existe $m \in \N$ tal que $\alpha = 1/m$

     Como 
     $$
     m +1 > m \\
     1/(m+1) < 1/m = \alpha
     $$
      Pero $1/(m+1) \in S$, por lo que contradice que $\alpha$ sea el mínimo, por lo tanto no tiene mínimo.

   * **Demostrar que $inf \ S = -1$**

     Como $-1 < 1/n -1 \ \forall n \in \N$ 

     Entonces $-1$ es la cota inferior de $S$

     Sea $\beta$ cualquier cota inferior de $S$ por demostrar $\beta \le -1$

     Supongamos que $\beta > -1 $. Por ser cota inferior de $S$ tenemos $\beta < 1/n-1 \ \forall n \in \N$

     Por el principio de Arquímides tenemos que existe $m \in \N$ tal que $1/\beta < m$ donde $-1 < 1/m < \beta$, pero $1/m \in S$,lo cual contradice que $\beta$ sea cota inferior de $S$.

     Entonces $\beta \le -1$ por lo tanto tenemos que $inf \ S = -1$