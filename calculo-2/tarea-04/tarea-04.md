# Tarea 4

**Rigoberto Canseco López**

## 1. Sea $f(x)= \frac 1 2 (a^x + a^{-x})$ si $a >0$. Prueba que $f(x+y)+f(x-y) = 2f(x)f(y)$.

## 2. Encuentra la inversa de $f(x)=24(2^{-x/25})$.

Como la función es inyectiva podemos determinar su inversa
$$
y = 24(2^{-x/25}) \quad f(x) \\
$$

$$
 \frac{y}{24} = 2^{-x/25} \\
 \log \frac{y}{24} = \log 2^{-x/25} \\
  \log \frac{y}{24} = \log 2^{-x/25} \\
\log y - \log24 = \frac{-1}{25} x \log2 \\
\frac{\log y - \log24}{\log2} = \frac{-1}{25} x  \\
(-25)(\frac{\log y - \log24}{\log2} )=  x  \quad \blacksquare


 
$$



## 3. Resolver las ecuaciones

### $\ln(x+6)+ \ln (x-3)= \ln \ 5 + \ln \ 2$

$$
\begin{split}
\ln(x+6)+ \ln (x-3) &= \ln \ 5 + \ln \ 2 \\
\ln((x+6) (x-3)) &= \ln \ (5 \cdot 2) \\
\ln((x+6) (x-3)) &= \ln \ (5 \cdot 2) = \ln(10)\\
\text{Se cancela el logaritmo por el exponente en ambos términos}\\
\cancel\ln((x+6) (x-3)) &= \cancel\ln(10)\\
(x+6)(x-3) &= 10 \\
x^2+3x-18 &= 10 \\
x^2+3x &= 10 +18 = 28 \\
\text{Completamos el binomio}\\

x^2+3x + \frac 9 4&= 28 +  \frac 9 4\\
\text{Factorizamos}\\
(x+\frac 3 2)^2 &= \frac {121}{4}\\
\sqrt{(x+\frac 3 2)^ 2} &= \sqrt\frac {121}{4} \\
x+\frac 3 2 &= \frac {11}{2} \\
x &= \frac {11}{2} -\frac 3 2 = \frac 8 2 = 4\\
x &= 4 \quad \blacksquare
\end{split}
$$

***

### $7e^x-e^{2x}=12$

$$

$$



## 4. Calcule la derivada de las siguientes funciones.

### $f(x)=x(\sin (\ln x)-\cos(\ln x))$

Usando la regla de cadena, $\frac {d} {dx}(f(x)) = \frac{df(u)}{du} \cdot \frac{du}{dx}$, donde $u =x$ y $\frac {d}{du}(f(u))=f'(u)$:
$$
\big(\frac{d}{dx}(x)\big)f'(x) = \frac{d}{dx}(x(-\cos(\log(x))+\sin(\log(x))))
$$
La derivada de $x$ es $1$
$$
f'(x) = \frac{d}{dx}(x(-\cos(\log(x))+\sin(\log(x))))
$$
Usando la regla del producto, $\frac{d}{dx}(uv)=v\frac{du}{dx}+u\frac{dv}{dx}$, donde $u=x$ y $v= \sin(\log(x)) - \cos(\log(x))$:
$$
f'(x)=x\Big(\frac{d}{dx}\big(-\cos(\log(x))+\sin(\log(x))\big)\Big) + \Big(\frac{d}{dx}(x)\Big)\Big(-\cos(\log(x))+ \sin(\log(x))\Big)
$$
Derivamos cada término de la suma
$$
f'(x)=x\Big(\frac{d}{dx}\big(-\cos(\log(x))+\sin(\log(x))\big)\Big) - \Big(\frac{d}{dx}(\cos(\log(x)))\Big)+\Big(\frac{d}{dx}\sin(\log(x))\Big) x
$$
Usando la regla de la cade, $\frac{d}{dx}(\cos(\log(x))) = \frac{d\cos(u)}{du}\cdot\frac{du}{dx}$, donde $u=log(x)$ y $\frac{d}{du}(\cos(u))=-\sin(u)$:
$$
f'(x)=(\frac{d}{dx}(x))(-\cos(\log(x))+ \sin(\log(x)))+ x(\frac{d}{dx}(\sin(\log(x)) -(-\frac{d}{dx}(\log(x)))\sin(\log(x)))) \\
= f'(x)=(\frac{d}{dx}(x))(-\cos(\log(x))+ \sin(\log(x)))+ x(\frac{d}{dx}(\sin(\log(x)) +\frac{d}{dx}(\log(x)))\sin(\log(x))) \\
$$
Usando la regla de la cadena, $\frac{d}{dx}(\log(x)) = \frac{d\log(u)}{du}\cdot\frac{du}{dx}$, donde $u=x$ y $\frac{d}{du}(\log(u))=1/u$:
$$
f'(x)= (\frac{d}{dx}(x))(-\cos(\log(x))+ \sin(\log(x)))+x(\frac{d}{dx}(\sin(\log(x)))+\frac{\frac{d}{dx}(x)}{x}\sin(\log(x)))
$$
La derivada de $x$ es $1$
$$
f'(x)=x\Big( \frac{d}{dx}(\sin(\log(x)))+\frac{(\frac{d}{dx}(x))\sin(\log(x))}{x}\Big)+ (-\cos(\log(x))+\sin(\log(x))) \\
=-\cos(\log(x))+ \sin(\log(x)) + x \Big(\frac{d}{dx}(\sin(\log(x))) + \frac{\frac{d}{dx}(x)\sin(\log(x))}{x} \Big)
$$
Usando la regla de la cadena, $\frac{d}{dx}(\sin(\log(x)))= \frac{d\sin(u)}{du}\frac{du}{dx}$, donde $u = \log(x)$ y $\frac{d}{du}(\sin(u))= \cos(u)$:
$$
f'(x) = -\cos(\log(x)) + \sin(\log(x)) + x\Big(\frac{(\frac{d}{dx}(x))\sin(\log(x))}{x} + \cos(\log(x))(\frac{d}{dx}(\log(x))) \Big)
$$
Usando la regla de la cadena, $\frac{d}{dx}(\log(x))= \frac{d\log(u)}{dx}\frac{du}{dx}$. donde $u=x$ y $\frac{d}{du}(\log(u))=\frac{1}{u}$:
$$
f'(x)= -\cos(\log(x)) + \sin(\log(x)) + x\Big(\frac{(\frac{d}{dx}(x))\sin(\log(x))}{x} + \frac{\frac{d}{dx}(x)}{x}\cos(\log(x))\Big)
$$
La derviada de $x$ es $1$
$$
f'(x)= -\cos(\log(x)) + \sin(\log(x)) + x\Big(\frac{(\frac{d}{dx}(x))\sin(\log(x))}{x} + \frac{\cos(\log(x))}{x}\Big) \\
=  -\cos(\log(x)) + \sin(\log(x)) + x\Big(\frac{\sin(\log(x))}{x} + \frac{\cos(\log(x))}{x}\Big) \\
= 2\sin(\log(x))
$$
Por lo tanto a deriva es 
$$
f'(x)= 2\sin(\log(x)) \quad \blacksquare
$$


