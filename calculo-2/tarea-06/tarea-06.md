# Tarea 6

**Rigoberto Canseco López**

## 1. $\int \frac 1{x^2+5x+6} \ dx$

Se puede completar la diferencia de cuadrados, $x^2+5x+6=(x+\frac 5 2)^2- \frac 14$
$$
\int \frac{1}{\left(x+\frac{5}{2}\right)^2-\frac{1}{4}} \, dx
$$
   Para la integral $\frac{1}{\left(x+\frac{5}{2}\right)^2-\frac{1}{4}}$, sustituimos $u=x+ \frac 5 2$ y $du=dx$
$$
\int \frac{1}{u^2-\frac{1}{4}} \, du
$$
 Multiplicamos por $4$ el denominar y el nominador 
$$
\int \frac{4}{4 u^2-1} \, du \\
= 4 \int \frac{1}{4 u^2-1} \, du \\
= -4 \int \frac{1}{1-4 u^2} \, du
$$
Para la integral $\frac{1}{1-4 u^2}$, sustituimos  $s=2\ u$ y $ds=2\ du$
$$
-2 \int \frac{1}{1-s^2} \, ds
$$
La integral de $\frac{1}{1-s^2}$ es $\tanh^{-1}(s)$
$$
= -2 \tanh^{-1}(s)+ C
$$
 Sustituimos de regreso $s=2 \ u$
$$
= -2 \tanh^{-1}(2u)+ C
$$
 Sustituimos de regreso $u=x+\frac 5 2$
$$
= -2 \tanh^{-1}(2x+5)+ C
$$
Por lo tanto la integral es igual a 
$$
 -2 \tanh^{-1}(2x+5)+ C \quad \blacksquare
$$


## 2. $\int x^2\sqrt{5-x^2} \ dx$

Para la integral $x^2 \sqrt{5-x^2}$, sustituimos $x=\sqrt{5} (u \sin )$ y $dx=\sqrt 5 \cos u \ du$. Por lo tanto $\sqrt{5-x^2}=\sqrt{5-5\sin^2u}=\sqrt{5} \cos u$ y $u=sin^{-1}(\frac {x} {\sqrt 5})$
$$
=\sqrt{5} \int 5 \sqrt{5} \left(\sin ^2 u\right) \left(\cos ^2 u\right) \, du \\
= 25 \int \left( \sin ^2 u\right) \left(\cos ^2 u\right) \, du
$$
Reescribimos $\cos^2 u$ como $1-\sin^2 u$
$$
=25 \int \left(\sin ^2 u\right) \left(1- \sin ^2 u\right) \, du \\
=  25 \int \left(\sin ^2 u-\sin ^4 u\right) \, du \\
= -25 \int \sin ^2 u \, du-25 \int\sin ^4 u\, du
$$
Usando la fórmula, $\int \sin ^m u\, du=-\frac{(u \cos ) \left( \sin ^{m-1} u\right)}{m} + \frac{m-1}{m}\int \sin ^{-2+m} u \, du$, donde $m=4$
$$
\text{= }\frac{25}{4} \left(\sin ^3u\right) (\cos u)+\frac{25}{4} \int \sin ^2 u\, du
$$
Escribiendo $\sin ^2 u$ como  $\frac{1}{2}-\frac{1}{2} \cos (2 u) $
$$
=\frac{25}{4} \left(\sin ^3u\right) (\cos u)+\frac{25}{4} \int \left(\frac{1}{2}-\frac{1}{2}  \cos (2 u)\right) \, du
$$
Integrando la suma término por término y factorizando las  constantes  
$$
=\frac{25}{4} \left(\sin ^3 u\right) (\cos u)-\frac{25}{8} \int \cos (2 u)  \, du +\frac{25}{8} \int 1 \, du
$$
Para el integrando $\cos 2u$, sustituimos $s=2\ u$ y $ds=2\ du$
$$
=\frac{25}{4} \left(\sin ^3u\right) (\cos u)-\frac{25}{16} \int \cos  s\, ds+\frac{25} {8}\int 1 \, du
$$
La integral de $\cos s $ es $\sin s$
$$
-\frac{25 (\sin s)}{16}+\frac{25}{4} \left(\sin ^3 u\right) (\cos u) +\frac{25}{8} \int 1 \, du
$$
La integral de $1$ es $u$
$$
-\frac{25 (\sin s)}{16}+\frac{25 u}{8}+\frac{25}{4} \left(\sin ^3u\right) (\cos u) +C
$$
Sustituimos $s=2 \ u$
$$
\frac{25 u}{8}+\frac{25}{4} \left( \sin ^3 u\right) ( \cos u)-\frac{25}{8} ( \sin u) (\cos u) +C
$$
Sustituimos $u=\sin ^{-1}(x/\sqrt5)$ 
$$
= \frac {25}{8}\sin^{-1} \frac{x}{\sqrt{5}} + \frac {25}4 \sin(\sin^{-1}(\frac {x}{\sqrt 5} ))^3\cos(\sin^{-1}(\frac {x}{\sqrt 5} )) -  \frac {25}8 \sin(\sin^{-1}(\frac {x}{\sqrt 5} ))\cos(\sin^{-1}(\frac {x}{\sqrt 5} )) + C
$$
Simplificando ${\cos  }({\sin^{{-1}} z})=\sqrt{1-z^2}$ y $\sin(\sin^{-1}z)=z$
$$
= \frac{1}{4} \sqrt{5-x^2} x^3-\frac{5}{8} \sqrt{5-x^2} x+\frac{25 }{8} \sin ^{-1}  \left(\frac {x} {\sqrt{5}}\right) + C \\
= \frac{1}{8} \left(x\left(2 x^2-5\right) \sqrt{5-x^2} +25\sin ^{-1}  \left(\frac {x} {\sqrt{5}}\right)\right) +C 
$$
Por lo tanto la integral es
$$
\frac{1}{8} \left(x\left(2 x^2-5\right) \sqrt{5-x^2} +25\sin ^{-1}  \left(\frac {x} {\sqrt{5}}\right)\right) +C \quad \blacksquare
$$


