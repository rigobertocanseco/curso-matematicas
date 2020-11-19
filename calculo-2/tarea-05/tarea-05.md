# Tarea 5

**Rigoberto Canseco López**

## Calcular las siguientes integrales

### 1. $\int \cot^3x \ dx$

*Solución*

Usando la fórmula $\int{\cot^n(x)\ dx}=-\frac{\cot^{n-1}(x)}{n-1}-\int\cot^{-2+n}(x) \ dx$, donde $n=3$ 
$$
\begin{split}
&=-\frac{1}{2}\cot^2x-\int\cot x\ dx \\ 
\text{Reemplazamos }\cot x \text{ por } \frac{\cos x}{\sin x}\\ 
&=-\frac{1}{2}\cot^2x-\int \frac{\cos x}{\sin x}\ dx \
\end{split}
$$
Para la integral $\frac{\cos x}{\sin x}$, substituimos $u=\sin x$ y $du=\cos x \ dx$
$$
\begin{split}

&=-\frac{1}{2}\cot^2x-\int \frac{1}{u}\ dx \
\end{split}
$$
La integral de $\frac{1}{u}$ es $\ln u$
$$
-\ln u-\frac 1 2 \cot ^2 x+C
$$
Sustituyendo $u$ por $\sin x$
$$
=-\frac 1 2 \cot^2 x - \ln (\sin x)+C \quad \blacksquare
$$


### 2. $\int x^6 \sin x \ dx$

*Solución*

Por integración por partes para $x^6 \sin x$
$$
\int u \ dv =uv-\int v\ du \\
u =x^6, \quad du=6x^5\ dx, \quad dv=\sin x \ dx, \quad v = -\cos \ x
$$
Tenemos que
$$
=-x^6 \cos x +6 \int x^5 \cos x \ dx
$$
Por integración por partes para $x^5 \cos x$
$$
\int u \ dv =uv-\int v\ du \\
u =x^5, \quad du=5x^4\ dx, \quad dv=\cos x \ dx, \quad v = \sin \ x
$$
Tenemos que
$$
= -x^6 \cos x +6x^5 \sin x -30 \int x^4 \sin x \ dx
$$
Por integración por partes para $x^4 \sin x$
$$
\int u \ dv =uv-\int v\ du \\
u =30x^4, \quad du=4x^3\ dx, \quad dv=\sin x \ dx, \quad v = -\cos \ x
$$
Tenemos que
$$
= 30x^4\cos x-x^6 \cos x +6x^5 \sin x -120 \int x^3 \cos x \ dx
$$
Por integración por partes para $x^3 \cos x$
$$
\int u \ dv =uv-\int v\ du \\
u =x^3, \quad du=3x^2\ dx, \quad dv=\cos x \ dx, \quad v = \sin \ x
$$
Tenemos que
$$
= 30x^4\cos x-x^6 \cos x +6x^5 \sin x -120 x^3 \sin x+360 \int x^2 \sin x \ dx
$$
Por integración por partes para $x^2 \sin x$
$$
\int u \ dv =uv-\int v\ du \\
u =x^2, \quad du=2x\ dx, \quad dv=\sin x \ dx, \quad v = -\cos \ x
$$
Tenemos que
$$
= 30x^4\cos x-x^6 \cos x +6x^5 \sin x -120 x^3 \sin x-360x^2 \cos x +720 \int x \cos x \ dx
$$
Por integración por partes para $x \cos x$
$$
\int u \ dv =uv-\int v\ du \\
u =x, \quad du= dx, \quad dv=\cos x \ dx, \quad v = \sin \ x
$$
Tenemos que
$$
= 30x^4\cos x-x^6 \cos x +6x^5 \sin x -120 x^3 \sin x-360x^2 \cos x +720 x\sin x-720 \int \sin x \ dx
$$
La integral de $\sin x$ es $cos x$
$$
= 30x^4\cos x-x^6 \cos x +6x^5 \sin x -120 x^3 \sin x-360x^2 \cos x +720 x\sin x-720 \cos x + C
$$
Factorizando
$$
=6x(x^4-20x^2+120)\sin x-(x^6-30x^4+360x^2-720)\cos x + C \quad \blacksquare
$$


### 3. $\int \frac{\ln x}{\sqrt x} \ dx$

*Solución*

Por integración por partes para $\frac {\ln x} {\sqrt x}$
$$
\int u \ dv =uv-\int v\ du \\
u =\ln x, \quad du= 1/x \ dx, \quad dv=1/\sqrt x \ dx, \quad v = 2\sqrt  x
$$
Tenemos que
$$
= 2\sqrt x \ln x - 2 \int \frac {1} {\sqrt x} dx
$$
La integral de $1/\sqrt x$ es $2\sqrt x$
$$
= 2\sqrt x \ln x - 4 {\sqrt x} + C
$$
Factorizando
$$
=2\sqrt x(\ln (x) - 2) + C \quad \blacksquare
$$


### 4. $\int 3^x \cos x\ dx$

*Solución*

