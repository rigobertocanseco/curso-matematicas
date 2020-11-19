 **Examen 2**
**Rigoberto Canseco López**

1. **Dé un ejemplo de una familia $F_1$ de funciones compatibles y un ejemplo de una familia $F_2$ de funciones no compatibles. Para el primer ejemplo, mencione quién es la función unión de la familia $F_1$.**
   A un conjunto de funciones $F$ es llamado compatible si cualquier dos funciones $f, g$ de $F$ son compatibles. A su vez las funciones $f(x)=g(x)$ para todo $x\in dom \ f \cap dom \ g$   

   1. ejemplo

   $$
   f=\{\sqrt x  |x\in \N\},g=\{\sqrt x |x\in \R\} \\
   dom(\bigcup F) = \bigcup \{dom \ f |f \in F\} \\
   f=\{\sqrt x  |x\in \N\}
   $$

   2. ejemplo
      $$
      f=\{\sqrt x  |x\in \N\},g=\{ x |x \in \R\}
      $$
      

2. **Sea $f: X \to Y$ función con $X\neq \emptyset$. Muestre que $f$ es una función sobreyectiva si y sólo si para todo $B\subseteq Y, B= f(f^{-1}(B))$**
   Tenemos que $B \subseteq Y$  
   $$
   \begin{split}
   f(f^{-1}(B)) &= \{y \in Y: \exist x\in f^{-1}(B)[f(x)= y]  \}\\
   &= \{y \in Y: \exist x\in \{z\in X:f(z) \in B\}[f(x)= y] \}\\
   &= \{y \in Y: \exist x\in X[f(x)= y \and f(x) \in B] \}\\
   &= B \quad \blacksquare
   \end{split}
   $$
     

3.  **Sean $f$ y $g$ funciones. Muestre  que si $ran \ f \subseteq dom \ g$ entonces $dom \  g \circ f =  dom \ f$**
   Sabemos que $dom \ g \circ f = dom \ f \cap f^{-1}(dom \ g)\subseteq dom \ f$. Por la otra dirección de la inclusión tenemos que, 
   $$
   dom \ g \circ f = dom \ f \cap f^{-1}(dom \ g) \supseteq dom \ f \cap f^{-1}(dom \ f) = dom \ f
   $$
    donde usamos el hecho de que $f^{-1}(ran \ f) = dom \ f$
   $$
   \begin{split}
   x \in f ^{-1}(ran \ f) &\iff \exist y \in ran \ f \text{ tal que } (y,x) \in f^{-1} \\
   &\iff \exist y \in  ran \ f \text{ tal que } (x,y) \in f \\
   &\iff x \in dom \ f \quad \blacksquare
   \end{split}
   $$
   

4. **Muestre que si $f: X\to Y$ es una función inyectiva, con $X\ne \emptyset$ y $\{A_\alpha:\alpha\in I\}$ es una familia de subconjuntos de $X$, entonces: **
   $$
   f\left( \bigcap_{\alpha\in I} A_\alpha\right)= \bigcap_{\alpha\in I}f(A_\alpha)
   $$
   Sea $f$ una función. Entonces
   $$
   \begin{split}
   y\in f\left( \bigcap_{\alpha\in I} A_\alpha\right) &\iff \exist  x \in  \bigcap_{\alpha\in I}A_\alpha \text{ tal que }(x,y)\in f \\
   
   &\iff \forall i \in I, x \in A_\alpha \text{ tal que } (x,y) \in f \\
   &\iff \forall i \in I, y \in f(A_\alpha) \\
   &\iff y \in \bigcap_{\alpha\in I}f(A_\alpha)  \quad \blacksquare
   
   \end{split}
   $$
   





