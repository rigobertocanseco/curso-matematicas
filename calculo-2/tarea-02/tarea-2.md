# Tarea II

### Calcular las siguientes derivadas.

#### 1. $\bf y= x^5-4x^3+2x-3$

Tenemos que la función $f(x)=x^5-4x^3+2x-3$

La derivada de un polinomio es $f'(x)= \sum_{k=1}^{n}{kc}_kx^{k-1}$ por lo tanto podemos derivar cualquier polinomio sumando las derivadas de cada uno de los términos.

Tenemos que la deriva de $f(x)$ es
$$
\begin{equation}
\begin{split}
f'(x) &= (5)(x^{5-1}) - (3)(4x^{3-1}) + (1)(2x^{1-1}) - (0)(3) \\
&= 5x^4 - 12x^2 + 2
\end{split}
\end{equation}
$$
Por lo tanto
$$
f'(x)=5x^4-12x^2+2 \quad	\blacksquare
$$

***

#### 2. $\bf y=(x+2)^8(x-3)^4$

La función $f(x) = (x+2)^8(x-3)^4$ 

Tenemos que la derivada del producto de dos funciones es igual a 
$$
(fg)'(x) = f'(x)g(x) + f(x)g'(x)
$$
Donde $f(x) = (x+2)^8$ y $g(x)=(x-3)^4$. 

* Calculamos la derivada de $f'(x)$ usando el teorema de la derivada de la potencia de una función con exponente entero positivo, que dice :

  Si  $n \in \N$ y $f(x)=v^n \ \forall x \in \N$ entonces $f'(x) = nv^{n-1} v'(x) \ \forall x \in \R$. 

  Donde $v = (x+2)$ y $n= 8$
  $$
  \begin{equation}
  \begin{split}
  f'(x) &= (8)(x+2)^{8-1} \\
  &= 8(x+2)^7
  \end{split}
  \end{equation}
  $$
  Por lo tato tenemos que 
  $$
  f'(x)g(x) = (8(x+2)^7)(x-3)^4
  $$

* Calculamos la derivada de $g'(x)$  usando el teorema de la derivada de la potencia de una función con exponente entero positivo, que dice :

  Si  $n \in \N$ y $f(x)=v^n \ \forall x \in \N$ entonces $f'(x) = nv^{n-1} v'(x) \ \forall x \in \R$. 

  Donde $v = (x-3)^4$ y $n = 4$
  $$
  \begin{equation}
  \begin{split}
  f'(x) &= (4)(x-3)^{4-1} \\
  &= 4(x-3)^3
  \end{split}
  \end{equation}
  $$
  Por lo tanto tenemos que
  $$
  f(x)g'(x)= ((x+2)^8)(4(x-3)^3)
  $$

Sumando ambos términos
$$
\begin{equation}
\begin{split}
(fg)'(x) &= f'(x)g(x) + f(x)g'(x) \\
&= (8(x+2)^7)(x-3)^4 + (x+2)^8(4(x-3)^3) \\
&= 8(x-3)^4(x+2)^7+4(x-3)^3(x+2)^8 \\
&= 4(x-3)^3(x+2)^7(2(x-3)+(x+2)) \\
&= 4(x-3)^3(x+2)^7(2x-6+x+2) \\
&= 4(x-3)^3(x+2)^7(3x-4) \\ 
\end{split}
\end{equation}
$$
Por lo tanto 
$$
f'(x)=4(x-3)^3(x+2)^7(3x-4) \quad	\blacksquare
$$

***

#### 3. $\bf y=sec \ 2x$

Sea la función $f(x) = sec \ 2x$

La secante  es el inverso multiplicativo del coseno por lo tanto $sec \ x = \frac{1}{cos \ x}$, por lo tanto $f(x) = \frac{1}{cos \ 2x}$. 

Ahora calculamos la derivada de $f'(x)$ 

Por el teorema que dice: 

