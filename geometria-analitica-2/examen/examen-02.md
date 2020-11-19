# Geometría Analítica II

**Examen parcial 2**

**Rigoberto Canseco López**

## 1. Considere $\mathscr{G}:3x^2-z^2=9$. Analice las siete simetrías vistas en clase. En caso de que se cumpla alguna, demuéstrela, de lo contrario exhiba un contraejemplo.

Probamos con el punto $P(2,0,\sqrt3)$ sustituimos en $\mathscr{G}:3x^2-z^2=9$ y vemos que cumple la igualdad $3(2)^2-(\sqrt3)^2=9$

* **Origen:** Sea el punto $P'(-2,0,-\sqrt3)$
  $$
  \begin{split}
  3x^2-z^2=9 \\
  3(-2)^2-(-\sqrt3)^2=9 \\
  12-3=9 \quad \bf\text{Cumple} \\
  \end{split}
  $$

* **Eje $X$:** Sea el punto $P'(2,0,-\sqrt3)$
  $$
  \begin{split}
  3x^2-z^2=9 \\
  3(2)^2-(-\sqrt3)^2=9 \\
  12-3=9 \quad \bf\text{Cumple}
  \end{split}
  $$

* **Eje $Y$:** Sea el punto $P'(-2,0,\sqrt3)$
  $$
  \begin{split}
  3x^2-z^2=9 \\
  3(-2)^2-(\sqrt3)^2=9 \\
  12-3=9 \quad \bf\text{Cumple} \\
  \end{split}
  $$

* **Eje $Z$:** Sea el punto $P'(-2,0,\sqrt3)$
  $$
  \begin{split}
  3x^2-z^2=9 \\
  3(-2)^2-(\sqrt3)^2=9 \\
  12-3=9 \quad \bf\text{Cumple} \\
  \end{split}
  $$

* **Plano $\pi_{xy}$:** Sea el punto $P'(2,0,-\sqrt3)$
  $$
  \begin{split}
  3x^2-z^2=9 \\
  3(2)^2-(-\sqrt3)^2=9 \\
  12-3=9 \quad \bf\text{Cumple} \\
  \end{split}
  $$

* **Plano $\pi_{yz}$:** Sea el punto $P'(-2,0,\sqrt3)$
  $$
  \begin{split}
  3x^2-z^2=9 \\
  3(-2)^2-(\sqrt3)^2=9 \\
  12-3=9 \quad \bf\text{Cumple} \\
  \end{split}
  $$

* **Plano $\pi_{xz}$:** Sea el punto $P'(2,0,\sqrt3)$
  $$
  \begin{split}
  3x^2-z^2=9 \\
  3(2)^2-(\sqrt3)^2=9 \\
  12-3=9 \quad \bf\text{Cumple} \\
  \end{split}
  $$


Por lo tanto $\mathscr{G}:3x^2-z^2=9$ cumple con las 7 simetrías $\quad \blacksquare$

## 2. Demuestre que el paraboloide hiperbólico $(\mathscr{G}:x^2-y^2=z)$ es una superficie doblemente reglada.

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



## 3. Considere el paraboloide hiperbólico $\mathscr{G}:9x^2-16y^2=z$ suponga que las rectas $l$ y $m$ que pasan por el punto $P=(1,0,9)$, donde $l:(1,0,9)+\alpha(4,-3,72)$ y $m:(1,0,9)+\beta(4,3,72)$ cumple que:

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

### a) $P \in l \subseteq \mathscr{G}$

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
= (1,0,9)+\alpha \lang4,-3,72\rang \\
\ell_k = l \quad \blacksquare
$$
Por lo tanto queda demostrado que $$P \in l \subseteq \mathscr{G}$$

### b) $P \in m \subseteq \mathscr{G}$

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
\ell_h =(1,0,9)+\beta \lang 4,3,72\rang \\
\ell_h = m\quad \blacksquare
$$
Por lo tanto queda demostrado que $P \in m \subseteq \mathscr{G}$

### c) Obtenga la ecuación del plano tangente en $P$ mediante la definición.

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