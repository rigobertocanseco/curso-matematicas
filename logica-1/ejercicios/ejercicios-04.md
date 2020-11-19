**Ejercicios**

Rigoberto Canseco López

***

Podemos definir la idea de construcción como: Sea una sucesión de construcción finita $\lang \epsilon_1, \epsilon_2, ..., \epsilon_{n-1}, \epsilon_n \rang$ de expresiones tal que, para cada $i < n$ , tenemos al menos uno de los siguientes hechos:

* $\epsilon_i$ es un símbolo de enunciado.
* $\epsilon_i=\epsilon_\square(\epsilon_i,\epsilon_j)$ para algún $j <n, i<n$ , y $\square$ un símbolo de conectivo binarios $(\or, \and, \to, \leftrightarrow)$   

Sea $S$ un conjunto de fórmulas que contiene todos los símbolos de enunciado y es cerrado bajo las operaciones de construcción, entonces $S$ es el conjunto de todas las fórmulas.

1. **Sea $\alpha$ la fórmula, sea $c$ el número posible de lugares en los que aparecen símbolos de conectivo binarios $(\or, \and, \to, \leftrightarrow)$ en $\alpha$; sea $s$ el número de lugares en los que aparece símbolos de enunciado en $\alpha$. (Por ejemplo, si $\alpha$ es $(A\to(\neg A))$, entonces $c=1$ y $s=2)$. Usando el principio de inducción, pruebe que $s=c+1$.**

   *Demostración por inducción*

   * **Caso base:** Sea $\alpha$ una fórmula bien formada con un símbolo de enunciado y ningún conector binario, es decir $\alpha=A_1$
     Por lo tanto se cumple que $s=c+1$ ya que el numero de símbolos conectivos es $c = 0$ y el número de símbolos de enunciado es $s=1$.
     $$
     s_1=c_0+1
     $$

   * **Hipótesis de inducción:** Entonces $s=c+1$ es cierta para cualquier paso $\epsilon_n$ de construcción y $\epsilon_n \in S$.

   * **Paso inductivo:** Se demuestra que, $s=c+1$ es cierta para el paso $n$ de construcción, entonces para el paso $\epsilon_{n+1}$ lo es también.

     Al agregar un símbolo de conector binario $\square$ a la formula $\alpha$ es evidente que debemos agregar un símbolo de enunciado , es decir.
     $$
     \begin{split}
     \text{Para } \epsilon_1\\
     \alpha&=A_1 \quad \\
      \text{Para } \epsilon_n\\
     \alpha &= (A_1 \square_1\  \_ \_  )\quad \text{Agregamos un símbolo conectivo binario} \\
     \alpha &= (A_1 \square_1 A_2) \\
      \text{Para } \epsilon_{n+1}\\
     \alpha&= (\alpha_{n} \square_{n} A_{n+1})
     \end{split}
     $$
     Por lo tanto
     $$
     s_{n}=c_{n} +1 \\
     \text{Agregando un símbolo conectivo al paso } n\\
     s_{n+1} =s_n+1=c_{n} +1 +1 \\
     s_{n+1} = (c_{n} +1) +1
     $$
     Como $\epsilon_n \in S$ también lo es $\epsilon_{n+1}$, queda demostrado $s=c+1 \quad \blacksquare$   