Si $f$ es derivable y $f(a) \ne 0$ entonce $\frac{1}{f(x)}$ es derivable en $a$ y 
$$
(\frac{1}{f})'(a)=\frac{-1}{f^2(a)}f'(a)
$$
Donde $a = cos \ 2x$

Por lo tanto 
$$
\begin{equation}
\begin{split}
(\frac{1}{f})'(a)=\frac{-1}{cos^2 \ (2x)}(cos \ 2x)'
\end{split}
\end{equation}
$$

Ahora la derivada del coseno es $cos'(u) = - sen \ u \cdot u'(x), \ \forall x \in \R$ 

Donde $u = 2x$
$$
(cos \ 2x)' = - sen \ 2x \cdot (2x)'
$$
Y la derivada de $(2x)'$ es 2 por lo tanto 
$$
\begin{equation}
\begin{split}
f'(x) &= \frac{-1}{cos ^2(2x)}(-sen (2x)(2))   \\
&= \frac{2 \cdot sen (2x)}{cos^2(2x)}
\end{split}
\end{equation}
$$
Por lo tanto 
$$
 f'(x)= \frac{2 \cdot sen (2x)}{cos^2(2x)} \quad	\blacksquare
$$

***

#### 4. $\bf y=sen(cos \ x)$

Sea la función $f(x) = sen (cos \ x)$

Calculamos la derivada del seno que es $sen' \ (u) = cos \ (u) \cdot u'(x)$.

Donde $u = cos (x)$
$$
sen ' (u) = cos(cos \ (x)) \cdot u'(x)
$$
Ahora la derivada de $u'(x)$ que es la derivada del coseno es el $cos' (x) = -sen (x)$, por lo tanto
$$
u'(x) = -sen(x)
$$
La deriva de $f'(x)$ es 
$$
\begin{equation}
\begin{split}
f'(x) &= sen' (u) = cos(u) \cdot u'(x)  \\
&= cos(cos(x)) \cdot (-sen(x)) \\
&= -sen(x)\cdot cos(cos(x))
\end{split}
\end{equation}
$$
Por lo tanto
$$
f'(x)= -sen(x)\cdot cos(cos(x)) \quad	\blacksquare
$$

***

#### 5. $\bf y = \sqrt{1-3x^5}$

Sea la función $f(x)=\sqrt{1-3x^5}$

Calculamos la derivada de $\frac{dy}{dx}$ usando la regla para calcular la derivada de una raíz cuadrada
$$
\frac{d\sqrt{u}}{du} \cdot \frac{du}{dx}
$$
Donde
$$
u = 1-3x^5 \quad \text{y} \quad \frac{d\sqrt{u}}{du} = \frac{1}{2\sqrt{u}}
$$
Por lo tanto tenemos que
$$
\frac{1}{2\sqrt{1-3^5}} \cdot \frac{dy}{dx}(1-3x^5)
$$

* Derivamos $\frac{dy}{dx}(1-3x^5)= \frac{dy}{dx}1 - \frac{dy}{dx}3x^5$  , es igual a
  $$
  \frac{dy}{dx}1 = 0 \quad \text { La derivada de una constante es 0} \\
  - \frac{dy}{dx}3x^5 = 15x^4 \quad \text {Usando la regla de la potencia  }
  $$
  Por lo tanto,
  $$
  \frac{dy}{dx}(1-3x^5)= 0 -  15x^4
  $$

* 

Tenemos que 
$$
\frac{1}{2\sqrt{1-3^5}} \cdot \frac{dy}{dx}(1-3x^5) = \frac{1}{2\sqrt{1-3x^5}} \cdot (-15x^4)
$$
Por lo tanto
$$
\frac{dy}{dx}=  \frac{-15x^4}{2\sqrt{1-3x^5}} \quad \blacksquare
$$

***

#### 6. $\bf y = (5+2cos5x)^{10}$

Sea la función $f(x)= (5+2cos5x)^{10}$

