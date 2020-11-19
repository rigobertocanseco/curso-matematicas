**Ejercicios**

Rigoberto Canseco López

***

**Ejercicios**

1. **¿Los siguientes conjuntos $c$ son cerrados bajo todas las operaciones en $\mathcal{F}$? Demuestra tu respuesta o escribe un ejemplo**

   * **a)** $U = \N, c = \{n ∈ U | n = 2k, k ∈ U \} \ \text y \ \mathcal{F} = \{f\} \text{ con } f (x) = 2x + 4$

     *Método inductivo*:

     Sea $n \in \N$ y $f(n)=2x+4$ donde $f(n) \in c$.

     * Caso base: Para $0, f(0)=2(0)+4=4$

       Donde $4 \in c$, por lo tanto $f(0)\in c$

     * Hipótesis de inducción: Para $n, f(n)=2n+4=2(n+2)$ 

       Donde $2(n+2)$ es de la forma $2k$, por lo tanto $f(n)\in c$

     * Paso inductivo: Para $n+1, f(n+1)=2(n+1)+4=2n+2+4=2((n+1)+2)$ 

       Donde podemos ver que $2((n+1)+2)$ es de la forma $2k$, por lo tanto $f(n+1)\in c$

     Podemos concluir que $c$ es cerrado bajo $f(x)=2x+4\quad \blacksquare$ 

   * **b)** $U = \R \setminus  \Q, c = U \  \text y \  \mathcal{F} = {f, g} \text{ con } f (x, y) = xy \ \text y \ g(x, y) = x + y$

     *Ejemplo*

     Sea $x,y\in\R\setminus\Q$ por ejemplo $x=y=\sqrt2$ para $f(x,y)=xy$, 
     $$
     f(\sqrt2,\sqrt2)=4, \\4\notin\R\cup\Q \therefore
     $$
     Por lo tanto no se cumple $\quad \blacksquare$

2. **Sean $a, b ⊂ U$ cerrados bajo $f : U^n \to U$ , demuestra que $a ∩ b$ es cerrado bajo $f$.**

   Sea $a\cap b, \exist x$ tal que
   $$
   (x\in a \and x \in b)\sub U \\
   (f_a(x)\and f_b(x))\sub U \\
   f_a (x_ 1 , ..., x_n ) \and f_b (x_ 1 , ..., x_n ) = x \\
   \text{ con } x_1,..., x_n,x \sub U
   $$

3. **¿Si $a, b ⊂ U$ son cerrados bajo $f : U^n \to U$ entonces $a ∪ b$ es cerrado bajo $f$ ? Demuestra tu respuesta o escribe un ejemplo.**

   Sea $a\cup b, \exist x$ tal que
   $$
   (x\in a \or x \in b)\sub U \\
   (f_a(x)\or f_b(x))\sub U \\
   f_a (x_ 1 , ..., x_n ) \or f_b (x_ 1 , ..., x_n ) = x \\
   \text{ con } x_1,..., x_n,x \sub U
   $$

4. 