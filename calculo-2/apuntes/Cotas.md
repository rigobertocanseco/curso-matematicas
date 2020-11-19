# Axioma del supremo



## Superior de un conjunto, elemento máximo, extremo superior

Sea $S$ un conjunto no vacío de números reales y supongamos que existe un número $B$ tal que: $x \le B$ para todo $x$ de $S$. Entonces decimos que $S$ está **acotado superiormente** por $B$.

$$
S \in \R, \exists B \mid \forall x\{ x \in S , x \le B \}
$$

El número $B$ se denomina una **cota superior para $S$**. Decimos una cota superior debido a que todo número mayor que $B$ también es una cota superior.

Si una cota superior $B$ pertenece a $S$, entonces $B$ se le llama el elemento **máximo de $S$**, si existe se escribe $B = max \ S$ .

Así que $B = max \ S$ si $B \in S$ y $x \le B$ para todo $x$ de $S$. Un conjunto sin cota superior se dice que es no acotado superiormente.

Ejemplos:

1. Sea $S$ el conjunto de todos los números reales $x$ tales que $0\le x \le 1$ . Este conjunto está acotado superiormente por el $1$. Su elemento máximo es $1$.
  
2. Sea $S$ el conjunto de todos los números reales positivos. Es un conjunto no acotado superiormente. No contiene cota superior ni máximo.
  
3. Sea $T$ el conjunto de todos los números reales $x$ tales que $0 \le x < 1$. Este conjunto está acotado superiormente por el $1$ pero no tiene elemento máximo.


Algunos conjuntos, parecidos al ejemplo 3, están acotados superiormente pero no tienen máximo. Para ellos existe un concepto que sustituye al máximo. Este se llama **extremo superior** del conjunto y se define como:

*Un número $B$ se denomina extremo superior ($sup \ S=B$) de un conjunto no vacío $S$ si $B$ tiene las dos propiedades siguientes*

a) $B$ es una cota superior de $S$

b) Ningún número menor que $B$ es cota superior para $S$

Si $S$ tiene máximo, éste es también extremo superior de $S$. Pero si $S$ no posee máximo puede tener extremo superior. En el ejemplo 3, el número $1$ es extremo superior para $T$ si bien $T$ no tiene máximo.

![](file:///home/rigoberto/.var/app/com.github.marktext.marktext/config/marktext/images/2020-09-26-18-48-15-image.png)

***Teorema: Dos números distintos no pueden ser extremos superiores para el mismo conjunto.***

*Demostración*: 

Sean $B$ y $C$ dos elementos extremos superiores para un conjunto $S$ La propiedad b) implica que $C \ge B$ puesto que $B$ es extremo superior, análogamente , $B \ge C$ ya que $C$ es extremo superior por lo tanto $B=C$.

Este teorema nos expresa que si existe un extremo superior para un conjunto $S$ hay solamente uno y puede decirse el extremo superior.

**Axioma del supremo superior (axioma de completud)**

Podemos ahora establecer el axioma del supremo para número reales.

***Axioma: Todo conjunto no vacío $S$ de números reales acotado superiormente posee extremo superior, esto es, existe un número real $B$ tal que $B = sup \ S$***

El extremo superior de $S$ no pertenece necesariamente a $S$ en realidad $sup \ S$ pertenece a $S$ si y solo sí $S$ posee máximo, en cuyo caso $max \ S = sup \ S$.



## Inferior de un conjunto, elemento mínimo, extremo inferior

Las definiciones de cota inferior, acotado inferiormente, mínimo se formulan en forma parecida.  

Sea $S$ un conjunto no vacío de números reales y supongamos que existe un número $L$ tal que: $x \ge L$ para todo $x$ de $S$. Entonces decimos que $S$ está **acotado inferiormente** por $B$.

$$
S \in \R, \exists L \mid \forall x\{ x \in S , x \ge L \}
$$

El número $L$ se denomina una **cota inferior para $S$**. Decimos una cota inferior debido a que todo número menor que $L$ también es una cota inferior.

Si una cota inferior $L$ pertenece a $S$, entonces $L$ se le llama el elemento **mínimo de $S$**, si existe se escribe $L = min \ S$.