Calculamos la derivada $\frac{dy}{dx}$ usamos la regla para derivar una potencia
$$
\frac{du^{n}}{du} \cdot \frac{du}{dx}
$$
 Donde 
$$
u = (5+2cos5x) \quad \text y \quad n = 10
$$

* La derivada de $\frac{d}{du}(u^{10})= 10u^9$
  $$
  = (10(5+2cos5x)^9)(\frac{d}{dx}(5+2cos5x))
  $$

* Derivamos $\frac{d}{dx}(5+2cos5x)$
  $$
  = \frac{d}{dx}5 + \frac{d}{dx}(2 \ cos\ 5x)
  $$

  * $$
    \frac{d}{dx}5 = 0
    $$

    

    Usamos la regla de la derivada para coseno $\frac{dcos(u)}{du} \cdot \frac{du}{dx}$

  * $$
    \frac{d}{dx}(2 \ cos \ 5x), \\
    \text{donde } u = 5x \\
    \text{ y}\\
    \frac{d}{du}(cos(u))= -sin(u)
    $$

    Por lo tanto tenemos 
    $$
    2 \frac{d}{dx}(\ cos \ 5x) = -sin(5x)(\frac{d}{dx}5x) = 2(-5sin(5x))
    $$

  La derivada resultante es
  $$
  2\frac{d}{dx}(5+2cos5x) = 0 + -5 \ sin (5x) = 2(-5 \ sin(5x))
  $$
  

La derivada resultante de
$$
\begin{split}
&= (10(5+2cos5x)^9)2(\frac{d}{dx}(5+2cos5x)) \\
&= (10(5+2cos5x)^9)2(-5 \ sin(5x)) \\
&= -100(5+2 \ cos \ 5x)^9 sin \ 5x
\end{split}
$$
Por lo tanto 
$$
\frac{dy}{dx}=  -100(5+2 \ cos \ 5x)^9 sin \ 5x \quad \blacksquare
$$

***

#### 7. $\bf y = \frac{4-x}{3+x}$

Sea la funcion $f(x)= \frac{4-x}{3+x}$

Calculamos la drivada $\frac{dy}{dx}$ usando la regla de cociente, 
$$
\frac{d}{dx}\frac{u}{v}=\frac{v \frac{du}{dx}-u \frac{dv}{dx}}{v^2}
$$
Donde 
$$
u = 4-x \quad \text y \quad v = 3+x
$$


Por lo tanto 
$$
\frac{dy}{dx}= \frac{(3+x)(\frac{d}{dx}(4-x)) - (4-x)(\frac{d}{dx}(3+x))}{(3+x)^2}
$$
Derivamos $\frac{d}{dx}(4-x)$:
$$
= \frac{d}{dx}4 - \frac{d}{dx}x = 0 - 1 = -1
$$
Derivamos $\frac{d}{dx}(3+x)$:
$$
= \frac{d}{dx}3 + \frac{d}{dx}x = 0 + 1 = 1
$$
Por lo tanto tenemos que
$$
\begin{split}
&= \frac{(3+x)(\frac{d}{dx}(4-x)) - (4-x)(\frac{d}{dx}(3+x))}{(3+x)^2} \\
&= \frac{(3+x)(-1) - (4-x)(1)}{(3+x)^2} \\
&= \frac{-3-x-4+x}{(3+x)^2} \\
&= \frac{-7}{(3+x)^2}
\end{split}
$$
Por lo tanto
$$
\frac{dy}{dx}= \frac{-7}{(3+x)^2} \quad \blacksquare
$$

***

#### 8. $\bf y = \frac{x}{\sqrt{9-4x}}$

Sea la función $f(x) = \frac{x}{\sqrt{9-4x}}$ 