2. **Suponga que $\alpha$ es una fórmula que no contiene el símbolo de negación $\neg$**

   * **Muestre que la longitud de $a$ (es decir, el número de símbolos en la sucesión) es impar.** 

     Longitud de $\alpha = 4k+1$

     *Demostración por inducción*

     * **Caso base:** Sea $\alpha$ una fórmula bien formada con un símbolo de enunciado y ningún conector binario, es decir $\alpha=A_1$
       $$
       \begin{split}
       \text{Para }k=0 \\ 
       \text {Longitud de }\alpha &= 4k+1 =4(0)+1=1\\
       \text {Longitud de }\alpha &= 1
       \end{split}
       $$
       Por lo tanto se cumple que la longitud de $\alpha$ es impar. 

     * **Hipótesis de inducción:** Entonces la longitud de $\alpha=4k+1$ es cierta para cualquier paso $\epsilon_n$ de construcción y $\epsilon_n \in S$. Donde $k$ es el numero de símbolos conectivos y $k\le n $. 

     * **Paso inductivo:** Se demuestra que, la longitud de $\alpha=4k+1$ es cierta para el paso $n$ de construcción, entonces para el paso $\epsilon_{n+1}$ lo es también.

       Al agregar un símbolo de conector binario $\square$ a la formula $\alpha$ es evidente que debemos agregar un símbolo de enunciado y en consecuencia se agregan 4 símbolos más es decir, $\{(,),\square,A\}$, 
       $$
       \begin{split}
        \text{Para }\epsilon_{1}\\
       \alpha &=A_1 \quad \\
        \text{Para }\epsilon_{n}\\
       \alpha &= (A_1 \square_1\  \_ \_  )\quad\text{Agregamos un símbolo conectivo binario} \\
       \alpha &= (A_1 \square_1 A_2) \quad \text{Tenemos } 5 \text{ símbolos y que es un número impar} \\
        \text{Para } \epsilon_{n+1}\\
       \alpha&= (\alpha_{n} \square_{n} A_{n+1})
       \end{split}
       $$
       Por lo tanto
       $$
       \begin{split}
       \text{Longitud de }\alpha \text{ para }n \\
       &=\sum_{k=0}^n4k+1 \quad \text{Es impar}\\
       \text{Para } n+1 \text{ tenemos que} \\
       4+\big(\sum_{k=0}^n4k+1\big)&=(4k+1)+4 \\
       &=4(k+1)+1 \quad \text{Es impar}
       \end{split}
       $$
       Como $\epsilon_n \in S$ también lo es $\epsilon_{n+1}$, queda demostrado la longitud de $\alpha$ es un número impar$\quad \blacksquare$   

   * **Muestre que más de una cuarta parte de los símbolos son símbolos de enunciado.**

     Número de símbolos de enunciado es $k+1$

     *Demostración por inducción*

     * **Caso base:** Sea $\alpha$ una fórmula bien formada  $\alpha=(A_1\square A_2)$ con un total de 5 símbolos $\{(,A_1,\square, A_2,)\}$
       Donde $2/5$ son símbolos de enunciados y por lo tanto cumple que, $1/5>1/4$ parte de los símbolos.

     * **Hipótesis de inducción:** Entonces más de una cuarta parte de los símbolos son símbolos de enunciado. 
       Donde el número de símbolos de enunciado es $k+1$ es cierta para cualquier paso $\epsilon_n$ de construcción y $\epsilon_n \in S$. Donde $k$ es el numero de símbolos conectivos y $k\le n $. 

     * **Paso inductivo:** Se demuestra que, la longitud de $\alpha=k+1$ es cierta para el paso $n$ de construcción, entonces para el paso $\epsilon_{n+1}$ lo es también.

       Al agregar un símbolo de conector binario $\square$ a la formula $\alpha$ es evidente que debemos agregar un símbolo de enunciado y en consecuencia se agregan 4 símbolos más es decir, $\{(,),\square,A\}$, 
       $$
       \begin{split}
       
        \text{Para }\epsilon_{1}\\
       
       \alpha &= (A_1 \square_1 A_{n+1})
       \\&\text{Tenemos } 2/5 \text{ son símbolos de enunciado} \\
        \text{Para }\epsilon_{n}\\
       \alpha &= ((A_1 \square_1\  A_{n}) \square_{n} A_{n+1}) 
       \\&\text{Tenemos } 3/9 \text{ son símbolos de enunciado} \\
        \text{Para } \epsilon_{n+1}\\
       \alpha&= (((A_1 \square_1\  A_2) \square_2 A_3) \square_{n+1} A_{n+1})
       \\&\text{Tenemos } 4/13 \text{ son símbolos de enunciado} 
       \end{split}
       $$
       Por lo tanto la longitud de símbolos de enunciado es $\sum_{k=0}^nk+1$ del total de símbolos de $\alpha (\sum_{k=0}^n4k+1)$ donde $k$ es el número de símbolos conectivos. 

       Es decir, longitud de símbolos de enunciado es:
       $$
       \begin{split}
       \text{Para } n \text{ tenemos que} \\
        =\sum_{k=0}^n{\frac{k+1}{4k+1}} \\
       
       \text{Para } n+1 \text{ tenemos que} \\
        ={\frac{\sum_{k=0}^n(k+1)+1}{\sum_{k=0}^n(4k+1)+4}}&=\frac{k+1+1}{(4k+1)+4} \\
       &=\frac{(k+1)+1}{4(k+1)+1} > \frac 1 4 
       \end{split}
       $$
       Como $\epsilon_n \in S$ también lo es $\epsilon_{n+1}$, queda demostrado la longitud de símbolos es más de una cuarta parte de símbolos  de $\alpha \quad \blacksquare$.

     

