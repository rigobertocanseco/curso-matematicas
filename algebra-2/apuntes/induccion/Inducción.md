# Ejercicios de inducción matemática


##### 1. Demuestra por inducción sobre $n \ge 0$, que $\sum_{i=1}^{n}{i(i+1)=\frac{n(n+1)(n+2)}{3}}$.

Tenemos que $n \in \N$, vamos a probar para los siguientes casos:

* Cuando $n = 0$
  $$
  \sum_{i=1}^{n}{i(i+1)=0(0+1)= \frac{0(0+1)(0+2)}{3}} = 0
  $$
  Por lo tanto cumple cuando $n = 0$.

* Cuando $n = 1$
  $$
  \sum_{i=1}^{n}{i(i+1)=0 + 1(1+1)= \frac{1(1+1)(1+2)}{3}} = 2
  $$

Hipótesis inductiva: supongamos que el teorema se cumple para todos los valores de $n$ ahora demostremos para $n+1$.
$$
\begin{equation}
\begin{split}
{\sum_{i=1}^{n+1}{i(i+1)}} & = (n+1)((n+1)+1) + {\sum_{i=1}^{n}{i(i+1)}} \\
& = \frac{n(n+1)(n+2)}{3} + (n+1)((n+1)+1)\ \text {, por nuestra hipótesis de inducción.}\\
& = \frac{n(n+1)(n+2)}{3}+ \frac{3(n+1)((n+1)+1)}{3} \\
& = \frac{n(n+1)(n+2)+3(n+1)((n+1)+1)}{3} \\
& = \frac{(n+1)(n(n+2)+3((n+1) +1))}{3} \\
& = \frac{(n+1)(n(n+2)+3(n+2))}{3} \\
& = \frac{(n+1)(n^2+2n+3n+2)}{3} \\
& = \frac{(n+1)(n+2)(n+3))}{3} \\
& = \frac{(n+1)((n+1)+1)((n+1)+2))}{3} \\
\end{split}
\end{equation}
$$
La equivalencia se cumple para $n+1$.

Por el principio de inducción matemática, el teorema es válido para todo $n \in \N$

##### 2. Demuestra por inducción sobre $n\ge 0$, que $\sum_{i=1}^{n}{i^3}= \frac{n^2(n+1)^2}{4}$ .

Tenemos que $n \in \N$, vamos a probar para los siguientes casos:

* Cuando $n = 1$
  $$
  \sum_{i=1}^{n}{i^3}= 1^3=\frac{1^2(1+1)^2}{4} = 1
  $$

* Cuando $n = 2$
  $$
  \sum_{i=1}^{n}{i^3}= 1^3 + 2^3=\frac{2^2(2+1)^2}{4} = 9
  $$

Hipótesis inductiva: supongamos que el teorema se cumple para todos los valores de $n$ ahora demostremos para $n = n+1$.
$$
\begin{equation}
\begin{split}
\sum_{i=1}^{n+1}{i^3} & = (n+1)^3 + \sum_{i=1}^{n}{i^3} \\
& = \frac{n^2(n+1)^2}{4} + (n+1)^3 \ \text {, por nuestra hipótesis de inducción.} \\ 
& = \frac{n^2(n+1)^2 + 4(n+1)^3}{4} \\
& = \frac{(n+1)^2(n^2+4(n+1))}{4} \\
& = \frac{(n+1)^2(n^2+4n+4)}{4} \\
& = \frac{(n+1)^2(n+2)^2}{4} \\
& = \frac{(n+1)^2((n+1)+1)^2}{4}
\end{split}
\end{equation}
$$
La equivalencia se cumple para $n+1$.

Por el principio de inducción matemática, el teorema es válido para todo $n \in \N$

##### 3. Demuestre por inducción sobre $n\ge5$, que $2^n > n^2$.

Tenemos que $n \in \N$, vamos a probar para los siguientes casos:

* Cuando $n = 5$
  $$
  2^5 > n^2 \\
  32 > 25
  $$

* Cuando $n = 6$
  $$
  2^6 > 6^2 \\
  64 > 36
  $$

Hipótesis inductiva: supongamos que el teorema se cumple para todos los valores de $n$ ahora demostremos para $n = n+1$.
$$
2 \cdot 2^{n} > (n+1)^2 \\
2^{(n+1)} > (n+1)^2
$$
Por lo tanto se cumple $\forall n \ge 5 $.