---
[Gráfica en Geogebra](https://www.geogebra.org/3d/fn8fhstv)title: Test
author: Author Name
header-includes: |
    \usepackage{fancyhdr}
	\usepackage{mathrsfs}
    \pagestyle{fancy}
    \fancyhead[CO,CE]{This is fancy}
    \fancyfoot[CO,CE]{So is this}
    \fancyfoot[LE,RO]{\thepage}
abstract: This is a pandoc test . . .
---

# Lista de ejercicios para el segundo parcial

**Rigoberto Canseco López**

## 1.

**Menciona tres cosas con ejemplos en los que se utilicen las superficies cuádricas y simetrías. Además de lo visto en clase.**



***

## 2.

**Para cada uno de los siguientes lugares geométricos analice las siete simetrías vistas en clase. En caso de que se cumpla alguna, demuéstrela, de lo contrario exhiba un contra ejemplo:**

**a) $\mathscr{G}: 2x+3y+z=0$**

Probamos con el punto $P(1,1,-5)$ , vemos que cumple la igualdad $2(1)+3(1)+(-5)=0$

* **Origen:** Sea el punto $P'(-1,-1,5)$
  $$
  \begin{split}
  2x+3y+z&=0 \\
  2(-1)+3(-1)+(5)&=0 \quad \bf\text{Cumple} \\
  \end{split}
  $$

* **Eje $X$:** Sea el punto $P'(1,-1,5)$
  $$
  \begin{split}
  2x+3y+z&=0 \\
  2(1)+3(-1)+(5)&=4 \quad \bf\text{No cumple} \\
  \end{split}
  $$

* **Eje $Y$:** Sea el punto $P'(-1,1,5)$
  $$
  \begin{split}
  2x+3y+z&=0 \\
  2(-1)+3(1)+(5)&=6 \quad \bf\text{No cumple} \\
  \end{split}
  $$

* **Eje $Z$:** Sea el punto $P'(-1,-1,5)$
  $$
  \begin{split}
  2x+3y+z&=0 \\
  2(-1)+3(-1)+(-5)&=-10 \quad \bf\text{No cumple} \\
  \end{split}
  $$

* **Plano $\pi_{xy}$:** Sea el punto $P'(1,1,5)$
  $$
  \begin{split}
  2x+3y+z&=0 \\
  2(1)+3(1)+(5)&=10 \quad \bf\text{No cumple} \\
  \end{split}
  $$

* **Plano $\pi_{yz}$:** Sea el punto $P'(-1,1,-5)$
  $$
  \begin{split}
  2x+3y+z&=0 \\
  2(-1)+3(1)+(-5)&=-4 \quad \bf\text{No cumple} \\
  \end{split}
  $$

* **Plano $\pi_{xz}$:** Sea el punto $P'(1,-1,-5)$
  $$
  \begin{split}
  2x+3y+z&=0 \\
  2(1)+3(-1)+(-5)&=-6 \quad \bf\text{No cumple} \\
  \end{split}
  $$

* 

***

**b) $\mathscr{G}: 3x^2-z^2=9$** 

**c) $\mathscr{G}: x^2+2y^2-3z^2=16$**

**d) $\mathscr{G}: x+y-z^2=1$**

**e) $\mathscr{G}: x^3-y/2-z^2=3$**

***

## 3.

**Pruebe que si $\ell : x − 1 = y − 2 = z + 1 \ \text y \ \mathscr{G} : z^2 − xy + 2x + y + 2z − 1 = 0$ entonces $ \ell \subseteq \mathscr{G}$ .**

*Solución*

Sea $\ell : x − 1 = y − 2 = z + 1$ y $\mathscr{G} : z^2 − xy + 2x + y + 2z − 1 = 0$
$$
\begin{split}
\text{Factorizando}\\
z^2 − xy + 2x + y + 2z − 1 &= 0 \\
z^2+2z+1+2x+y-xy -2 &=0 \\
(z+1)(z+1)+(x-1)(-y+2) &= 0\\
\mathscr{G}:(z+1)^2+(x-1)(2-y) &= 0\\
\end{split}
$$
Vemos que los puntos $P_1,P_2$ se encuentran en $\ell, \mathscr{G}$:

* $P_1(1,2,-1) \in \ell$ 

$$
 x − 1 = y − 2 = z + 1 \\
 (1)-1=(2)-2=(-1)+1\\
 0=0=0
$$

* $P_1(1,2,-1) \in \mathscr{G}$

$$
(z+1)^2+(x-1)(2-y) = 0\\
((-1)+1)^2+((1)-1)(2-(2))=0\\
0^2+(0)(0)=0
$$



* $P_2(-1,0,-3)\in \ell$ 

$$
x − 1 = y − 2 = z + 1 \\
 (-1)-1=(0)-2=(-3)+1\\
 -2=-2=-2
$$

* $P_2(-1,0,-3) \in \mathscr{G}$

$$
(z+1)^2+(x-1)(2-y) = 0\\
((-3)+1)^2+((-1)-1)(2-(0))=0\\
-2^2+(-2)(2)=0\\
4-4=0
$$

Ahora demostramos que $ \ell \subseteq \mathscr{G}$ 

Vemos que $\ell$ se en encuentra en el plano $\pi_{xz}$ 
$$
\begin{split}
y-2=x-1\\
y = x+1
\end{split}
$$
Sustituimos $y$ en $\mathscr{G}$
$$
\mathscr{G}:(z+1)^2+(x-1)(2-y) = 0\\
(z+1)^2+(x-1)(2-(x+1))=0\\
(z+1)^2+(x-1)(2-x-1)=0\\
\pi_{xz}:(z+1)^2+(x-1)(-x+1)=0
$$
Probamos que los puntos se encuentren en el plano

* $P_1(1,2,-1) \in \pi_{xy}$
  $$
  (z+1)^2+(x-1)(-x+1)=0\\
  ((-1)+1)^2+((1)-1)(-(1)+1)=0\\
  0^2+(0)(0)=0
  $$

* $P_2(-1,0,-3) \in \pi_{xy}$
  $$
  (z+1)^2+(x-1)(-x+1)=0\\
  ((-3)+1)^2+((-1)-1)(-(-1)+1)=0\\
  -2^2+(-2)(2)=0\\
  4-4=0
  $$