### $f(x)= \log _xe$

Usando la regla de la cadena, $\frac{d}{dx}(f(x))= \frac{df(u)}{du}\frac{du}{dx}$, donde $u=x$ y $\frac{d}{du}(f(u))=f'(u)$:
$$
\frac{d}{dx}(x)f'(x)= \frac{d}{dx}(\frac{1}{\log(x)})
$$
La derivada de $x$ es 1:
$$
\frac{d}{dx}(x)f'(x)= \frac{d}{dx}(\frac{1}{\log(x)})
$$
Usando la regla de la cadena, $\frac{d}{dx}(\frac{1}{\log(x)})= \frac{d}{du}\frac{1}{u}\frac{du}{dx}$, donde $u =\log(x)$ y $\frac{d}{du}(\frac{1}{u})=-\frac{1}{u^2}$:
$$
f'(x)= \frac{\frac{d}{dx}(\log(x))}{\log(x)^2}
$$
Usando la regla de la cadena, $\frac{d}{dx}(\log(x))= \frac{d\log(u)}{du}\frac{du}{dx}$, donde $u=x$ y $\frac{d}{du}(\log(u))=\frac{1}{u}$:
$$
f'(x)= - \frac{1}{\log^2(x)}\frac{\frac{d}{dx}(x)}{x}
$$
La derivada de $x$ es $1$
$$
f'(x)= - \frac{1}{x\log^2(x)}
$$
Por lo tanto la derivada es:
$$
f'(x)= - \frac{1}{x\log^2(x)} \quad \blacksquare
$$


### $f(x)= e^{\tan x}$

Usando la regla de la cadena, $\frac{d}{dx}(e^{ \tan(x)}) = \frac{de^u}{du}\frac{du}{dx}$, donde $u= \tan(x)$ y $\frac{d}{du}(e^u)=e^u$
$$
e^{\tan(x)}\big(\frac{d}{dx}(\tan(x))\Big)
$$
Usando la regla de la cadena, $\frac{d}{dx}(\tan(x))=\frac{d\tan(u)}{du}\frac{du}{dx}$, donde $u=x$ y $\frac{d}{du}(\tan(u))=\sec^2(u)$:
$$
= \frac{d}{dx}(x)\sec(x)^2e^{\tan(x)} \\
= 1(e^{\tan(x)}\sec^2(x))
$$
Por lo tanto la derivada es 
$$
f'(x)= e^{\tan(x)}\sec^2(x) \quad \blacksquare
$$


### $f(x)=e^{e^x}$