Así que $L = min \ S$ si $L \in S$ y $x \ge L$ para todo $x$ de $S$. Un conjunto sin cota inferior se dice que es no acotado inferiormente.

Ejemplos:

1. Sea $S$ el conjunto de todos los números reales $x$ tales que $0\le x \le 1$ . Este conjunto está acotado inferiormente por el $0$. Su elemento mínimo es $0$.
2. Sea $S$ el conjunto de todos los números reales positivos. Es un conjunto está acotado inferiormente. Su elemento mínimo es 1.
3. Sea $T$ el conjunto de todos los números reales $x$ tales que $0 < x < 1$. Este conjunto está acotado inferiormente por el $0$ pero no tiene elemento mínimo.

Algunos conjuntos, parecidos al ejemplo 3, están acotados inferiormente pero no tienen mínimo. Para ellos existe un concepto que sustituye al mínimo. Este se llama **extremo inferior** del conjunto y se define como:

Un número $L$ se llama extremo inferior(ínfimo) de $S$ si 

a) $L$ es una cota inferior para $S$ 

b) ningún número mayor que $L$ es cota inferior  para $S$ 

El extremo inferior de $S$, cuando existe , es único y se designa por $inf \ S$. Si $S$ posee mínimo, entonces $min \ S = inf \ S$.

Con el axioma del supremo se puede demostrar el siguiente teorema

***Teorema: Todo conjunto no vacío $S$ acotado inferiormente posee extremo inferior, esto es, existe un número real $L$ tal que $L = inf \ S$***  

*Demostración:*

Sea $-S$ el conjunto de los números opuestos de los de $S$. Entonce $-S$ es no vacío y acotado superiormente. El axioma nos dice que existe un número $B$ que es extremo superior de $-S$. Es fácil ver que $-B = inf \ S$.

**Ejemplo** Sea $S$ el conjunto de todos los números de la forma $(1+1/n)^n$, donde $n = 1,2,3,4,...$ Si, por ejemplo, hacemos $n=1,2$ y $3$, encontramos que los números $2, 9/4, 64/27$ pertenecen a $S$. Todo número del conjunto es mayor que $1$, con lo que el conjunto está acotado inferiormente y por lo tanto tiene un extremo inferior. El menor número de $S$ es $2$ $inf \ S = min S = 2$. También el conjunto está acotado superiormente, aunque no es tan fácil demostrar*. Una ves sabido que $S$  está acotado superiormente,el axioma del supremo nos asegura la existencia del extremo superior de $S$. En este caso no resulta fácil determinar el valor del extremo superior de $S$ a partir de la definición de este conjunto.   



## La propiedad Arquimediana del sistema de los número reales

Se va a mostrar algunas propiedades importantes del sistema de los número reales que son consecuencia del axioma del extremo superior.

***Teorema 1: El conjunto $P$ de los enteros positivos $1,2,3,...$ no está acotado superiormente.***

*Demostración:*

Supongamos que $P$ está acotado superiormente. Demostraremos que esto nos conduce a una contradicción. Puesto que $P$ no es vacío por el axioma del supremo nos dice que $P$ tiene extremo superior, sea éste $b$. El número $b-1$, siendo menor que $b$, no puede ser cota superior de $P$. Luego existe un mínimo entero positivo $n$ tal que $n>b-1$. Para este $n$ tenemos $n+1>b$. Puesto que $n+1$ pertenece a $P$, esto contradice el que $b$ sea una cota superior para $P$.

Como corolarios del teorema anterior se tiene:

***Teorema 2: Para cada real $x$ existe un entero positivo $n$ tal que $n>x$***.

*Demostración:* 

Si no fuera así, $x$ sería una cota superior de $P$, en contradicción con el teorema 1

 ***Teorema 3: Si $x>0$ e $y$ es un número real arbitrario, existe un entero positivo $n$ tal que $nx>y$***.

*Demostración:*

Aplicando el teorema 2 cambiando $x$ por $y/x$.