Por lo tanto se cumple que $\ell \sube \mathscr{G} \quad \blacksquare$ 

[Gráfica en Geogebra](https://www.geogebra.org/3d/emztqxer)

![](/home/rigoberto/Descargas/tarea02-03.png)



## 4.

**Considere a $\mathscr{G}$ como el hiperboloide de un manto ($\frac{x^2}{a^2}+ \frac{y^2}{b^2}-\frac{z^2}{c^2}=1$ donde $a,b,c$ son números reales positivos). Denote como $\ell ^*$ a la recta que pasa por $ae_1$ y tiene dirección $(0,b,c)$ y por $m^*$ a la recta que pasa por $-ae_1$ y tiene dirección $(0,-b,c)$. Pruebe que los enunciados siguientes son ciertos.**

**a) $\ell^* \neq m^*$**

Para la recta $\ell^*$ tenemos que pasa por el punto $ae_1(a,b,c)$ y tiene como dirección $\lang 0,b,c\rang$, por lo tanto la recta es
$$
\ell^*=a_{e1}+\lambda\lang 0,b,c\rang= (a,b,c)+\lambda\lang 0,b,c\rang \\
\text{ecuación simétrica }\\\frac{y-b}{b}=\frac{z-c}{c}
$$
Para la recta $m^*$ tenemos que pasa por el punto $ae_1(-a,b,c)$ y tiene como dirección $\lang 0,-b,c\rang$, por lo tanto la recta es
$$
m^*=-a_{e1}+\lambda\lang 0,b,c\rang= (-a,b,c)+\lambda\lang 0,-b,c\rang \\
\text{ecuación simétrica }\\-\frac{y-b}{b}=\frac{z-c}{c}
$$
Por lo tanto $\ell^*, m^*$ son diferentes

**b) $\ell^*\subseteq \mathscr{G}^*$**

Vemos que los puntos $P_1,P_2$ se encuentran en $\ell, \mathscr{G}$:

* $P_1(a,b,c) \in \ell$ 

$$
\frac{y-b}{b}=\frac{z-c}{c}\\
\frac{b-b}{b}=\frac{c-c}{c}\\
0=0
$$

* $P_1(a,b,c) \in \mathscr{G}$

$$
\frac{x^2}{a^2}+ \frac{y^2}{b^2}-\frac{z^2}{c^2}=1\\
\frac{a^2}{a^2}+ \frac{b^2}{b^2}-\frac{c^2}{c^2}=1\\
1+\cancel{1-1}=1
$$

* $P_2(a,-b,-c) \in \ell$ 

$$
\frac{y-b}{b}=\frac{z-c}{c}\\
\frac{-b-b}{b}=\frac{-c-c}{c}\\
\frac{-2\cancel b}{ \cancel b}=\frac{-2 \cancel c}{\cancel c}\\
$$

* $P_1(a,-b,-c) \in \mathscr{G}$

$$
\frac{x^2}{a^2}+ \frac{y^2}{b^2}-\frac{z^2}{c^2}=1\\
\frac{a^2}{a^2}+ \frac{(-b)^2}{b^2}-\frac{(-c)^2}{c^2}=1\\
1+\cancel{1-1}=1
$$

Ahora demostramos que $ \ell \subseteq \mathscr{G}$ 

Vemos que $\ell$ se en encuentra en el plano $\pi_{yz}$ 
$$
\frac{y-b}{b}=\frac{z-c}{c} \\
y=b\big(\frac{z-c}{c}+1\big)
$$
Sustituimos $y$ en $\mathscr{G}$
$$
\mathscr{G}:\frac{x^2}{a^2}+ \frac{y^2}{b^2}-\frac{z^2}{c^2}=1\\
\frac{x^2}{a^2}+ \frac{(b\big(\frac{z-c}{c}+1\big))^2}{b^2}-\frac{z^2}{c^2}=1\\
\frac{x^2}{a^2}+ \frac{\cancel {b^2}\big(\frac{z-c}{c}+1\big)^2}{\cancel {b^2}}-\frac{z^2}{c^2}=1\\
\frac{x^2}{a^2}+ \big(\frac{z-c}{c}+1\big)^2-\frac{z^2}{c^2}=1\\
\pi_{yz}:\frac{x^2}{a^2}+ \big(\frac{z-c}{c}+1\big)^2-\frac{z^2}{c^2}=1
$$
Probamos que los puntos se encuentren en el plano

* $P_1(a,b,c) \in \pi_{yz}$
  $$
  \frac{x^2}{a^2}+ \big(\frac{z-c}{c}+1\big)^2-\frac{z^2}{c^2}=1\\
  \frac{a^2}{a^2}+ \big(\frac{c-c}{c}+1\big)^2-\frac{c^2}{c^2}=1\\
  1+(0+1)^2-1=1\\
  1=1
  $$

* $P_2(a,-b,-c) \in \pi_{yz}$
  $$
  \frac{x^2}{a^2}+ \big(\frac{z-c}{c}+1\big)^2-\frac{z^2}{c^2}=1\\
  \frac{a^2}{a^2}+ \big(\frac{-c-c}{c}+1\big)^2-\frac{(-c)^2}{c^2}=1\\
  1+ \big(\frac{-2c}{c}+1\big)^2-1=1\\
  1+ (-1)^2-1=1\\
  1=1
  $$

Por lo tanto se cumple que $\ell \sube \mathscr{G}$

**c) $m^* \subseteq \mathscr{G}^*$**

Vemos que los puntos $P_1,P_2$ se encuentran en $m^*, \mathscr{G}$:

* $P_1(-a,b,-c) \in \ell$ 

$$
\frac{-y-b}{b}=\frac{z-c}{c}\\
\frac{-b-b}{b}=\frac{-c-c}{c}\\
\frac{-2\cancel b}{\cancel b}=\frac{-2\cancel c}{\cancel c}\\
-2=-2
$$

* $P_1(-a,b,-c) \in \mathscr{G}$

$$
\frac{x^2}{a^2}+ \frac{y^2}{b^2}-\frac{z^2}{c^2}=1\\
\frac{(-a)^2}{a^2}+ \frac{b^2}{b^2}-\frac{(-c)^2}{c^2}=1\\
1+\cancel{1-1}=1
$$

