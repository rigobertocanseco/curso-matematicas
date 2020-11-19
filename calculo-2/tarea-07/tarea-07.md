# Tarea 7

**Rigoberto Canseco López**

## 1. $\int \frac 1 {\sqrt x(1+\sqrt[4]x)^2} \ dx$

Sustituimos $u=\sqrt[4]{x}$ y $du=\frac 1 {4x^{3/4}} \ dx$ 
$$
= 4\int \frac u {(u+1)^2} \ du
$$
Para el integrando $\frac{u}{(u+1)^2}$, se usa fracciones parciales
$$
= 4 \int\left(\frac 1 {u+1}-\frac1{(u+1)^2}\right) \ du
$$
Se integra término por término 
$$
= 4\int\frac 1 {u+1} \ du - 4 \int \frac 1 {(u+1)^2} \ du
$$
Para el integrando $\frac 1 {u+1}$, sustituimos $s=u+1$ y $ds=du$
$$
=4\int \frac 1 s \ ds - 4 \int \frac 1{(u+1)^2} \ du
$$
La integral de $1/s$ es $\ln s$
$$
4\ln s - 4\int \frac 1 {(u+1)^2} \ du
$$
Para el integrando $\frac 1 {(u+1)^2}$. sustituimos $v=u+1$ y $dv=du$
$$
= 4 \ln s - 4\int \frac 1 {v^2} \ dv 
$$
La integral de $1/v^2$ es $-1/v$
$$
= 4 \ln s + \frac 4 v + C 
$$
Sustituimos de regreso para $v = u+1$
$$
=4\left(\ln s + \frac 1 {u+1}\right) + C
$$
Sustituimos de regreso para $s=u+1$
$$
4\left( \ln (u+1) + \frac{1}{u+1} \right) +C
$$
Sustituimos de regreso $u=\sqrt[4] x$. 

Tenemos que la integral es 
$$
= 4 \left( \ln(\sqrt [4]x+1)+ \frac 1 {\sqrt[4] x+1}  \right) + C \quad \blacksquare
$$

## 2. $\int \frac 1 {4\sin x-7\cos x} \ dx$

Para $\frac 1 {4\sin x-7\cos x} $, sustituimos $u= \tan \frac x 2$ y $du=\frac 1 2 \ dx \sec^2\frac x 2 $. Transformamos la integral usando la sustitución $\sin x = \frac {2u}{u^2+1}$, $\cos x=\frac{1-u^2}{u^2+1}$ y $dx=\frac{2 \ du}{u^2+1}$
$$
= \int \frac 2 {(u^2+1)\left(\frac{8u}{u^2+1}-\frac{7(1-u^2)}{u^2+1}\right)} \ du \\
= \int \frac{2}{7u^2+8u-7}\ du \\
= 2\int \frac{1}{7u^2+8u-7}\ du
$$
Completando el cuadrado de $7 u^2+8 u-7$ tenemos 
$$
= 2 \int \frac{1}{\left(\sqrt{7} u+\frac{4}{\sqrt{7}}\right)^2-\frac{65}{7}} \, du
$$
Para la integral sustituimos $s=\sqrt 7 u+\frac 4 {\sqrt 7}$ y $ds = \sqrt 7 \ du$
$$
= \frac{2 }{\sqrt{7}}\int \frac{1}{s^2-\frac{65}{7}} \, ds \\
= \frac{2 }{\sqrt{7}}\int -\frac{7}{65 \left(1-\frac{7 s^2}{65}\right)} \, ds \\
=-\frac{2 \sqrt{7}}{65} \int \frac{1}{1-\frac{7 s^2}{65}} \, ds
$$
Para $\frac{1}{1-\frac{7 s^2}{65}}$, sustituimos $v=\sqrt{\frac{7}{65}}s$  y $dv=\sqrt{\frac{7}{65}} \ ds$
$$
= -\frac{2}{65} \int \frac{1}{1-v^2} \, dv
$$
La integral de $\frac{1}{1-v^2}$ es $\tanh^{-1} v$
$$
= - \frac{2  \tanh^{-1} v}{\sqrt{65} } + C
$$
Sustituimos de regreso para $v=\sqrt{\frac{7}{65}}s$
$$
= - \frac{2  \tanh^{-1} \left(\sqrt{\frac{7}{65}}s\right)}{\sqrt{65} } + C
$$
Sustituimos de regreso para $s=\sqrt{7} u+\frac{4}{\sqrt{7}}$
$$
= - \frac{2  \tanh^{-1} \left({\frac{7u+4}{\sqrt65}}\right)}{\sqrt{65} } + C
$$
Sustituimos de regreso para $u = \tan \frac x 2$.

Tenemos que la integral buscada es
$$
= - \frac{2  \tanh^{-1} \left({\frac{7\tan \frac x 2+4}{\sqrt65}}\right)}{\sqrt{65} } + C \quad \blacksquare
$$


## 3. $\int \frac 1 {4-5\cos x} \ dx$

Para $\frac{1}{4-5 \cos x}$, sustituimos $u = \tan \frac x 2$ y $du = \frac 1 2 \ dx \sec^2 \frac x 2$  . Transformamos la integral usando la sustitución: $\sin x = \frac {2u}{u^2+1}$, $\cos x = \frac {1-u^2}{u^2+1}$ y $dx=\frac {2\ du}{u^2+1}$
$$
= \int \frac{2}{\left(u^2+1\right) \left(4-\frac{5 \left(1-u^2\right)}{u^2+1}\right)} \ du
$$
Simplificamos 
$$
\text{= }\int \frac{2}{9 u^2-1} \, du \\
\text{= }2 \int \frac{1}{9 u^2-1} \, du \\
= -2 \int \frac{1}{1-9 u^2} \, du
$$
La la integral, sustituimos $s=3u$ y $ds=3\ du$ 
$$
=-\frac{2}{3}\int \frac{1}{1-s^2} \ ds
$$
La integral de $\frac 1 {1-s^2}$ es $\tanh^{-1}s$
$$
= - \frac 2 3 \tanh^{-1} s + C
$$
Sustituimos de regreso para $s=3u$ 
$$
=-\frac 2 3 \tanh ^{-1} (3u) + C
$$
Sustituimos de regreso para $u=\tan \frac x 2$
$$
= - \frac 2 3 \tanh^{-1}(3\tan \frac x 2)+ C
$$
La integral buscada es 
$$
= - \frac 2 3 \tanh^{-1}(3\tan \frac x 2)+ C \quad \blacksquare
$$
$\sqrt{-1} \ 2^3 \sum \pi$ 

**Calcular las siguientes integrales usando el método de Euler**.

## 4. $\int \frac{3x-6}{\sqrt{x^2-4x+5}} \ dx$

## 5. $\int \frac{x}{\sqrt{2x-x^2}} \ dx$

## 6. $\int\frac{1}{\sqrt{3+3x-x^2}} \ dx$