Calculamos la derivada usando la regla del producto
$$
\frac{d}{dx}u v=v \frac{du}{dx}+u \frac{dv}{dx},
$$
Donde
$$
u = \frac{1}{\sqrt{9-4x}} \quad \text y \quad v = x
$$
Por lo tanto
$$
\frac{dy}{dx} = x(\frac{d}{dx}\frac{1}{\sqrt{9-4x}}) + \frac{1}{\sqrt{9-4x}}(\frac{d}{dx}x)
$$
Derivamos: $\frac{d}{dx}\frac{1}{\sqrt{9-4x}}$

* Usando la regla de la derivada para una raiz $\frac{d}{du}\frac{1}{\sqrt{u}}\text{}\frac{du}{dx}$

  Donde 
  $$
  u = 9-4x \quad y \quad \frac{d}{du}\frac{1}{\sqrt{u}} = - \frac{1}{2u^{3/2}}
  $$

  $$
  = - \frac{1}{2u^{3/2}}(\frac{d}{dx}(9-4x))
  $$

  Derivamos $\frac{d}{dx}(9-4x)$
  $$
  = \frac{d}{dx}9 - 4x\frac{d}{dx} = 0 - 4 = -4
  $$
  Por lo tanto tenemos que
  $$
  \begin{split}
  \frac{d}{dx}\frac{1}{\sqrt{9-4x}} &= - \frac{1}{2u^{3/2}}(\frac{d}{dx}(9-4x)) \\
  &= - \frac{1}{2u^{3/2}}(-4) \\
  &= \frac{2}{u^{3/2}} \quad \text {sustituyendo} \ u \\
  &=  \frac{2}{(9-4x)^{3/2}} 
  \end{split}
  $$

Calculamos la derivada de: $\frac{d}{dx}x$ 
$$
\frac{d}{dx}x = 1
$$
Sustutuyendo las  2 derivadas obtenidas previamente
$$
\begin{split}
\frac{dy}{dx} &= x(\frac{d}{dx}\frac{1}{\sqrt{9-4x}}) + \frac{1}{\sqrt{9-4x}}(\frac{d}{dx}x) \\
&= x(\frac{2}{(9-4x)^{3/2}}) + \frac{1}{\sqrt{9-4x}}(1) \\
&= \frac{2x}{(9-4x)^{3/2}} + \frac{1}{\sqrt{9-4x}} \\
&= \frac{2x}{(9-4x)^{3/2}} + \frac{1}{\sqrt{9-4x}} \\
&= \frac{2x}{(9-4x)^{3/2}} + \frac{1}{\sqrt{9-4x}}(\frac{9-4x}{9-4x}) \\
&= \frac{2x+(9-4x)}{(9-4x)^{3/2}}  \\
&= \frac{-2x+9}{(9-4x)^{3/2}}  \\
\end{split}
$$
Por lo tanto
$$
\frac{dy}{dx}= \frac{-2x+9}{(9-4x)^{3/2}}  \quad \blacksquare
$$

***

#### 9.  $\bf y=\frac{sen \ x + cos \ x}{sen \ x - cos \ x}$

Sea la funcion $f(x) = \frac{sen \ x + cos \ x}{sen \ x - cos \ x}$

Calculamos la drivada $\frac{dy}{dx}$ usando la regla de cociente, 
$$
\frac{d}{dx}\frac{u}{v}=\frac{v \frac{du}{dx}-u \frac{dv}{dx}}{v^2}
$$
Donde 
$$
u=sen \ x + cos \ x  \quad \text y \quad v = sen \ x - cos \ x
$$
Por lo tanto
$$
\frac{dy}{dx} = \frac{(sen \ x-cos \ x)(\frac{d}{dx}(sen \ x + cos \ x)) - (sen \ x + cos \ x )(\frac {d}{dx}(sen \ x - cos \ x))}{(sen \ x - cos \ x)^2}
$$
Derivamos $\frac{d}{dx}(sen \ x + cos \ x)$:

* Derivamos el término $\frac{d}{dx}sen \ x$:

  Usando la regla para derivar el seno tenemos que
  $$
  \frac{d}{dx}sen \ x = \frac{d \ sen \ u}{du} \frac{du}{dx} 
  $$
  Donde 
  $$
  u = x \quad \text y \quad \frac{d}{du} \ sen \ u = cos \ u 
  $$
  Por lo tanto tenemos que la derivadea de $\frac{d}{dx}sen \ x$
  $$
  \begin{split}
  \frac{d}{dx}sen \ x &= xdx(\frac{d}{dx}sen \ x) \\
  &= 1 (cos \ x) \\
  & = cos \ x
  \end{split}
  $$

* Derivamos el término $\frac{d}{dx}cos \ x$

  Usando la regla para derivar el seno tenemos que

$$
\frac{d}{dx}cos \ x = \frac{d \ cos \ u}{du} \frac{du}{dx}
$$

​		Donde 
$$
u = x \quad \text y \quad \frac{d}{du} \ cos \ u = -sen \ u
$$
​		Por lo tanto tenemos que la derivadea de $\frac{d}{dx}cos \ x$
$$
\begin{split}
\frac{d}{dx}cos \ x &= xdx(\frac{d}{dx}cos \ x) 
\\&= 1 (-sen \ x) \\
& = -sen \ x
\end{split}
$$
Derivamos $\frac{d}{dx}(sen \ x - cos \ x)$:

* Derivamos el término $\frac{d}{dx}sen \ x$:

  Usando la regla para derivar el seno tenemos que
  $$
  \frac{d}{dx}sen \ x = \frac{d \ sen \ u}{du} \frac{du}{dx} 
  $$
  Donde 
  $$
  u = x \quad \text y \quad \frac{d}{du} \ sen \ u = cos \ u 
  $$
  Por lo tanto tenemos que la derivadea de $\frac{d}{dx}sen \ x$
  $$
  \begin{split}
  \frac{d}{dx}sen \ x &= xdx(\frac{d}{dx}sen \ x) \\
  &= 1 (cos \ x) \\
  & = cos \ x
  \end{split}
  $$

* Derivamos el término $\frac{d}{dx}- cos \ x$

  Usando la regla para derivar el seno tenemos que

$$
-\frac{d}{dx}cos \ x = \frac{d \ cos \ u}{du} \frac{du}{dx}
$$

​		Donde 
$$
u = x \quad \text y \quad \frac{d}{du} \ cos \ u = -sen \ u
$$
​		Por lo tanto tenemos que la derivadea de $\frac{d}{dx}cos \ x$
$$
\begin{split}
-\frac{d}{dx}cos \ x &= xdx(\frac{d}{dx}cos \ x) 
\\&= -1 (-sen \ x) \\
& = sen \ x
\end{split}
$$
Sustituimos las derivadas en $\frac{dy}{dx}$:
$$
\begin{split}
\frac{dy}{dx} &= \frac{(sen \ x-cos \ x)(\frac{d}{dx}(sen \ x + cos \ x)) - (sen \ x + cos \ x )(\frac {d}{dx}(sen \ x - cos \ x))}{(sen \ x - cos \ x)^2} \\

&= \frac{(sen \ x-cos \ x)(cos \ x - sen \ x) - (sen \ x + cos \ x )(cos \ x + sen \ x)}{(sen \ x - cos \ x)^2} \\
\text{Simplificando la ecuación:} \\

&= \frac{sen \ x \cdot cos \ x - sen^2 \ x- cos ^2 \ x+cos \ x \cdot sen \ x}{(sen \ x - cos \ x)^2} \\
&- \frac{(sen \ x \cdot cos \ x+ sen ^2 \ x+ sen \ x\cdot cos \ x + cos^2 \ x)}{(sen \ x - cos \ x)^2} \\
&=\frac{-2 sen^2  \ x-2 cos^2 \ x}{(sen \ x - cos \ x)^2} \\
&= \frac{-2(sen^2 \ x + cos^2 \ x)}{(sen \ x- cos \ x)^2}