* $P_2(-a,-b,c) \in \ell$ 

$$
\frac{-y-b}{b}=\frac{z-c}{c}\\
\frac{-(-b)-b}{b}=\frac{c-c}{c}\\
0=0
$$

* $P_1(-a,-b,c) \in \mathscr{G}$

$$
\frac{x^2}{a^2}+ \frac{y^2}{b^2}-\frac{z^2}{c^2}=1\\
\frac{(-a)^2}{a^2}+ \frac{(-b)^2}{b^2}-\frac{(-c)^2}{c^2}=1\\
1+\cancel{1-1}=1
$$

Ahora demostramos que $ \ell \subseteq \mathscr{G}$ 

Vemos que $\ell$ se en encuentra en el plano $\pi_{yz}$ 
$$
\frac{-y-b}{b}=\frac{z-c}{c} \\
y=-b\big(\frac{z-c}{c}+1\big)
$$
Sustituimos $y$ en $\mathscr{G}$
$$
\mathscr{G}:\frac{x^2}{a^2}+ \frac{y^2}{b^2}-\frac{z^2}{c^2}=1\\
\frac{x^2}{a^2}+ \frac{(-b\big(\frac{z-c}{c}+1\big))^2}{b^2}-\frac{z^2}{c^2}=1\\
\frac{x^2}{a^2}+ \frac{\cancel {b^2}\big(\frac{z-c}{c}+1\big)^2}{\cancel {b^2}}-\frac{z^2}{c^2}=1\\
\frac{x^2}{a^2}+ \big(\frac{z-c}{c}+1\big)^2-\frac{z^2}{c^2}=1\\
\pi_{yz}:\frac{x^2}{a^2}+ \big(\frac{z-c}{c}+1\big)^2-\frac{z^2}{c^2}=1
$$
Probamos que los puntos se encuentren en el plano

* $P_1(-a,b,c) \in \pi_{yz}$
  $$
  \frac{x^2}{a^2}+ \big(\frac{z-c}{c}+1\big)^2-\frac{z^2}{c^2}=1\\
  \frac{(-a)^2}{a^2}+ \big(\frac{c-c}{c}+1\big)^2-\frac{c^2}{c^2}=1\\
  1+(0+1)^2-1=1\\
  1=1
  $$

* $P_2(-a,-b,-c) \in \pi_{yz}$
  $$
  \frac{x^2}{a^2}+ \big(\frac{z-c}{c}+1\big)^2-\frac{z^2}{c^2}=1\\
  \frac{(-a)^2}{a^2}+ \big(\frac{(-c)-c}{c}+1\big)^2-\frac{(-c)^2}{c^2}=1\\
  1+ \big(\frac{-2c}{c}+1\big)^2-1=1\\
  1+ -1^2-1=1\\
  1=1
  $$

Por lo tanto se cumple que $\ell \sube \mathscr{G}$

[Gráfica en Geogebra](https://www.geogebra.org/3d/p4pyz3tm)

![](/home/rigoberto/Descargas/tarea02-04.png)



## 5.

**Considere el *paraboloide hiperbólico* $(\mathscr{G}:\frac{x^2}{a^2}-\frac{y^2}{b^2}=cz)$. Demuestre que hay una recta $\ell_* \subseteq \mathscr{G}$ tomando en cuenta los siguientes planos:**
$$
\pi^0_h:=\frac{x}{a}-\frac{y}{b}=h \quad \pi^1_h:=h\Big(\frac{x}{a} + \frac{y}{b} \Big) = cz
$$
Es decir:

**i) Prueba que $\forall h\in \R, \ell_k \subseteq \mathscr{G}$ **

El vector normal de $\pi_h^0$ es $u=\lang 1/a ,-1/b,0\rang$ y el vector normal de $\pi_h^1$ es $v=\lang h/a, h/b, -c \rang$ además podemos ver que no son paralelos, por lo tanto la $\pi_h^0 \cap \pi_h^1$ es una linea recta $\ell_k$ que depende de $h$

Donde $h \in \R$, existen dos casos para $h\Big(\frac{x}{a}-\frac{y}{b}\Big)\Big(\frac{x}{a} + \frac{y}{b} \Big)
=hcz$

Si $h = 0$ tenemos que
$$
0\Big(\frac{x}{a}-\frac{y}{b}\Big)\Big(\frac{x}{a} + \frac{y}{b} \Big)
=0cz \quad \text{Por lo tanto se cumple la igualdad}
$$
Si $h\neq 0$ podemos multiplicar los planos para  demostrar que $\ell_k \subseteq \pi_h^0$ y $\ell_k \subseteq \pi_h^1$
$$
\begin{split}
(\pi_h^0)(\pi_h^1) &= h\Big(\frac{x}{a}-\frac{y}{b}\Big)\Big(\frac{x}{a} + \frac{y}{b} \Big)
=hcz\\
&=h\Big(\frac{x}{a}-\frac{y}{b}\Big)\Big(\frac{x}{a} + \frac{y}{b} \Big)= hcz \\
&=\cancel{(1/h)h}\Big(\frac{x}{a}-\frac{y}{b}\Big)\Big(\frac{x}{a} + \frac{y}{b} \Big)= \cancel{(1/h)h}cz \\

&=\frac{x^2}{a^2}-\frac{y^2}{b^2}= cz \\

\end{split}
$$
La última ecuación coincide con la ecuación de $\mathscr{G}$, por lo tanto $\ell_k$ queda contenida en $\mathscr{G}$.

**ii) Prueba que $\forall P \in \mathscr{G} \ \exist r \in \R $ tal que $P\in\ell_r \subseteq \mathscr{G}$**

Sea $P \in \mathscr{G} $ y el punto $P_0(x_0,y_0,z_0)$, además proponemos los planos $\pi_r^0, \pi_r^1$, sabemos por la afirmación anterior que  $\pi_r^0 \cap \pi_r^1$ es una linea recta $\ell_r$ nuestros planos son:
$$
\pi^0_r:=\frac{x_0}{a}-\frac{y_0}{b}=r \\ \pi^1_r:=r\Big(\frac{x_0}{a} + \frac{y_0}{b} \Big) = cz_0
$$
Donde $P \in \ell_r$ y también sabemos que $\ell_r \subseteq \mathscr{G}$ por el inciso anterior. Por lo tanto queda demostrado que  $\forall P \in \mathscr{G} \ \exist r \in \R $ tal que $P\in\ell_r \subseteq \mathscr{G}$.



