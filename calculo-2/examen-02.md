# Examen 2

**Rigoberto Canseco López**

## 1.

Existe una función $f$ definida y continua  para todo real $x$ que satisface
$$
\int_{1}^{x}{tf(t)}dt =\int^{x}_0{f(t)}cos^3t \ dt + \tan^2 x- \cos^2 x+ \sin x +3
$$
Encontrar la fórmula explícita para $f(x)$

Para obtener la forma explícita de $f(x)$ hay que derivar utilizando el TFC.

Derivando ambas partes de la ecuación y  aplicando el TFC nos queda que
$$
\frac{d}{dx}(\int_1^x f(t)\ dt ) = \frac{d}{dx}(\int^{x}_0{f(t)}cos^3t \ dt + \int^{x}_0\tan^2 x \ dt- \int^{x}_0\cos^2 x\ dt+ \int^{x}_0\sin x \ dt+\int^{x}_03\ dt) \\
xf(x) = f(x)(cos^3t) + \tan^2 x- \cos^2 x+ \sin x +3 \\
$$
Por lo tanto despejando $f(x)$ tenemos que:
$$
f(x)(x-\cos^3x) = \tan^2 x- \cos^2 x+ \sin x +3 \\
f(x) = \frac{\tan^2 x- \cos^2 x+ \sin x +3} {(x-\cos^3x)}\quad  \blacksquare
$$


## 2

Encontrar $F'(x)$ si $F(x)=\int_{\sec x}^{x^5}\frac{t^4}{5+t^8}dt$

Podemos escribir la integral como:
$$
F(x) = \int^{c}_{\sec x}{\frac{t^4}{5+t^8}dt}+  \int^{x^5}_{c}{\frac{t^4}{5+t^8}dt}
$$
Resolvemos la primer integral
$$
\int^{c}_{\sec x}{\frac{t^4}{5+t^8}dt}
$$


Para resolver esta derivada, es útil tratarla como una composición de funciones, tenemos que:
$$
f(x) = \int^{c}_{x}{\frac{t^4}{5+t^8}dt} \quad \text{ y } \quad g(x)=\sec x
$$
Por lo que, por regla de la cadena tenemos que $F(x)= f(g(x))$ por lo tanto, usando el TFC y las reglas de derivación:
$$
f'(x) = \frac{t^4}{5+t^8} \quad \text{ y } \quad g'(x)=\tan(x)\sec(x)
$$
Sustituyendo los valores de $g, f', g'$. Tenemos:
$$
\begin{split}
F'(x) &= f'(g(x))g'(x) \\
&= f'(\sec x)(\tan x \sec x) \\
&= (\tan x \sec x)\frac{\sec^4 x}{5+\sec^8x}
\end{split}
$$
Resolvemos la segunda integral
$$
\int^{x^5}_{c}{\frac{t^4}{5+t^8}dt}
$$


Para resolver esta derivada, es útil tratarla como una composición de funciones, tenemos que:
$$
f(x) = \int^{c}_{x}{\frac{t^4}{5+t^8}dt} \quad \text{ y } \quad g(x)=x^5
$$
Por lo que, por regla de la cadena tenemos que $F(x)= f(g(x))$ por lo tanto, usando el TFC y las reglas de derivación:
$$
f'(x) = \frac{t^4}{5+t^8} \quad \text{ y } \quad g'(x)=5x^4
$$
Sustituyendo los valores de $g, f', g'$. Tenemos:
$$
\begin{split}
F'(x) &= f'(g(x))g'(x) \\
&= f'(x^5)(5x^4) \\
&= (5x^4)\frac{x^{20}}{5+x^{40}}
\end{split}
$$
Por lo tanto tenemos que
$$
= (5x^4)\frac{x^{20}}{5+x^{40}} -((\tan x \sec x)\frac{\sec^4 x}{5+\sec^8x}
)\\
=\frac{5x^{24}}{5+x^{40}} - \frac{\sec^5 x\tan x}{5+\sec^8x} \quad \blacksquare
$$


## 3.

Calcula $\int_{-6}^{4}|4x+2|dx$

Lo primero que hay que hacer es identificar el punto donde el argumento vale cero, debido a que la función valor absoluto depende de si su argumento es positivo o negativo.
$$
\begin{split}
4x+2&=0\\
x&=-2/4\\
x&=-1/2\\

\end{split}
$$
La solución encontrada es $x=-1/2$, quiere decir que en $x<-1/2$, el argumento de la función es negativo y en $x ≥ −1/2$ positivo; por lo que separando la integral en ambos intervalos:
$$
\int_{-6}^{4}|4x+2| \ dx = \int_{-6}^{-1/2}|4x+2| \ dx + \int_{-1/2}^{4}|4x+2| \ dx
$$
Sustituyendo el valor absoluto:
$$
|4x+2|= -(4x+2) = -4x-2 \quad\text{si } x < -1/2 \\
|4x+1|= 4x+1 = \quad\text{si } x \ge -1/2
$$
Tenemos que la integral es 
$$
= \int_{-6}^{-1/2}-4x-2 \ dx + \int_{-1/2}^{4}4x+2 \ dx
$$
Separando las integrales de acuerdo a las notas del **(pdf 1, pag-17-18)**
$$
\begin{split}
&= \int_{-6}^{-1/2}-4x\ dx+\int_{-6}^{-1/2}-2 \ dx + \int_{-1/2}^{4}4x \ dx+ \int_{-1/2}^{4}2 \ dx \\
&= -4\int_{-6}^{-1/2}x\ dx-2\int_{-6}^{-1/2} \ dx + 4\int_{-1/2}^{4}x \ dx+ 2\int_{-1/2}^{4} \ dx \\
&= -4(x^2/2)-2x + 4(x^2/2) + 2x
\end{split}
$$
Realizando las integrales, de acuerdo a las notas del **(pdf 1, pag-17-18)**
$$
\begin{split}
&=-4 \left(\frac{1}{2} \left(-\frac{1}{2}\right)^2-\frac{(-6)^2}{2}\right)-2 \left(-\frac{1}{2}--6\right)+4 \left(\frac{4^2}{2}-\frac{1}{2} \left(-\frac{1}{2}\right)^2\right)+2 \left(4--\frac{1}{2}\right)\\
&=101
\end{split}
$$
Por lo tanto $\int_{-6}^{4}|4x+2| \ dx = 101 \quad \blacksquare$