Usando la regla de la cadena, $\frac{d}{dx}(f(x))= \frac{df(u)}{du}\frac{du}{dx}$, donde $u=x$ y $\frac{d}{du}(f(u))= f'(u)$:
$$
\frac{d}{dx}(x)f'(x)= \frac{d}{dx}(e^{e^x})
$$
La derivada $x$ es 1

Usando la regla de la cadena, $\frac{d}{dx}(e^{e})= \frac{de^u}{du}\frac{du}{dx}$, donde $u=e^x$ y $\frac{d}{du}(e^u)=e^u$:
$$
f'(x)= e^{e^x}\frac{d}{dx}(e^x)
$$
 Uando la regla de la cadena, $\frac{d}{dx}(e^x)= \frac{de^u}{du}\frac{du}{dx}$, donde $u=x$ y $\frac{d}{du}(e^u)= e^u$:
$$
f'(x)= e^x \frac{d}{dx}(x)e^{e^x} = e^{e^x+x}\Big(\frac{d}{dx}(x)\Big)
$$
 La derivada de $x$ es $1$
$$
f'(x)= e^{e^x+x}
$$
Por lo tanto la derivada es
$$
f'(x)= e^{e^x+x} \quad \blacksquare
$$


## 5. Aplica la derivada logarítmica a:

### $f(x)=(1+x)(1-x)$

Calculamos $g(x)$
$$
\begin{split}
g(x) &= \ln|f(x)| \\
&=\ln|(1+x)(1-x)| \\
&=\ln|(1+x)| + \ln|(1-x)| \\
\end{split}
$$
La derivada de $g(x)$ es
$$
g'(x)= \frac{2x}{x^2-1}
$$
Calculamos $f'(x) = f(x)g'(x)$
$$
\begin{split}
f'(x) &= f(x)g'(x) \\
&= \big((1+x)(1-x)\big)\big(\frac{2x}{x^2-1}\big) \\
&= \frac{(2x)(-1)\cancel{(1+x)(1-x)}}{\cancel{x^2-1}} \\
&=-2x

\end{split}
$$
Por lo tanto la derivada es 
$$
f'(x) = 2x \quad \blacksquare
$$

***

### $f(x)= \frac{x^2\sqrt{3-x}}{(1-x)\sqrt[3]{(3+x)^2}}$

$$
\begin{split}
g(x) &= \ln|f(x)| \\
&= \ln |\frac{x^2\sqrt{3-x}}{(1-x)\sqrt[3]{(3+x)^2}}| \\
&= \ln|{x^2\sqrt{3-x}}| - \ln|(1-x)\sqrt[3]{(3+x)^2}| \\
&= \ln|x^2| + \ln|\sqrt{3-x}| - \ln|(1-x)| - \ln |\sqrt[3]{(3+x)^2}| \\
&= 2\ln|x| + 1/2\ln|3-x| - \ln|(1-x)| - 2/3\ln |(3+x)| \\
\end{split}
$$

La derivada de $g(x)$ es
$$
g'(x) = \frac{1}{1-x}-\frac{1}{2 (3-x)}-\frac{2}{3 (3+x)}+\frac{2}{x}
$$
Calculamos $f'(x) = f(x)g'(x)$
$$
\begin{split}
f'(x) &= f(x)g'(x) \\
&=\Big(\frac{x^2\sqrt{3-x}}{(1-x)\sqrt[3]{(3+x)^2}}\Big) \Big(\frac{1}{1-x}-\frac{1}{2 (3-x)}-\frac{2}{3 (3+x)}+\frac{2}{x}\Big) \\
&= \frac{x^2\sqrt{3-x}}{(1-x)^2\sqrt[3]{(3+x)^2}} - \frac{x^2\sqrt{3-x}}{2(1-x)(3-x)\sqrt[3]{(3+x)^2}} - \frac{2x^2\sqrt{3-x}}{3(1-x)(3+x)\sqrt[3]{(3+x)^2}} + \frac{2x^2\sqrt{3-x}}{x(1-x)\sqrt[3]{(3+x)^2}} \\

&= \frac{x^2\sqrt{3-x}}{(1-x)^2\sqrt[3]{(3+x)^2}} - \frac{x^2}{2(1-x)\sqrt{3-x}\sqrt[3]{(3+x)^2}} - \frac{2x^2\sqrt{3-x}}{3(1-x)(3+x)\sqrt[3]{(3+x)^2}} + \frac{2x\sqrt{3-x}}{(1-x)\sqrt[3]{(3+x)^2}} \\

\end{split}
$$
Por lo tanto la derivada es
$$
f'(x) = \frac{x^2\sqrt{3-x}}{(1-x)^2\sqrt[3]{(3+x)^2}} - \frac{x^2}{2(1-x)\sqrt{3-x}\sqrt[3]{(3+x)^2}} - \frac{2x^2\sqrt{3-x}}{3(1-x)(3+x)\sqrt[3]{(3+x)^2}} + \frac{2x\sqrt{3-x}}{(1-x)\sqrt[3]{(3+x)^2}} \quad \blacksquare
$$