## 6.

**Demuestre que el cono cuadrático ($\mathscr{K}:\frac{x^2}{a^2}+\frac{y^2}{b^2}-\frac{z^2}{c^2}=0$ donde $a,b,c$ son números reales positivos) es superficie reglada.**

Dado el cono cuadrático en posición canónica $\frac {x^2} {a^2} +\frac {y^2}{b^2}-\frac{z^2}{c^2}=0$, podemos factorizar como una diferencia de cuadrados
$$
\begin{split}
\frac {x^2} {a^2} -\frac{z^2}{c^2} &=- \frac {y^2}{b^2}\\
\Big(\frac {x} {a} -\frac{z}{c}\Big)\Big(\frac {x} {a} +\frac{z}{c}\Big) &=\Big(-1\Big) \big(\frac {y}{b}\Big)\Big(\frac {y}{b}\Big)
\end{split}
$$
  Multiplicamos el lado derecho de la igualdad por $1/k,k$, donde $k \neq 0$
$$
\Big(\frac {x} {a} -\frac{z}{c}\Big)\Big(\frac {x} {a} +\frac{z}{c}\Big) =\Big(-1\Big) \Big(\frac {y}{b}\Big)\Big(\frac {y}{b}\Big)\Big(\frac k k \Big)\\
\Big(\frac {x} {a} -\frac{z}{c}\Big)\Big(\frac {x} {a} +\frac{z}{c}\Big) =\Big(- \frac {ky}{b}\Big)\Big(\frac {y}{bk}\Big)
$$
Ahora se forma un sistema de ecuaciones
$$
L_{13}:\frac {x} {a} -\frac{z}{c} = -\frac {ky}{b} \quad 
L_{24}:\frac {x} {a} +\frac{z}{c} = \frac {y}{bk} \tag 1
$$

$$
L_{23}:\frac {x} {a} +\frac{z}{c} =- \frac {ky}{b}\quad 
L_{14}:\frac {x} {a} -\frac{z}{c}=\frac {y}{bk} \tag 2
$$

**Para las ecuaciones $(1)$**

Las ecuaciones son lineales, y por tanto corresponde a planos. La ecuación general del plano es $Ax+By+Cz+D=0$. 
El vector normal de $L_{13}$ es $u= \langle 1/a,k/b, -1/c \rangle$. El vector normal de $L_{24}$ es $v=\langle 1/a,-1/(kb), 1/k \rangle$.

Hacemos el producto cruz de los vectores $u= \langle 1/a,k/b, -1/c \rangle$ y $v=\langle 1/a,-1/(kb), 1/k \rangle$ para obtener el vector de dirección de la las rectas $L_{13}  \cap L_{24}$ 
Usando Wolfram.

![image-20201029234732713](/home/rigoberto/.config/Typora/typora-user-images/image-20201029234732713.png)
$$
= \langle -\frac{1}{bck} + \frac{k}{bc}, -\frac{2}{ac}, -\frac{1}{abk}-\frac{k}{ab} \rangle \tag 3
$$
Buscamos un punto que satisfaga la ecuaciones $L_{13}:\Big(\frac {x} {a} -\frac{z}{c}\Big) =\Big(- \frac {ky}{b}\Big) \quad 
L_{24}:\Big(\frac {x} {a} +\frac{z}{c}\Big) =\Big(\frac {y}{bk}\Big)$ 

Si $a,b,c$ los igualamos a $1$ tenemos 
$$
x-z=-yk \quad \text y \quad x+z=\frac y k \\
x=0 \\ y=z
$$
El punto que satisface ambas ecuaciones es $P(0,1,1)$, lo sustituimos en la ecuación $L_{13}$ para obtener el valor de $k$
$$
x+z=-yk \\
0+1=(1)k\\
k=1
$$
Sustituimos el valor de $k$ en $(3)$,  tenemos que vector de dirección es 
$$
= \langle -\frac{1}{bck} + \frac{k}{bc}, -\frac{2}{ac}, -\frac{1}{abk}-\frac{k}{ab} \rangle \\
= \langle -\frac{1}{bc(1)} + \frac{1}{bc}, -\frac{2}{ac}, -\frac{1}{ab(1)}-\frac{1}{ab} \rangle \\
=\langle  \cancel{-\frac{1}{bc} + \frac{1}{bc}}, -\frac{2}{ac},- \frac {2}{ac} \rangle \\
=\langle 0, -\frac{2}{ac},- \frac {2}{ac} \rangle
$$


Tenemos que la primer recta que contienen al punto $P(0,1,1)$ es 
$$
(x,y,z)= (0,1,-1)+ \lambda \langle 0, -\frac{2}{ac},- \frac {2}{ac} \rangle\tag {Primer recta }
$$
Por lo tanto todos los puntos de esa recta también satisfacen la ecuación del cono cuadrático, es decir la recta está contenida en la superficie.

**Para las ecuaciones $(2)$**

Las ecuaciones son lineales, y por tanto corresponde a planos. La ecuación general del plano es $Ax+By+Cz+D=0$. 
El vector normal de $L_{23}$ es $u= \langle 1/a,k/b, 1/c \rangle$. El vector normal de $L_{14}$ es $v=\langle 1/a,-1/bk, -1/c \rangle$.

Hacemos el producto cruz de los vectores $u$ y $v$ para obtener el vector de dirección de la las rectas $L_{23}  \cap L_{14}$ 
Usando Wolfram

![image-20201030002032395](/home/rigoberto/.config/Typora/typora-user-images/image-20201030002032395.png)
$$
= \langle \frac{1}{bck} - \frac{k}{bc}, \frac{2}{ac}, -\frac{1}{abk}-\frac{k}{ab} \rangle \tag 4
$$
Tomamos el punto $P(0,1,-1)$ y lo sustituimos en la ecuación  $L_{23}:\frac {x} {a} +\frac{z}{c} =- \frac {ky}{b}$. para obtener el valor de $k$