\end{split}
$$
Por lo tanto
$$
\frac{dy}{dx}= \frac{-2(sen^2 \ x + cos^2 \ x)}{(sen \ x- cos \ x)^2} \quad \blacksquare
$$

***

#### 10. $\bf y=\sqrt{cot \ x} - \sqrt{csc \ x}$

Sea la función $f(x)= \sqrt{cot \ x} - \sqrt{csc \ x}$

Derivamos cada elemento de la resta 
$$
\frac{dy}{dx} =\frac{d}{dx}\sqrt{cot \ x} - \frac{d}{dx}\sqrt{csc \ x}
$$

* Calculamos la drivada $\frac{d}{dx}\sqrt{cot \ x}$ usando la regla de raiz, 

$$
\frac{d}{dx} \sqrt{x \cot }= \frac{d\sqrt{u}}{du} \frac{du}{dx}
$$

​		Donde 
$$
u = cot \ x \quad \ \text y \quad \frac{d\text{}}{du}\left(\sqrt{u}\right)=\frac{1}{2 \sqrt{u}}
$$
​		Por lo tanto 
$$
\frac{\frac{d}{dx}x \cot x}{2 \sqrt{\cot  x}}
$$
​		La derivada de $\frac{d}{dx} x \ cot \ x$
$$
\frac{d}{dx} x \cot \ x=\frac{d\cot (u)}{du} \frac{du}{dx} \\
\text{Donde}\\
u = x \quad \text{y} \quad \frac{d\text{}}{du}(\cot  u)=-\left(\csc ^2 u\right)
$$
​			Por lo tanto
$$
\frac{d}{dx}\sqrt{cot \ x} = \frac{\frac{d}{dx}x \cot x}{2 \sqrt{\cot  x}} = \frac{-\ csc^2 \ x}{2 \sqrt{\cot  x}}
$$


* Calculamos la drivada $\frac{d}{dx}\sqrt{csc \ x}$ usando la regla de raiz, 

$$
\frac{d}{dx} \sqrt{x \csc }= \frac{d\sqrt{u}}{du} \frac{du}{dx}
$$

​		Donde 
$$
u = csc \ x \quad \ \text y \quad \frac{d\text{}}{du}\left(\sqrt{u}\right)=\frac{1}{2 \sqrt{u}}
$$
​		Por lo tanto 
$$
\frac{\frac{d}{dx}x \csc x}{2 \sqrt{\csc  x}}
$$
​		La derivada de $\frac{d}{dx} x \ csc \ x$
$$
\frac{d}{dx} x \csc \ x=\frac{d\csc (u)}{du} \frac{du}{dx} \\
\text{Donde}\\
u = x \quad \text{y} \quad \frac{d\text{}}{du}(\cot  u)=-cot \ u \cdot csc \ u
$$
​			Por lo tanto
$$
\frac{d}{dx}\sqrt{csc \ x} = \frac{\frac{d}{dx}x \csc x}{2 \sqrt{\csc  x}} = \frac{-\ cot \ x \cdot csc \ x}{2 \sqrt{\csc  x}}
$$
Sustituyendo las derivas en
$$
\frac{dy}{dx} =\frac{d}{dx}\sqrt{cot \ x} - \frac{d}{dx}\sqrt{csc \ x}
$$
Tenemos que:
$$
\begin{split}
\frac{dy}{dx} &= \frac{d}{dx}\sqrt{cot \ x} - \frac{d}{dx}\sqrt{csc \ x} \\
&= \frac{-\ csc^2 \ x}{2 \sqrt{\cot  x}} - \frac{-\ cot \ x \cdot csc \ x}{2 \sqrt{\csc  x}} \\
&= \frac{-\ csc^2 \ x}{2 \sqrt{\cot  x}} + \frac{\ cot \ x \cdot csc \ x}{2 \sqrt{\csc  x}} \\
\end{split}
$$
Por lo tanto
$$
\frac{dy}{dx}=  \frac{-\ csc^2 \ x}{2 \sqrt{\cot  x}} + \frac{\ cot \ x \cdot csc \ x}{2 \sqrt{\csc  x}}  \quad \blacksquare
$$

