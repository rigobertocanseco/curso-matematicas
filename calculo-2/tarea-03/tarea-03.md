# Tarea 3

**Rigoberto Canseco López**

## 1. Sean $P$ y $Q$ dos particiones del intervalo $[a,b]$ y $f$ una función acotada en $[a,b]$. Si $Q \supset P$ entonces $U(f,Q)\le U(f,P)$

Si $Q$ y $P$ son dos particiones tales que $Q \supset P$, entonces $L(f,P) \le L(f,Q) \le U(f,Q) \le U(f,P)$. Como $Q \supset P$  por lo tanto $Q$ contiene un elemento más que $P$.

Supongamos que 
$$
P=\{t_0,t_1,..., t_n\} \quad Q=\{t_0,t_1,...,t_{k-1}, u, t_{k}, ..., t_n\}
$$


Tenemos que

$$
M' = sup\ \{f(x) \ | \  x \in [t_{k-1}, u] \} \\
M'' = sup\ \{f(x) \ | \ x \in [u, t_k] \}
$$

Sabemos que
$$
\ \\
U(f,P) = \sum_{i=1}^{n}M_i(t_i-t_{i-1}) \\
L(f,Q) = \sum_{i=1}^{k-1}M_i(t_i-t_{i-1}) + M'(u-t_{k
-1})+M''(t_k-u)+  \sum_{i=k+1}^{n}M_i(t_i-t_{i-1})
$$
Por demostrar que
$$
U(f,Q) \le U(f,P)
$$
Basta demostrar que 
$$
M'(u-t_{k-1}) + M''(t_k-u) \le M_k(t_k-t_{k-1}) 
$$
Recordemos que si $A \subset B$ y ambos conjuntos están acotados inferiormente, entonces 
$$
sup \ A \ge x \text{ Para todo } x\in A
$$
en particular
$$
sup \ A \ge b \text{ para todo } b \in B \supset A
$$
de donde 
$$
sup \ A \ge sup \ B
$$
Como $[t_{k-1}, u] \subset [t_{k-1}, t_k]$, entonces
$$
M_k \ge M'
$$
Análogamente como $[u, t_k] \subset [t_{k-1}, t_k]$, entonces
$$
M_k\ge M''
$$
Así
$$
\begin{split}
M_k(t_k-t_{k-1}) &= M_k(t_k-u+u-t_{k-1}) \\
&= M_k(t_k-u)+M_k(u-t_{k-1}) \\
&= M_k(t_k-u)+M_k(u-t_{k-1}) \\
&\ge M'(t_k-u) + M''(u-t_{k-1})
\end{split}
$$
Por tanto 
$$
U(f,P) \ge U(f,Q) \quad \blacksquare
$$

***

## 2. Calcular las siguientes integrales

### a. $\int_0^5[x] \ dx$

### b. $\int_{-1}^2[3x]-[x] \ dx$

### c. $\int_{-1}^{1}|2x+1| \ dx$

Lo primero que hay que hacer es identificar el punto donde el argumento vale cero, debido a que la función valor absoluto depende de si su argumento es positivo o negativo.
$$
2x+1 = 0 \\
x = -1/2
$$
La solución encontrada es $x=-1/2$, quiere decir que en $x<-1/2$, el argumento de la función es negativo y en $x ≥ −1/2$ positivo; por lo que separando la integral en ambos intervalos:
$$
\int_{-1}^{1}|2x+1| \ dx = \int_{-1}^{-1/2}|2x+1| \ dx + \int_{-1/2}^{1}|2x+1| \ dx
$$
Sustituyendo el valor absoluto:
$$
|2x+1|= -(2x+1) = -2x-1 \quad\text{si } x < -1/2 \\
|2x+1|= 2x+1 = \quad\text{si } x \ge -1/2
$$
Tenemos que la integral es 
$$
= \int_{-1}^{-1/2}-2x-1 \ dx + \int_{-1/2}^{1}2x+1 \ dx
$$
Separando las integrales de acuerdo a las notas del **(pdf 1, pag-17-18)**
$$
\begin{split}
&= \int_{-1}^{-1/2}-2x\ dx+\int_{-1}^{-1/2}-1 \ dx + \int_{-1/2}^{1}2x \ dx+ \int_{-1/2}^{1}1 \ dx \\
&= -2\int_{-1}^{-1/2}x\ dx-1\int_{-1}^{-1/2} \ dx + 2\int_{-1/2}^{1}x \ dx+ 1\int_{-1/2}^{1} \ dx \\
&= -2(x^2/2)-x + 2(x^2/2) + x
\end{split}
$$
Realizando las integrales, de acuerdo a las notas del **(pdf 1, pag-17-18)**
$$
\begin{split}
&= -2((-1/2)^2/2- (-1)^2/2) - (-1/2-1) \\
&+2((1)^2/2- (-1/2)^2/2) - (1-1/2) \\
&= 1/4 + 9/4 = 10/4 = 5/2 \\
&= \frac{5}{2}
\end{split}
$$
Por lo tanto $\int_{-1}^{1}|2x+1| \ dx = \frac{5}{2} \quad \blacksquare$

## 3. Encontrar en cada caso $F'(x)$