Si $a,b,c$ los igualamos a $1$ tenemos 
$$
x+z=-ky \\
0-(-1)=-k(1)\\
1=-k\\
k = -1
$$
Sustituimos el valor de $k$ en $(4)$, tenemos que vector de dirección es 
$$
= \langle \frac{1}{bck} - \frac{k}{bc}, \frac{2}{ac}, -\frac{1}{abk}-\frac{k}{ab} \rangle \\
= \langle \frac{1}{bc(-1)} - \frac{-1}{bc}, \frac{2}{ac}, -\frac{1}{ab(-1)}-\frac{-1}{ab} \rangle \\
=\langle  \cancel{\frac{1}{bc} -\frac{1}{bc}}, \frac{2}{ac},\frac {2}{ac} \rangle \\
=\langle 0, \frac{2}{ac},- \frac {2}{ac} \rangle
$$
Tenemos que la segunda recta que contienen al punto $P(0,1,-1)$ es 
$$
(x,y,z)= (0,1,-1)+ \lambda\langle 0, \frac{2}{ac}, \frac {2}{ac} \rangle \tag {Segunda recta }
$$
Por lo tanto todos los puntos de esa recta también satisfacen la ecuación del cono, es decir la recta está contenida en la superficie. Ademas vemos que las rectas son las mismas solo tiene dirección opuesta. 

Por lo tanto se demuestra que el *paraboloide hiperbólico* $(\mathscr{G}:x^2-y^2=z)$ es una superficie  reglada $\quad \blacksquare$

[Gráfica en Geogebra](https://www.geogebra.org/3d/uqefburx)

![](/home/rigoberto/Descargas/tarea02-06.png)

## 7.

**Demuestre que el *paraboloide hiperbólico* $(\mathscr{G}:x^2-y^2=z)$ es una superficie doblemente reglada**

Dado el paraboloide hiperbólico en posición canónica $x^2-y^2=z$, podemos factorizar como una diferencia de cuadrados
$$
x^2-y^2=z \\
(x+y)(x-y)=z
$$
  Multiplicamos el lado derecho de la igualdad por $1/k,k$, donde $k \neq 0$
$$
(x+y)(x-y)=(kz)(\frac 1 k)
$$
Ahora se forma un sistema de ecuaciones
$$
L_{13}:x+y=kz \quad L_{24}:x-y= \frac 1 k \tag 1
$$

$$
L_{14}:x-y=kz \quad L_{23}: x+y=\frac 1 k  \tag 2
$$

**Para las ecuaciones $(1)$**

Las ecuaciones son lineales, y por tanto corresponde a planos. La ecuación general del plano es $Ax+By+Cz+D=0$. 
El vector normal de $L_{13}$ es $u= \langle 1,1, -k \rangle$. El vector normal de $L_{24}$ es $v=\langle1,-1, 0 \rangle$.

Hacemos el producto cruz de los vectores $u=\lang 1 ,1,-k\rang$ y $v=\lang 1, -1, 0 \rang$ para obtener el vector de dirección de la las rectas $L_{13}  \cap L_{24}$ 
Usando Wolfram.

![image-20201029220057332](/home/rigoberto/.config/Typora/typora-user-images/image-20201029220057332.png)
$$
= \langle -k, -k, -2 \rangle \tag 3
$$
Buscamos un punto que satisfaga la ecuación $L_{13}:x+y=kz$.
Tomamos el punto $P(0,1,-1)$ y lo sustituimos en la ecuación $L_{13}$ para obtener el valor de $k$
$$
x+y=kz \\
0+1=k(-1)\\
k=-1
$$
Sustituimos el valor de $k$ en $(3)$,  tenemos que vector de dirección es $\langle 1, 1, -2 \rangle$
Tenemos que la primer recta que contienen al punto $P(0,1,-1)$ es 
$$
(x,y,z)= (0,1,-1)+ \lambda \langle1,1,-2\rangle \tag {Primer recta }
$$
Por lo tanto todos los puntos de esa recta también satisfacen la ecuación del paraboloide hiperbólico, es decir la recta está contenida en la superficie.

**Para las ecuaciones $(2)$**

Las ecuaciones son lineales, y por tanto corresponde a planos. La ecuación general del plano es $Ax+By+Cz+D=0$. 
El vector normal de $L_{14}$ es $u= \langle 1,-1, -k \rangle$. El vector normal de $L_{23}$ es $v=\langle1,1, 0 \rangle$.

Hacemos el producto cruz de los vectores $u=\lang 1 ,-1,-k \rang$ y $v=\lang 1, 1, 0 \rang$ para obtener el vector de dirección de la las rectas $L_{14}  \cap L_{23}$ 
Usando Wolfram

![image-20201029223034771](/home/rigoberto/.config/Typora/typora-user-images/image-20201029223034771.png)
$$
= \langle k, -k, 2 \rangle \tag 4
$$

Tomamos el punto $P(0,1,-1)$ y lo sustituimos en la ecuación  $L_{14}:x-y=kz$. para obtener el valor de $k$
$$
x-y=kz \\
0-1=k(-1)\\
k=1
$$
Sustituimos el valor de $k$ en $(4)$, tenemos que vector de dirección es $\langle 1, -1, 2 \rangle$
Tenemos que la segunda recta que contienen al punto $P(0,1,-1)$ es 
$$
(x,y,z)= (0,1,-1)+ \lambda \langle1,-1,2\rangle \tag {Segunda recta }
$$
Por lo tanto todos los puntos de esa recta también satisfacen la ecuación del paraboloide hiperbólico, es decir la recta está contenida en la superficie.



Por lo tanto se demuestra que el *paraboloide hiperbólico* $(\mathscr{G}:x^2-y^2=z)$ es una superficie doblemente reglada $\quad \blacksquare$

[Gráfica en Geogebra](https://www.geogebra.org/3d/skkvxruh)

![https://www.geogebra.org/3d/skkvxruh](/home/rigoberto/Descargas/tarea02-07.png)

## 8.

**Considere el paraboloide hiperbólico $\mathscr{G}:9x^2-16y^2=z$ pruebe que las rectas $l$ y $m$ pasan por el punto $P=(0,1,-16)$, donde $l:(0,1,-16)+\alpha(4,-3,96)$ y $m:(0,1,-16)+\beta(4,3,-96)$ cumple que**

Sea el paraboloide hiperbólico $\mathscr{G}:9x^2-16y^2=z$ , la ecuación simétrica del paraboloide hiperbólico 
$$
\mathscr{G}:\frac{x^2}{a^2}-\frac{y^2}{b^2}=cz
$$
Separamos la ecuación en la forma de producto de la diferencia de cuadrados
$$
\Big(\frac{3x}{a}+\frac{4y}{b}\Big)k \Big(\frac{3x}{a}-\frac{4y}{b}\Big)=kcz\\
\pi_k^0:\frac{3x}{a}+\frac{4y}{b}=k \quad \ \quad \pi_k^1:k\Big(\frac{3x}{a}-\frac{4y}{b}\Big)=cz \\
\text{Sustituimos }k \text{ por } h \\
\pi_h^0:\frac{3x}{a}-\frac{4y}{b}=h \quad \ \quad \pi_h^1:h\Big(\frac{3x}{a}+\frac{4y}{b}\Big)=cz
$$
**Planos $\pi _k$**

Sean los planos
$$
\pi_k^0:\frac{3x}{a}+\frac{4y}{b}=k \quad \ \quad \pi_k^1:k\Big(\frac{3x}{a}-\frac{4y}{b}\Big)=cz
$$
El vector normal de $\pi_k^0$
$$
u_k=\lang3/a,4/b,0\rang
$$
El vector normal de $\pi_k^1$
$$
v_k=\lang 3k/a,-4k/b,-c\rang
$$
El producto cruz de ambos vectores, $u_k, v_k$ es, usando wolfram:

![image-20201030125438301](/home/rigoberto/.config/Typora/typora-user-images/image-20201030125438301.png)
$$
w_k=u_k \times v_k = \lang -4c/b,3c/a, -24k/ab\rang
$$
**Planos $\pi _h$**

Hacemos lo mismo que en el plano $\pi_k$ ahora formamos el otro ecuación y 
$$
\Big(\frac{3x}{a}+\frac{4y}{b}\Big)h \Big(\frac{3x}{a}-\frac{4y}{b}\Big)=hcz
$$
 

Sean los planos
$$
\pi_h^0:\frac{3x}{a}-\frac{4y}{b}=h \quad \ \quad \pi_h^1:h\Big(\frac{3x}{a}+\frac{4y}{b}\Big)=cz
$$
El vector normal de $\pi_h^0$
$$
u_h=\lang3/a,-4/b,0\rang
$$
El vector normal de $\pi_h^1$
$$
v_h=\lang 3h/a,4h/b,-c\rang
$$
El producto cruz de ambos vectores, $u_k, v_k$ es usando Wolfram:

![image-20201030125924850](/home/rigoberto/.config/Typora/typora-user-images/image-20201030125924850.png)
$$
w_h=u_h \times v_h = \lang 4c/b,3c/a, 24h/ab\rang
$$
Podemos ver que los vectores directores $w_k= \lang -4c/b,3c/a, -24k/ab\rang$ y $w_h = \lang 4c/b,3c/a, 24h/ab\rang$ no son paralelos

Sea el paraboloide hiperbólico $\mathscr{G}:9x^2-16y^2=z$ , la ecuación simétrica del paraboloide hiperbólico 
$$
\mathscr {G} :\frac{x^2}{a^2}-\frac{y^2}{b^2}=cz
$$
 Por lo tanto tenemos que 
$$
a=1, \quad b=1, \quad c=1
$$


**a) $P \in l \subseteq \mathscr{G}$**

Sustituimos los valores del punto $P(0, 1,-16)$ y $a,b$ en la siguiente ecuación para encontrar $k$
$$
\frac{3x}{a}+\frac{4y}{b}=k \\
\frac{3(0)}{1}+\frac{4(1)}{1}=k \\
4 =k
$$
Sustituimos el valor de $k$ y $a,b,c$ en la ecuación del vector director $w_k$ 
$$
w_k= \lang -4c/b,3c/a, -24k/ab\rang \\
w_k= \lang -4(1)/1,3(1)/1, -24(4)/(1*1)\rang \\
w_k= \lang -4,3, -96\rang = \lang 4,-3, 96\rang
$$
Podemos encontrar la ecuación de la recta que pasa por el punto $P$ y el vector director $w_k$
$$
\ell_k=P+\lambda w_k \\
\ell_k =(0,1,-16)+\alpha \lang-4,3,-96\rang
= (0,1,-16)+\alpha \lang4,-3,96\rang
$$
Por lo tanto queda demostrado que $$P \in l \subseteq \mathscr{G}$$

**b) $P \in m \subseteq \mathscr{G}$**

**c)Demuestre mediante la definición de plano tangente (No gradiente 1 , puesto que esta es una herramienta de cálculo en varias variables) que esté en el punto $P$ está dado por la ecuación cartesiana:**$32y+z-16=0$