***

#### 11. $ \bf {y = arc \ cos \ 2x}$

Sea la función $f(x)= arc \ cos \ 2x = cos ^ {-1} \ 2x$

Usando la regla para calcular la derivada de $\frac{d}{dx} (cos^{-1} \ 2x)$
$$
\frac{dy}{dx}= \frac{d \ cos ^{-1}(u)}{du} \frac{du}{dx}
$$
Donde 
$$
u = 2x \quad \text{y} \quad \frac{d\text{}}{du}\left(cos ^ {-1} \ u \right)=-\frac{1}{\sqrt{1-u^2}}
$$
Por tanto, tenemos que 
$$
\frac{d}{dx} (cos^{-1} \ 2x) = -\frac{\frac{d}{x d}2 x}{\sqrt{1-4 x^2}}
$$
La derivada de 
$$
\frac{d}{dx}2x = 2(\frac{d}{dx}x) = 2 (1) = 2
$$
Sustituyendo las derivadas calculadas  
$$
\frac{d}{dx} (cos^{-1} \ 2x)  = -\frac{\frac{d}{x d}2 x}{\sqrt{1-4 x^2}} =  -\frac{2}{\sqrt{1-4 x^2}}
$$
Por lo tanto
$$
\frac{dy}{dx}= -\frac{2}{\sqrt{1-4 x^2}} \quad \blacksquare
$$

***

#### 12 . $\bf x^2y^3+3y^2=x-4y$

#### 13. $\bf y= arc \ tan(\frac{1+x}{1-x})$

Sea la función $f(y) = arc \ tan \ (\frac{1+x}{1-x}) = tan ^ {-1}(\frac{1+x}{1-x})$

Usando la regla para derivar un arco tangente 
$$
\frac{d}{dx}\ tan ^{-1} (\frac{x+1}{1-x})=\frac{d\tan ^{-1}u}{du} \frac{du}{dx}
$$
Donde 
$$
u = \frac{x+1}{1-x} \quad \text{y} \quad \frac{d}{du}\left(tan^{-1} u \right)=\frac{1}{u^2+1}
$$
Tenemos que 
$$
\frac{dy}{dx}= \frac{\frac{d}{dx}\frac{x+1}{1-x}}{\frac{(x+1)^2}{(1-x)^2}+1}
$$
Usamos la regla de la división para calcular la derivada de $\frac{d}{dx}\frac{x+1}{1-x}$
$$
\frac{d}{dx}\frac{u}{v}=\frac{v \frac{du}{dx}-u \frac{dv}{dx}}{v^2}
$$
 Donde 
$$
u = x+ 1 \quad \text y \quad v = 1-x
$$
Tenemos que 
$$
= \frac{(1-x)\frac{d}{dx}(x+1)-(x+1)\frac{d}{dx}(1-x)}{(1-x)^2}
$$

* La derivada de $\frac{d}{dx}(x+1)$ es:
  $$
  \frac{d}{dx}(x+1) = \frac{d}{dx}x + \frac{d}{dx}1 = 1 + 0 = 1
  $$

* La derivada de $\frac{d}{dx}(1-x)$ es :
  $$
  \frac{d}{dx}(1-x) = \frac{d}{dx}1 - \frac{d}{dx}x = 0 - 1= -1
  $$