### a. $F(x)=\int_0^{x^2} \frac{sen \ 2t}{1+t^2} \ dt$

Para resolver esta derivada, es útil tratarla como una composición de funciones, tenemos que:
$$
f(x) = \int^{x}_{0}{\frac{sen \ 2t}{1+t^2}dt} \quad \text{ y } \quad g(x)=x^2
$$
Por lo que, por regla de la cadena tenemos que $F(x)= f(g(x))$ por lo tanto, usando el TFC y las reglas de derivación:
$$
f'(x) = \frac{sen \ 2x}{1+x^2} \quad \text{ y } \quad g'(x)=2x
$$
Sustituyendo los valores de $g, f', g'$. Tenemos:
$$
\begin{split}
F'(x) &= f'(g(x))g'(x) \\
&= f'(x^2)(2x) \\
&= 2x\frac{sen \ 2x^2}{1+x^4} \quad \blacksquare
\end{split}
$$
Por lo que $F'(x)= 2x\frac{sen \ 2x^2}{1+x^4}$

***

### b. $\int_z^{x^2}\frac{2}{(1+t^2)^2} \ dt$ para $x > 1$

Para resolver esta derivada, es útil tratarla como una composición de funciones, tenemos que:
$$
f(x) = \int_z^{x}{\frac{2}{(1+t^2)^2}} dt \quad \text y \quad g(x^2)
$$
Por lo que, por regla de la cadena tenemos que $F(x)= f(g(x))$ por lo tanto, usando el TFC y las reglas de derivación:
$$
f'(x)=\frac{2}{(1+t^2)^2} \quad \text y \quad g'(x)=2x
$$
Sustituyendo los valores de $g, f', g'$. Tenemos:
$$
\begin{split}
F'(x)&= f'(g(x))(g'(x))\\
&=f'(x^2)2x \\
&= \frac{4x}{(1-x^4)^2} \quad \blacksquare
\end{split}
$$
Por lo que $F'(x) = \frac{4x}{(1-x^4)^2} $

***

## 4. Sea $\int_0^x f(t)\ dt = \sqrt{1+x^2} -1 $ Calcular $f(1)$

Para obtener la forma explícita de $f(x)$ hay que derivar utilizando el TFC.

Derivando ambas partes de la ecuación y  aplicando el TFC del lado izquierdo:
$$
\frac{d}{dx}(\int_0^x f(t)\ dt ) = \frac{d}{dx}(\sqrt{1+x^2} -1) \\
\text{Usando las reglas de derivación tenemos que:}\\
f(x) = \frac{x}{\sqrt{1+x^2}}
$$
Evaluamos la ecuación en el punto $f(1)$
$$
\begin{split}
f(1) &= \frac{x}{\sqrt{1+x^2}} \\
&= \frac{1}{\sqrt{1+1^2}} \\
&= \frac{1}{\sqrt{2}} \quad \blacksquare
\end{split}
$$
Por lo tanto tenemos que $f(1)= \frac{1}{\sqrt 2}$

***

## 5. Una función $f$ es continua para cualquier $x$ y satisface la ecuación $\int_0^xf(t) \ dt = -\frac{1}{2} + x^2 + xsen \ 2x + \frac{cos \ 2x}{2}$ para todo $x$. Calcular $f(\frac{\pi}{4})$ y $f'(\frac{\pi}{4})$

Para obtener la forma explícita de $f(x)$ hay que derivar utilizando el TFC.

Derivando ambas partes de la ecuación y  aplicando el TFC del lado izquierdo:
$$
\frac{d}{dx}(\int_0^x f(t)\ dt ) = \frac{d}{dx}(-\frac{1}{2} + x^2 + xsen \ 2x + \frac{cos \ 2x}{2}) \\
\text{Usando las reglas de derivación tenemos que:}\\
f(x) = 2x(cos \ 2x +1)
$$
Evaluamos la ecuación en el punto $f(\pi/4)$
$$
\begin{split}
f(\pi/4) &= 2x(cos \ 2x +1) \\
&= 2(\pi/4)(cos \ 2(\pi/4) +1) \\
&= (\pi/2)(cos \ (\pi/2) +1)  \\
&= \pi/2(0+1)\\
&= \frac{\pi}{2}
\end{split}
$$
Por lo tanto $f(\pi/4) = \frac{\pi}{2} \quad \blacksquare$

Para calcular $f'(\pi/4)$ primero obtenemos $f'(x)$
$$
f(x)= 2x(cos(2x) +1)\\
\text{Usando las reglas de derivación tenemos que:}\\
f'(x) = 2(-2x sen \ (2x) + cos \ (2x) +1)
$$
Evaluamos la ecuación en el punto $f'(\pi/4)$
$$
\begin{split}
f'(\pi/4) &=  2(-2x sen \ (2x) + cos \ (2x) +1) \\
&= 2(-2(\pi/4)sen(2(\pi/4))+cos(2(\pi/4))+1) \\
&= 2((-\pi/2)sen(\pi/2)+cos(\pi/2)+1) \\
&= 2((-\pi/2)1+0+1) \\
&= 2(-\pi/2)1+2 \\
&= -\pi+2 \\
&=2-\pi
\end{split}
$$
Por lo tanto $f'(\pi/4)=2-\pi \quad \blacksquare$

***