## 9.

**Considere el paraboloide hiperbólico** $\mathscr{G}:9x^2-16y^2=z$ pruebe que las rectas $l$ y $m$ pasan por el punto $P=(1,0,9)$, donde $l:(1,0,9)+\alpha(4,-3,72)$ y $m:(1,0,9)+\beta(4,3,72)$ cumple que

Sea el paraboloide hiperbólico $\mathscr{G}:9x^2-16y^2=z$ , la ecuación simétrica del paraboloide hiperbólico 
$$
\mathscr{G}:\frac{x^2}{a^2}-\frac{y^2}{b^2}=cz
$$
Separamos la ecuación en la forma de producto de la diferencia de cuadrados
$$
\Big(\frac{3x}{a}+\frac{4y}{b}\Big)k \Big(\frac{3x}{a}-\frac{4y}{b}\Big)=kcz\\
\pi_k^0:\frac{3x}{a}+\frac{4y}{b}=k \quad \ \quad \pi_k^1:k\Big(\frac{3x}{a}-\frac{4y}{b}\Big)=cz \\
\text{Sustituimos }k \text{ por } h \\
\pi_h^0:\frac{3x}{a}-\frac{4y}{b}=h \quad \ \quad \pi_h^1:h\Big(\frac{3x}{a}+\frac{4y}{b}\Big)=cz
$$
**Planos $\pi _k$**