Por integración por partes para $3^x \cos x$
$$
\int u \ dv =uv-\int v\ du \\
u =\cos x, \quad du= -\sin x \ dx, \quad dv=3^x\ dx, \quad v = 3^x/\ln 3
$$
Tenemos que
$$
= \frac{3^x\cos x}{\ln 3} + \frac{1}{\ln 3} \int 3^x \sin x \ dx
$$
Por integración por partes para $3^x \sin x$
$$
\int u \ dv =uv-\int v\ du \\
u =\sin x, \quad du= \cos x \ dx, \quad dv=3^x\ dx, \quad v = 3^x/\ln 3
$$
Tenemos que
$$
= \frac{3^x\sin x}{\ln^2 3} +\frac{3^x\cos x}{\ln 3} - \frac{1}{\ln^2 3} \int 3^x \cos x \ dx
$$
Agregamos $\frac{1}{\ln^2 3}\int 3^x \cos x dx$ a las dos partes
$$
\big(1+ \frac{1}{\ln^2 3} \big)\int3^x\cos x dx=\frac{3^x \sin x}{\ln^2 3}+ \frac{3^x \cos x}{\ln 3} + C
$$
Dividiendo entre $1+ \frac{1}{\ln^2 3} $
$$
\int3^x\cos x dx=\frac{ \frac{3^x \sin x}{\ln^2 3}+ \frac{3^x \cos x}{\ln 3}}{1+ \frac{1}{\ln^2 3} } + C \\

\frac{ 3^x (\sin x+ \ln 3\cos x)}{1+\ln^2 3} + C \quad \blacksquare
$$




### 5. $\int e^{2x} \sin 3x \ dx$

*Solución*

Por integración por partes para $e^{2x} \sin 3x$
$$
\int u \ dv =uv-\int v\ du \\
u =\sin 3x, \quad du= 3\cos 3x \ dx, \quad dv=e^{2x}\ dx, \quad v = e^{2x}/2
$$
Tenemos que
$$
= \frac 1 2 e^{2x}\sin 3x-\frac 3 2\int e^{2x}\cos 3x \ dx
$$
Por integración por partes para $e^{2x} \cos 3x$
$$
\int u \ dv =uv-\int v\ du \\
u =\cos 3x, \quad du= -3\sin 3x \ dx, \quad dv=e^{2x}\ dx, \quad v = e^{2x}/2
$$
Tenemos que
$$
= \frac 1 2 e^{2x}\sin 3x-\frac 3 4 e^{2x}\cos 3x -\frac 9 4\int e^{2x}\sin 3x \ dx
$$
Agregamos $\frac 9 4\int e^{2x}\sin 3x \ dx$ en ambas partes
$$
\frac {13} {4}\int e^{2x}\sin3x \ dx = \frac 1 2 e^{2x}\sin 3x-\frac 3 4 e^{2x}\cos 3x \cancel{-\frac 9 4\int e^{2x}\sin 3x \ dx +\frac 9 4\int e^{2x}\sin 3x \ dx}
$$
Multiplicando ambas partes por $4/13$
$$
\int e^{2x}\sin3x \ dx = \frac {4}{13}(\frac 1 2 e^{2x}\sin 3x-\frac 3 4 e^{2x}\cos 3x) + C
$$
Factorizando
$$
= \frac {1}{13}e^{2x}(2\sin 3x-3e^{2x}\cos 3x) + C \quad \blacksquare
$$


### 6. $\int \arctan x \ dx$

*Solución*

Por integración por partes para $\arctan x$
$$
\int u \ dv =uv-\int v\ du \\
u =\arctan x, \quad du= 1/(x^2+1) \ dx, \quad dv= dx, \quad v = x
$$
Tenemos que
$$
= x\arctan x - \int \frac{x}{x^2+1}dx
$$
Sustituimos la integral $x/(x^2+1)$ por $u=x^2+1$ y $dU=2x \ dx$
$$
= x \arctan x- \frac 1 2\int \frac 1 u du
$$
La integral de $1/u$ es $\ln x$
$$
= x \arctan x- \frac{\ln u}{2}+ C
$$
Se sustituye $u=x^2+1$
$$
= x \arctan x - \frac 1 2 \ln (x^2+1) + C \quad \blacksquare
$$


### 7. $\int (x^2+2x)\sqrt[4]{x^3+3x^2+9} \ dx$

*Solución*

Para la integral $ (x^2+2x)\sqrt[4]{x^3+3x^2+9}$, sustituimos $u=x^3+3x^2+9$ y $du=(3x^2+6x)$
$$
= \frac 1 3 \int \sqrt[4] u \ du
$$
La integral de $\sqrt[4] u$ es $4 u^{5/4}/5$
$$
= \frac{4u^{5/4}}{15} + C
$$
Sustituimos $u =x^3+3x^2+9$
$$
= \frac{4}{15}(x^3+3x^2+9)^{5/4} + C \quad \blacksquare
$$


### 8. $\int \sec x \tan x \cos (\sec x) \ dx$

*Solución*

Para la integral $\tan x \sec x \cos(\sec x)$, sustituimos $u=\sec x$ y $du=\tan x \sec x dx$
$$
= \int \cos u \ du
$$
La integral de $\cos u$ es $\sin u$
$$
= \sin u + C
$$
Sustituyendo de $u=\sec x$
$$
= \sin \sec x + C \quad \blacksquare
$$