La propiedad descrita en teorema anterior, se denomina como propiedad arquimediana del sistema de los números reales. Geométricamente significa que cada segmente, tan largo como se quiera, puede ser recubierto por un número finito de segmentos de longitud positiva dada, tan pequeña como se quiera. 

A partir de la propiedad arquimediana, podemos demostrar el teorema siguiente.

***Teorema 4: Si tres números reales $a, x, y$ satisfacen las desigualdades $a\le x\le a+y/n$ para todo entero $n \ge 1$, entonces $x = a$.***

*Demostración:*



## Propiedades fundamentales del extremo superior

La primera de ella establece que todo conjunto de números con extremo superior contiene números tan próximos como se quiera a dicho extremo. Un conjunto con extremo inferior contiene números tan próximos a él como se quiera.

***Teorema 1: Sea $h$ un número positivo dado y $S$ un conjunto de números reales***.

*a) Si $S$ tiene extremo superior, para un cierto $x$ de $S$ se tiene $x>sup \ S-h$.*

*Demostración:*

Si es $x \le sup \ S-h$ para todo $x$ de $S$, entonces $sup \ S -h$ sería una cota superior de $S$ menor que su extremo superior. Por consiguiente debe de ser $x>sup \ S-h$ por lo menos para un $x$ de $S$. 

*b) Si $S$ tiene extremo inferior, para un cierto $x$ de $S$ se tiene $x<inf \ S+h$.*

*Demostración:*

Si es $x \ge inf \ S+h$ para todo $x$ de $S$, entonces $inf \ S +h$ sería una cota inferior de $S$ mayor que su extremo inferior. Por consiguiente debe de ser $x<inf \ S+h$ por lo menos para un $x$ de $S$. 

***Teorema 2:  Propiedad aditiva. Dados dos subconjuntos no vacíos $A$ y $B$, sea $C$ el conjunto.***
$$
C = \{ a+b \ | \ a \in A, b\in B \}
$$
*a) Si $A$ y $B$ poseen extremo superior, entonces $C$ tiene extremo superior, y $sup \ C = sup \ A + sup \ B$*

*Demostración*:

Supongamos que $A$ y $B$ tenga superior. Si $c \in C$, entonces $c= a+b$, donde $a \in A$ y $b \in B$. Por consiguiente $c \le sup \ A + sup \ B$; de modo que $sup \ A + sup \ B $ es una cota superior de $C$. esto demuestra que $C$  tiene extremo superior y que $sup \ C \le sup \ A + sup \ B $.

Sea ahora $n$ un entero positivo cualquiera. Según el teorema 1 con $h = 1/n$ existe un $a$ en $A$ y un $b$ en $B$ tales que $a>sup \ A - 1/n$, y $b>sup \ B -1/n$.

Sumando estas desigualdades, se obtiene $a+b>sup \ A + sup \ B - 2/n$ o $sup \ A+ sup \ B < a+b+2/n \le sup \ C+ 2/n$ puesto que $a+b\le sup \ C$. Por consiguiente hemos demostrado que
$$
sup \ C \le sup \ A + sup \ B < sup \ C + 2/n
$$
 para todo entero $n\ge 1$. En virtud del teorema 4(P. Arquimediana), debe de ser $sup \ C = sup \ A + sup \ B$.



*b) Si $A$ y $B$ poseen extremo inferior, entonces $C$ tiene extremo inferior, y $inf \ C = inf \ A + inf \ B$*

 *Demostración*

***Teorema 3: Dados dos subconjuntos no vacíos $S, T \in \R $ tales que $s \le t$ para todo $s$ de $S$ y todo $t$ de $T$. Entonces $S$ tiene superior, y $T$ extremo inferior, y se verifica $sup \ S \le inf \ T$***.

*Demostración:* 

Cada $t$ de $T$ es cota superior para $S$. Por consiguiente $S$ tiene extremo superior que satisface la desigualdad $sup S \ \le t$ para todo $t$ de $T$. Luego $sup \ S$ es una cota inferior para $T$, con lo cual $T$ tiene extremo inferior que no puede ser menor que $sup S$. Dicho de otro modo, se tiene que $sup \ S \le inf \ T$, como se afirmó.