Sean los planos
$$
\pi_k^0:\frac{3x}{a}+\frac{4y}{b}=k \quad \ \quad \pi_k^1:k\Big(\frac{3x}{a}-\frac{4y}{b}\Big)=cz
$$
El vector normal de $\pi_k^0$
$$
u_k=\lang3/a,4/b,0\rang
$$
El vector normal de $\pi_k^1$
$$
v_k=\lang 3k/a,-4k/b,-c\rang
$$
El producto cruz de ambos vectores, $u_k, v_k$ es, usando wolfram:

![image-20201030125438301](/home/rigoberto/.config/Typora/typora-user-images/image-20201030125438301.png)
$$
w_k=u_k \times v_k = \lang -4c/b,3c/a, -24k/ab\rang
$$
**Planos $\pi _h$**

Hacemos lo mismo que en el plano $\pi_k$ ahora formamos el otro ecuación y 
$$
\Big(\frac{3x}{a}+\frac{4y}{b}\Big)h \Big(\frac{3x}{a}-\frac{4y}{b}\Big)=hcz
$$
 

Sean los planos
$$
\pi_h^0:\frac{3x}{a}-\frac{4y}{b}=h \quad \ \quad \pi_h^1:h\Big(\frac{3x}{a}+\frac{4y}{b}\Big)=cz
$$
El vector normal de $\pi_h^0$
$$
u_h=\lang3/a,-4/b,0\rang
$$
El vector normal de $\pi_h^1$
$$
v_h=\lang 3h/a,4h/b,-c\rang
$$
El producto cruz de ambos vectores, $u_k, v_k$ es usando Wolfram:

![image-20201030125924850](/home/rigoberto/.config/Typora/typora-user-images/image-20201030125924850.png)
$$
w_h=u_h \times v_h = \lang 4c/b,3c/a, 24h/ab\rang
$$
Podemos ver que los vectores directores $w_k= \lang -4c/b,3c/a, -24k/ab\rang$ y $w_h = \lang 4c/b,3c/a, 24h/ab\rang$ no son paralelos

Sea el paraboloide hiperbólico $\mathscr{G}:9x^2-16y^2=z$ , la ecuación simétrica del paraboloide hiperbólico 
$$
\mathscr {G} :\frac{x^2}{a^2}-\frac{y^2}{b^2}=cz
$$
 Por lo tanto tenemos que 
$$
a=1, \quad b=1, \quad c=1
$$


**a) $P \in l \subseteq \mathscr{G}$**

Sustituimos los valores del punto $P(1, 0,9)$ y $a,b$ en la siguiente ecuación para encontrar $k$
$$
\frac{3x}{a}+\frac{4y}{b}=k \\
\frac{3(1)}{1}+\frac{4(0)}{1}=k \\
3 =k
$$
Sustituimos el valor de $k$ y $a,b,c$ en la ecuación del vector director $w_k$ 
$$
w_k= \lang -4c/b,3c/a, -24k/ab\rang \\
w_k= \lang -4(1)/1,3(1)/1, -24(3)/(1*1)\rang \\
w_k= \lang -4,3, -72\rang
$$
Podemos encontrar la ecuación de la recta que pasa por el punto $P$ y el vector director $w_k$
$$
\ell_k=P+\lambda w_k \\
\ell_k =(1,0,9)+\alpha \lang-4,3,-72\rang
= (1,0,9)+\alpha \lang4,-3,72\rang
$$
Por lo tanto queda demostrado que $$P \in l \subseteq \mathscr{G}$$

**b) $P \in m \subseteq \mathscr{G}$**

Sustituimos los valores del punto $P(1,0,9)$ y $a,b$ en la siguiente ecuación para encontrar $h$
$$
\frac{3x}{a}-\frac{4y}{b}=h \\
\frac{3(1)}{1}-\frac{4(0)}{1}=h \\
3 =h
$$
Sustituimos el valor de $h$ y $a,b,c$ en la ecuación del vector director $w_h$ 
$$
w_h= \lang 4c/b, 3c/a, 24h/ab\rang \\
w_h= \lang 4(1)/1,3(1)/1, 24(3)/(1*1)\rang \\
w_h= \lang 4,3,72\rang
$$
Podemos encontrar la ecuación de la recta que pasa por el punto $P$ y el vector director $w_k$
$$
\ell_h=P+\beta w_h \\
\ell_h =(1,0,9)+\beta \lang 4,3,72\rang
$$
Por lo tanto queda demostrado que $P \in m \subseteq \mathscr{G}$

**c) Obtenga la ecuación del plano tangente en $P$**

Con el producto cruz entre sus vectores directores podemos encontrar el vector normal al plano tangente, los vectores directores $w_k,w_h$. Usando wolfram