Sustituimos los valores en la derivada  $\frac{d}{dx}\frac{x+1}{1-x}$
$$
\begin{split}
&= \frac{(1-x)\frac{d}{dx}(x+1)-(x+1)\frac{d}{dx}(1-x)}{(1-x)^2} \\
&= \frac{(1-x)(1)-(x+1)(-1)}{(1-x)^2} \\
&= \frac{(1-x)+(x+1)}{(1-x)^2} \\
&= \frac{2}{(1-x)^2} \\ 
\end{split}
$$
Sustituimos la derivada anterior en 
$$
\begin{split}
\frac{dy}{dx} &= \frac{\frac{d}{dx}\frac{x+1}{1-x}}{\frac{(x+1)^2}{(1-x)^2}+1} \\
&= \frac{\frac{2}{(1-x)^2}}{\frac{(x+1)^2}{(1-x)^2}+1}\\
&= \frac{2(1-x)^2}{(1-x)^2((x+1)^2+(1-x)^2)}\\
&= \frac{2}{(x+1)^2+(1-x)^2}\\
&= \frac{2}{x^2+1}\\
\end{split}
$$
Por lo tanto
$$
\frac{dy}{dx}= \frac{2}{(1-x)^2}  \quad \blacksquare
$$

***

#### 14. $y=\frac{-2}{ \sqrt[4]{x^3} }$

Sea la función $f(x)= -2/x^{3/4}$ 

Calcular la derivada
$$
= -2\left(\frac{d}{dx}\frac{1}{x^{3/4}}\right)
$$


Usamos la regla de la potencia para calcular la derivada de $\frac{dy}{dx}$
$$
\frac{d}{dx}x^n=n x^{n-1}
$$
Donde $n = -3/4$, por tanto tenemos que:
$$
\frac{d}{dx}\frac{1}{x^{3/4}}=\frac{d}{dx}x^{-3/4}=\frac{1}{4} (-3) x^{-7/4} \\
= -2(\frac{-3}{4 x^{7/4}})
$$
Tenemos que
$$
\frac{dy}{dx} = \frac{3}{2 x^{7/4}}   \quad \blacksquare
$$

***

#### 15. $\bf y=\frac{1}{\sqrt[3]{x+\sqrt{x}}}$

Sea la funcion $f(x)= \frac{1}{\sqrt[3]{x+\sqrt{x}}}$, encontrar la derivada $\frac{dy}{dx}$.

Derivamos usando la regla para raíz cúbica
$$
\frac{dy}{dx} = \frac{d}{dx}\frac{1}{\sqrt[3]{x+\sqrt{x}}}=\frac{d}{du}\frac{1}{\sqrt[3]{u}} \frac{du}{dx}
$$
Donde 
$$
u = x + \sqrt x \quad y \quad \frac{d\text{}}{du}\left(\frac{1}{\sqrt[3]{u}}\right)=-\frac{1}{3 u^{4/3}}
$$
De modo que
$$
\frac{dy}{dx} = -\frac{\frac{d}{dx}(x+\sqrt{x})}{3 \left(x+\sqrt{x}\right)^{4/3}}
$$

* La derivada $\frac{d}{dx}x$ = 1

* Derivamos $\frac{d}{dx}\sqrt x$ , usando al regla para potencias

$$
\frac{d}{dx}x^n=n x^{n-1}
$$

​		Donde $n = 1/2$
$$
\frac{d}{dx}\sqrt{x}=\frac{d}{dx}x^{1/2}=\frac{x^{-1/2}}{2} = \frac{1}{2 \sqrt{x}}
$$
Sustituimos las valores de las derivadas en 
$$
\begin{split}
\frac{dy}{dx} &= -\frac{\frac{d}{dx}(x+\sqrt{x})}{3 \left(x+\sqrt{x}\right)^{4/3}} \\
&= -\frac{(1+\frac{1}{2 \sqrt{x}})}{3 \left(x+\sqrt{x}\right)^{4/3}} \\
\end{split}
$$
Tenemos que
$$
\frac{dy}{dx} = -\frac{(1+\frac{1}{2 \sqrt{x}})}{3 \left(x+\sqrt{x}\right)^{4/3}}    \quad \blacksquare
$$