## 3. $\int \frac 1 {\sqrt {x^2+4}} \ dx$

Para la integral de $\frac{1}{\sqrt{x^2+4}}$, sustituimos $x=2 \tan u$ y $dx=2\sec^2u \ du$. Entonces  $\sqrt{x^2+4} = \sqrt{4 \tan ^2u+4} = 2\sec u$ y $u=\tan^{-1}\frac x 2$
$$
=2 \int \frac{\sec u}{2} \, du \\
= \int {\sec u} \ du
$$
Multiplicando el numerador y denominador de $\sec u$ por $\tan u + \sec u$
$$
= \int \frac{\sec ^2 u+(\sec  u) (\tan  u)}{\sec  u+\tan  u} \ du
$$
Para la integral de $\frac{\sec ^2 u+(\sec  u) (\tan  u)}{\sec  u+\tan  u}$, sustituimos $s=\tan u + \sec u$ y $ds= \sec ^2 u+(\tan u) (\sec u) \ du$
$$
= \int \frac{1}{s} \, ds
$$
La integral de $\frac 1 s$ es $\ln s$
$$
= \ln s + C 
$$
Sustituyendo $s= \tan u+ \sec u$
$$
\ln  (\tan u+\sec u) + C
$$
Sustituyendo $u = \tan^{-1} \left(\frac{x}{2}\right)$
$$
= \ln(\tan(\tan^{-1}\frac x 2)+ \sec(\tan^{-1}\frac x 2)) + C
$$
Simplificando $\sec  {\tan^{-1} z}=\sqrt{z^2+1}$ y $\tan  ({\tan ^{-1}z) }=z$
$$
= \ln(\frac 1 2(\sqrt{x^2+4}+x))+C
$$
Por lo tanto la integral es 
$$
\ln(\frac 1 2(\sqrt{x^2+4}+x))+C \quad \blacksquare
$$


## 4. $\int \frac{1}{3x^2-x+1} \ dx $

Se completa el binomio cuadrado $3 x^2-x+1$
$$
= \int \frac{1}{\left(\sqrt{3} x-\frac{1}{2 \sqrt{3}}\right)^2+\frac{11}{12}} \ dx
$$
 Para la integral $\frac{1}{\left(\sqrt{3} x-\frac{1}{2 \sqrt{3}}\right)^2+\frac{11}{12}}$, sustituimos $u=\sqrt{3} x-\frac{1}{2 \sqrt{3}}$ y $du=\sqrt{3} \ dx$
$$
=\frac{1}{\sqrt{3}}\int \frac{1}{u^2+\frac{11}{12}} \ du \\
= \frac{1}{\sqrt{3}}\int \frac{12}{11 \left(\frac{12 u^2}{11}+1\right)} \ du \\
= \frac{4 \sqrt{3}}{11}\int \frac{1}{\frac{12 u^2}{11}+1} \ du
$$
Para la integral $\frac{1}{\frac{12 u^2}{11}+1}$ , sustituimos $s=2 \sqrt{\frac{3}{11}} \ u$ y $ds=2 \sqrt{\frac{3}{11}} \ du$
$$
=\frac{2}{\sqrt{11}}\int \frac{1}{s^2+1} ds
$$
La integral de $\frac{1}{s^2+1}$ es $\tan^{-1}s$
$$
\frac{2  \tan^{-1} s}{\sqrt{11}}+C
$$
Sustituimos $s= 2 \sqrt{\frac{3}{11}} u$
$$
=\frac{2  \tan^{-1}\left(2 \sqrt{\frac{3}{11}} u\right)}{\sqrt{11} } +C
$$
Sustituimos $u = \sqrt{3} x-\frac{1}{2 \sqrt{3}}$
$$
= \frac{2  \tan^{-1} \frac{(6 x-1) } {\sqrt{11} } }{\sqrt{11}}  +C 
$$
Por lo tanto la integral es
$$
\frac{2  \tan^{-1} \frac{(6 x-1) } {\sqrt{11} } }{\sqrt{11}}  +C \quad \blacksquare
$$