![image-20201030132416314](/home/rigoberto/.config/Typora/typora-user-images/image-20201030132416314.png)
$$
w=w_k \times w_h = \lang -432,0, 24\rang
$$
Sustituimos el punto $P(1,0,9)$ y el vector del plano tangente en la ecuación del plano $Ax+By+Cz+D=0$ para encontrar a D
$$
Ax+By+Cz+D=0 \\
-432(1)+(0)(0)+(24)(9)+D =0 \\
-432(1)+(24)(9)+D = 0\\
D =216
$$
Por lo tanto tenemos que la ecuación del plano tangente es
$$
\pi:=-432x+24z+216=0 \quad \blacksquare
$$
[Gráfica en Geogebra](https://www.geogebra.org/3d/pkuznuxp)

![](/home/rigoberto/Descargas/tarea02-09.png)

## 10.

**Considera el paraboloide hiperbólico $\mathscr {P} :x²-\frac{y^2}{4}-5z=0$, obtenga la ecuación del plano tangente en el punto $P(\sqrt 6 , 2, 1)$**

Sea el paraboloide hiperbólico $\mathscr {P} :x²-\frac{y^2}{4}-5z=0$ , la ecuación simétrica del paraboloide hiperbólico 
$$
\mathscr {P} :\frac{x^2}{a^2}-\frac{y^2}{b^2}=cz
$$
Separamos la ecuación en la forma de producto de la diferencia de cuadrados
$$
\Big(\frac{x}{a}+\frac{y}{b}\Big)k \Big(\frac{x}{a}-\frac{y}{b}\Big)=kcz\\
\pi_k^0:\frac{x}{a}+\frac{y}{b}=k \quad \ \quad \pi_k^1:k\Big(\frac{x}{a}-\frac{y}{b}\Big)=cz \\
\text{Sustituimos }k \text{ por } h \\
\pi_h^0:\frac{x}{a}-\frac{y}{b}=h \quad \ \quad \pi_h^1:h\Big(\frac{x}{a}+\frac{y}{b}\Big)=cz
$$
**Planos $\pi _k$**

Sean los planos
$$
\pi_k^0:\frac{x}{a}+\frac{y}{b}=k \quad \ \quad \pi_k^1:k\Big(\frac{x}{a}-\frac{y}{b}\Big)=cz
$$
El vector normal de $\pi_k^0$
$$
u_k=\lang1/a,1/b,0\rang
$$
El vector normal de $\pi_k^1$
$$
v_k=\lang k/a,-k/b,-c\rang
$$
El producto cruz de ambos vectores, $u_k, v_k$ es

![image-20201030110151253](/home/rigoberto/.config/Typora/typora-user-images/image-20201030110151253.png)
$$
w_k=u_k \times v_k=\lang1/a,1/b,0\rang \times \lang k/a,-k/b,-c\rang = \lang -c/b,c/a, -2k/ab\rang
$$
**Planos $\pi _h$**

Hacemos lo mismo que en el plano $\pi_k$ ahora formamos el otro ecuación y 
$$
\Big(\frac{x}{a}+\frac{y}{b}\Big)h \Big(\frac{x}{a}-\frac{y}{b}\Big)=hcz
$$
 

Sean los planos
$$
\pi_h^0:\frac{x}{a}-\frac{y}{b}=h \quad \ \quad \pi_h^1:h\Big(\frac{x}{a}+\frac{y}{b}\Big)=cz
$$
El vector normal de $\pi_h^0$
$$
u_h=\lang1/a,-1/b,0\rang
$$
El vector normal de $\pi_h^1$
$$
v_h=\lang h/a,h/b,-c\rang
$$
El producto cruz de ambos vectores, $u_k, v_k$ es

![image-20201030112204717](/home/rigoberto/.config/Typora/typora-user-images/image-20201030112204717.png)
$$
w_h=u_h \times v_h=\lang1/a,-1/b,0\rang \times \lang h/a,h/b,-c\rang = \lang c/b,c/a, 2h/ab\rang
$$
Podemos ver que los vectores directores $w_k= \lang -c/b,c/a, -2k/ab\rang$ y $w_h = \lang c/b,c/a, 2h/ab\rang$ no son paralelos

**Plano tangente**

Sea el paraboloide hiperbólico $\mathscr {P} :x²-\frac{y^2}{4}-5z=0$ , la ecuación simétrica del paraboloide hiperbólico 
$$
\mathscr {P} :\frac{x^2}{a^2}-\frac{y^2}{b^2}=cz
$$
 Por lo tanto tenemos que 
$$
a=1, \quad b=2, \quad c=5
$$
*Para el plano $\pi_k$*

Sustituimos los valores del punto $P(\sqrt6, 2,1)$ y $a,b$ en la siguiente ecuación para encontrar $k$
$$
\frac{x}{a}+\frac{y}{b}=k \\
\frac{\sqrt6}{1}+\frac{2}{2}=k \\
\sqrt 6+1 =k
$$
Sustituimos el valor de $k$ y $a,b,c$ en la ecuación del vector director $w_k$ 
$$
w_k= \lang -c/b,c/a, -2k/ab\rang \\
w_k= \lang -5/2,5/1, -2(\sqrt6+1)/(1*2)\rang \\
w_k= \lang -5/2,5, -\sqrt6-1\rang
$$
Podemos encontrar la ecuación de la recta que pasa por el punto $P$ y el vector director $w_k$
$$
\ell_k=P+\lambda w_k \\
\ell_k =(\sqrt6,2,1)+\lambda \lang-5/2,5,-\sqrt6-1\rang
$$
 *Para el plano $\pi_h$*

Sustituimos los valores del punto $P(\sqrt6, 2,1)$ y $a,b$ en la siguiente ecuación para encontrar $h$
$$
\frac{x}{a}-\frac{y}{b}=h \\
\frac{\sqrt6}{1}-\frac{2}{2}=h \\
\sqrt 6-1 =h
$$
Sustituimos el valor de $h$ y $a,b,c$ en la ecuación del vector director $w_h$ 
$$
w_h= \lang c/b,c/a, 2h/ab\rang \\
w_h= \lang 5/2,5/1, 2(\sqrt6-1)/(1*2)\rang \\
w_h= \lang 5/2,5, \sqrt6-1\rang
$$
Podemos encontrar la ecuación de la recta que pasa por el punto $P$ y el vector director $w_k$
$$
\ell_h=P+\lambda w_h \\
\ell_h =(\sqrt6,2,1)+\lambda \lang 5/2,5, \sqrt6-1\rang
$$
Sabemos que $\ell_k \subseteq \mathscr {P}, \ell_h \subseteq \mathscr {P}, P \in \ell_k, P\in \ell_h$ 

Con el producto cruz entre sus vectores directores podemos encontrar el vector normal al plano tangente, los vectores directores $w_k,w_h$. Usando wolfram

![image-20201030114750160](/home/rigoberto/.config/Typora/typora-user-images/image-20201030114750160.png)
$$
w=w_k \times w_h= \lang -5/2,5, -\sqrt6-1\rang\times \lang 5/2,5, \sqrt6-1\rang
\\ = \lang 10\sqrt6,-5, -25\rang
$$
Sustituimos el punto $P$ y el vector del plano tangente en la ecuación del plano $Ax+By+Cz+D=0$ para encontrar a D
$$
Ax+By+Cz+D=0 \\
10\sqrt6(\sqrt6)+(-5)(2)+(-25)(1)+D =0 \\
10(6)-10-25+D = 0\\
D =-60+10+25=-25
$$
Por lo tanto tenemos que la ecuación del plano tangente es
$$
\pi:=10\sqrt6x-5y-25z-25=0 \quad \blacksquare
$$
[Gráfica en Geogebra](https://www.geogebra.org/3d/fn8fhstv)

![](/home/rigoberto/Descargas/tarea02-010.png)