## 5. $\int \frac{\sqrt{1-x^2}}{x^2} \ dx$

Sustituimos $x = \sin u$ y $dx=\cos u\  du$. Entonces $\sqrt{1-x^2}= \sqrt{1-u \sin ^2}=\cos u$ y $u= \sin^{-1}x$
$$
= \int \cot ^2 u\, du
$$
Reescribimos $ \cot ^2 u$ como $\csc^2u-1$
$$
= \int \csc ^2 u -1 \ du
$$
Integramos la suma término por término 
$$
= \int \csc ^2 u\, du-\int 1 \, du
$$
La integral de $\csc^2u$ es $-\cot u$
$$
=-\cot u-\int 1 \, du
$$
La integral de $1$ es $u$
$$
=-u -\cot u + C
$$
 Sustituimos $u=\sin^{-1} x$
$$
-{\sin^{-1} x}-\cot  ({\sin^{-1} x}) +C
$$
Simplificamos usando $\cot(\sin^{-1}z)= \frac{\sqrt{1-z^2}}{z}$
$$
= -\frac{\sqrt{1-x^2}+x \ {\sin^{-1} x}}{x} +C
$$
Por lo tanto la integral buscada es
$$
 -\frac{\sqrt{1-x^2}+x \ {\sin^{-1} x}}{x} +C \quad \blacksquare
$$


## 6. $\int \frac{x^3-1}{4x^3-x} \ dx$



## 7. $\int \frac{e^x}{\sqrt{1+e^x+e^{2x}}} \ dx$

Para la integral  $\frac{e^x}{\sqrt{1+e^x+e^{2x}}} $, sustituimos $u=e^x$ y $du=e^x \ dx$
$$
=\int \frac{1}{\sqrt{u^2+u+1}} \ du
$$
Completamos el cuadrado 
$$
=\int \frac{1}{\sqrt{\left(u+\frac{1}{2}\right)^2+\frac{3}{4}}} \ du
$$
Para la integral $\frac{1}{\sqrt{\left(u+\frac{1}{2}\right)^2+\frac{3}{4}}}$, substituimos $s=u+\frac 1 2$ y $ds=du$
$$
=\int \frac{1}{\sqrt{s^2+\frac{3}{4}}} \, ds
$$
Para la integral $\frac{1}{\sqrt{s^2+\frac{3}{4}}}$, substituimos $s= \frac 1 2 \sqrt 3 \tan r$ y $ds= \frac 1 2 \sqrt 3 \sec^2r \ dr$. Entonces $\sqrt{s^2+\frac{3}{4}}= \sqrt{\frac{3}{4} \left( \tan ^2r\right)+\frac{3}{4}} = \frac{1}{2} \sqrt{3} ( \sec r)$ y $r= \tan^{-1} \frac{2 s}{\sqrt{3}}$
$$
=\frac{\sqrt{3}}{2}\int \frac{2 ( \sec r)}{\sqrt{3}} \ dr \\
= \int \sec r \ dr
$$
La integral de $\sec r$ es $\ln(\tan r+\sec r)$
$$
=\ln(\tan r+ \sec r)+C
$$
Substituimos $p = {\tan^{-1} }\left(\frac{2 s}{\sqrt{3}}\right)$
$$
=\ln  \left(
\tan ({\tan ^{-1}\frac { 2 s}{ \sqrt{3}})} + \sec( \tan^{-1}\frac{ 2 s}{  \sqrt{3}})
\right) +C
$$
Simplificamos ${\sec \ }{\tan^{-1} z}=\sqrt{z^2+1}$ y ${\tan  \ }{\tan^{-1} z}=z$
$$
=\ln\frac{\left(\sqrt{4 s^2+3}+2 s\right) }{\sqrt{3}} +C
$$
Sustituimos $s=u+ 1/2$
$$
= \ln \frac{2 \sqrt{u^2+u+1}+2 u+1  }{\sqrt{3}}+C
$$
Se sustituye $u=e^x$
$$
\ln \frac{2 \sqrt{e^x+e^{2 x}+1}+2 e^x+1  }{\sqrt{3}}+C 
$$
Por lo tanto la integral buscada es
$$
\ln \frac{2 \sqrt{e^x+e^{2 x}+1}+2 e^x+1  }{\sqrt{3}}+C  \quad \blacksquare
$$


## 8. $\int  \frac{x^4+4x^3-5x^2+2x-6}{x^2(x-1)^3}$

