# Geometría Analítica II | Lista de ejercicios

**Alumno: ** *Rigoberto Canseco López*

## 1. Escribe las *ecuaciones canónicas* de las cónicas indicando qué cumple cada una.

## 2. De todas las formas de ecuación de las siguiente rectas:

### a) Tiene  vector director $(3,3,1)$ y pasa por $(0,4,2)$

#### Usando la ecuación paramétrica $\ell :(x,y,z)=P+\lambda v$ ####

Donde: $P =(0,4,2) \quad \text y \quad v= (3,3,1)$
$$
\begin{split}
\ell :(x,y,z) &= P+\lambda v  \\
&= (x_0,y_0,z_0) + \lambda (v_1,v_2,v_3)\\
&= (0,4,2) + \lambda(3,3,1) \\
&= (0,4,2) + (\lambda3,\lambda3,\lambda1) \\
&=  (0+\lambda3,4+\lambda3,2+\lambda1) \\
\end{split}
$$

Por lo tanto tenemos que
$$
x=x_0 + \lambda v_1, \quad x-x_0=\lambda v_1, \quad \frac{x-x_0}{v_1}= \lambda \\
\frac{x - 0}{3} = \lambda \\
y=y_0 + \lambda v_2, \quad y-y_0=\lambda v_2, \quad \frac{y-y_0}{v_2}= \lambda \\
\frac{y - 4}{3} = \lambda \\
z=z_0 + \lambda v_3, \quad z-z_0=\lambda v_3, \quad \frac{z-z_0}{v_3}= \lambda \\
\frac{z - 2}{1} = \lambda \\
$$

#### La ecuación simétrica está dada por:

$$
\frac{x-x_0}{v_1}=\frac{y-y_0}{v_2}=\frac{z-z_0}{v_3}
$$
Sustituyendo los valores en la ecuación tenemos que:
$$
\frac{x-0}{3}=\frac{y-4}{3}=\frac{z-2}{1} \\
\frac{x}{3}=\frac{y-4}{3}=z-2
$$

---

### b) Pasa por $(1,-2,5)$ y por $(3,-3,4)$

#### La ecuación paramétrica es $\ell :(x,y,z)=P+\lambda v$

Calculamos el vector $v$ que es la diferencia de $P_1$ y $P_2$

Tenemos los siguientes puntos $P_1(1,-2,5)$ y $P_2(3,-3,4)$ 

El vector director es: 
$$
\begin{split}
v=&P_1-P_2 \\
=& (1,-2,-5) - (3,-3,4) \\
=& (1-3,-2+3,-5-4) \\
=& (-2,1,-9)
\end{split}
$$
Por lo tanto la ecuación paramétrica para el punto $P_1$ es:
$$
\begin{split}
\ell :(x,y,z) &= P+\lambda v  \\
&= (x_0,y_0,z_0) + \lambda (v_1,v_2,v_3)\\
&= (1,-2,5) + \lambda(-2,1,-9) \\
\end{split}
$$
Por lo tanto la ecuación paramétrica para el punto $P_2$ es:
$$
\begin{split}
\ell :(x,y,z) &= P+\lambda v  \\
&= (x_0,y_0,z_0) + \lambda (v_1,v_2,v_3)\\
&= (3,-3,4) + \lambda(-2,1,-9) \\
\end{split}
$$

#### La ecuación simétrica está dada por:

$$
\frac{x-x_1}{x_2-x1} = \frac{y-y_1}{y_2-y1} = \frac{z-z_1}{z_2-z1} \\
$$
Por lo tanto tenemos que:
$$
\frac{x-1}{3-1} = \frac{y-(-2)}{3-(-2)} = \frac{z-5}{4-5} \\
\frac{x-1}{3-1} = \frac{y+2}{3+2} = \frac{z-5}{4-5} \\
$$

---

### c) Tiene como vector director al vector normal de los vectores $(1,1,1)$ y $(-1,0,2)$ y que pasa por el punto $(4,2,1)$

## 3. Encuentra la ecuación del plano cuyo vector normal es el $(3,-1,5)$ y que contiene el punto $(2,-1,0)$

La ecuación del plano es $\pi :Ax+By+Cz+D =0$, donde nuestro vector normal es $v(A,B,C)=(3,-1,5)$ y nuestro punto $P(x_0,y_0,z_0)=(2,-1,0)$

Sustituyendo el punto $P$ en la ecuación del plano $Ax+By+Cz+D =0$
$$
Ax_0+By_0+Cz_0+D = 0 \\
Ax_0+By_0+Cz_0= -D
$$
Sustituyendo los valores de el $v$ y $P$ en la ecuación de arriba nos queda que:
$$
\begin{split}
&Ax_0+By_0+Cz_0= -D \\
&= (3)(2)+(-1)(-1)+(5)(0) = -D \\
&= 6+1+0= -D \\
&= 7 = -D \\
\end{split}
$$
Por lo tanto $D = -7$

Por último tenemos que la ecuación de plano es $Ax+By+Cz+D =0$, sustituimos los valores del vector normal $v$ y de $D$.
$$
Ax+By+Cz+D =0 \\
(3)x + (-1)y +(5)z + (-7) = 0 \\
3x -y+5z-7 =0
$$

## 4. Encuentra la ecuación del plano que pasa por los puntos $(3,4,1),(-1,-2,-5)$  y $(1,7,1)$

Tenemos tres puntos $P_1(3,4,1)$, $P_2(-1,-2,-5)$ y $P_3(1,7,1)$

Obtenemos la diferencia de dos puntos $P_1$ y $P_2$
$$
\begin{split}
P_1-P_2 &= (3,4,1)-(-1,-2,-5) \\
&= (3-(-1), 4-(-2), 1-(-5)) \\
&= (3+1, 4+2,1+5)\\
&= (4,6,6)
\end{split}
$$
Obtenemos la diferencia de dos puntos $P_2$ y $P_3$
$$
\begin{split}
P_2-P_3 &= (-1,-2,-5)-(1,7,1) \\
&= (-1-(1), -2-(7), -5-(1)) \\
&= (-1-1, -2-7,5-1)\\
&= (-2,-9,4)
\end{split}
$$
Obtenemos el vector normal del producto cruz de $(4,6,6)$ y $(-2,-9,4)$

![image-20201007191111298](/home/rigoberto/.config/Typora/typora-user-images/image-20201007191111298.png)

Por lo tanto el vector normal del plano es $(78,-28,-24)$

Sustituyendo los valores de el vector $v(78,-28,-24)$ y $P_1(3,4,1)$ en la ecuación $Ax_0+By_0+Cz_0= -D$  nos queda que:
$$
\begin{split}
&Ax_0+By_0+Cz_0= -D \\
&= (78)(3)+(-28)(4)+(-24)(1) = -D \\
&= 234+(-112)+(-24)= -D \\
&= -112 = -D \\
\end{split}
$$
Por lo tanto $D = 112$

Por último tenemos que la ecuación de plano es $Ax+By+Cz+D =0$, sustituimos los valores del vector normal $v$ y de $D$.
$$
Ax+By+Cz+D =0 \\
(78)x + (-28)y +(-24)z + (112) = 0 \\
78x - 28y + -24z +112 =0
$$

## 5. Sea $P = (x,y,z)$ demuestre lo siguiente

### a) $P$ y $-P$ son simétricos respecto al origen

---

### b) $P$ y $(-x,y,-z)$ son simétricos respecto al eje $Y$

---

### c) $P$ y $(x,-y,-z)$ son simétricos respecto al eje $X$

---

### d) $P$ y $(−x, y, z)$ son simétricos respecto al plano $π_{YZ}$.

---

### e) $P$ y $(x, −y, z)$ son simétricos respecto al plano $π_{XZ}$.

## 6. Para cada uno de los siguientes lugares geométricos analice las siete simetrías vistas en clase. En caso de que se cumpla alguna, demuéstrela, de lo contrario exhiba un contra ejemplo:

### a) $\mathscr{G}:2x+3y+z=0$ 

---

### b) $\mathscr{G}:3x²-z²=9$ 

---

### c) $\mathscr{G}:x²+2y²-3z²=16$ 

---

### d) $\mathscr{G}:x+y-z²=1$ 

---

### e) $\mathscr{G}:x³-y/2-z²=3$ 


## 7. Suponga $C, S ∈ \R^3$ . Pruebe que si $(C − S)⊥ e_1$ , entonces $C$ y $S$ tienen la misma primer coordenada.

***Demostración:***

Sean que $C=(x_0, y_0, z_0)$ y $S(x_1,y_1,z_1)$ entonces tenemos que $C,S \in \R^3$ y $(C-S)\bot e_1 $ 

Donde $e_1 =(1,0,0)$
$$
\begin{split}
&(C-S)\bot e_1 = ((x_0,y_0,z_0)- (x_1,y_1, z_1)) \bot e_1 \\ \\
&\Rightarrow (x_0-x_1, y_0-y_1,z_0-z_1) \bot e_1 \\
&= (x_0-x_1,y_0-y_1,z_0-z_1) \cdot (1,0,0) \\ 
&= (x_0-x_1)(1) + (y_0-y_1)(0) +(z_0-z_1)(0) = 0 \\
&=(x_0-x_1) + 0 + 0 = 0 \\
&=x_0-x_1=0
\end{split}
$$
Nos queda que $x_0 = x_1$ 

Por lo tanto tienen la misma primer coordenada.


## 8. Suponga $C, S ∈ \R^3$ . Pruebe que si $(C − S)⊥ e_2$ , entonces $C$ y $S$ tienen la misma segunda coordenada.

***Demostración:***

Sean que $C=(x_0, y_0, z_0)$ y $S(x_1,y_1,z_1)$ entonces tenemos que $C,S \in \R^3$ y $(C-S)\bot e_2 $ 

Donde $e_1 =(1,0,0)$
$$
\begin{split}
&(C-S)\bot e_2 = ((x_0,y_0,z_0)- (x_1,y_1, z_1)) \bot e_1 \\ \\
&\Rightarrow (x_0-x_1, y_0-y_1,z_0-z_1) \bot e_2 \\
&= (x_0-x_1,y_0-y_1,z_0-z_1) \cdot (0,1,0) \\ 
&= (x_0-x_1)(0) + (y_0-y_1)(1) +(z_0-z_1)(0) = 0 \\
&= 0 + (y_0-y_1) + 0 = 0 \\
&=y_0-y_1=0
\end{split}
$$
Nos queda que $y_0 = y_1$ 

Por lo tanto tienen la misma segunda coordenada.

## 9. En cada inciso halle la ecuación cartesiana para la superficie de revolución generada por el lugar geométrico $\mathscr{G}$ y la recta $\ell$.

> **Lema 1:** Si $S, C \in \R^3 \ \text y \ C-S\bot e_3 \Rightarrow C \ \text  y \ S$ tienen la misma tercer coordenada. 
>
> **Lema 2:** Si $S, C \in \R^3 \ \text y \ C-S\bot e_2 \Rightarrow C \ \text  y \ S$ tienen la misma segunda coordenada. 
>
> **Lema 3:** Si $S, C \in \R^3 \ \text y \ C-S\bot e_1 \Rightarrow C \ \text  y \ S$ tienen la misma primer coordenada. 
>
> **Corolario 1:** Si $C \in Z \ \text y \ Q \in \mathscr{R}$, donde $\mathscr{R}$ es la superficie de revolución generada por el eje $Z$, entonces $C$ y $Q$ tienen la misma tercer coordenada. 
>
> **Corolario 2:** Si $C \in Y \ \text y \ Q \in \mathscr{R}$, donde $\mathscr{R}$ es la superficie de revolución generada por el eje $Y$, entonces $C$ y $Q$ tienen la misma segunda coordenada. 
>
> **Corolario 3:** Si $C \in X \ \text y \ Q \in \mathscr{R}$, donde $\mathscr{R}$ es la superficie de revolución generada por el eje $X$, entonces $C$ y $Q$ tienen la misma primer coordenada. 

---

### a) $\mathscr{G} \ :"x^2 + 2y^2 = 1, z = 0 "$ y $\ell$ es el eje $X$.

Sean $C \in eje \ X$$, $  $Q \in \mathscr{G}$  y $P \in \mathscr{R}$

Como $\mathscr{G}:"x^2 + 2y^2 = 1, z = 0 "$ por lo tanto 

Se hace un cambio de variable $w = y$
$$
w = y =  \sqrt{\frac{(1-x²)}{2}}
$$
Por el lema 3 y el corolario 3 podemos deducir los valores de $C$ y $Q$.

Donde $C=(x,0,0)$, $Q=(x,w,0)$, $P(x,y,z)$ y $v=e_1 = (1,0,0)$

* Probar que $(C-P)\bot v$:
  $$
  \begin{split}
  (C-P)\bot e_1 &= ((x,0,0)-(x,y,z))\cdot(1,0,0) \\
  &= (x-x,0-y,0-z)\cdot(1,0,0) \\
  &= (0,-y,-z)\cdot(1,0,0) \\
  &=(0,0,0)
  \end{split}
  $$
  Por lo tanto $(C-P)$ es perpendicular a $e_1$ 

* Probar que $(C-Q)\bot v$:
  $$
  \begin{split}
  (C-Q)\bot e_1 &= ((x,0,0)-(x,w,0))\cdot(1,0,0) \\
  &= (x-x,0-w,0-0)\cdot(1,0,0) \\
  &= (0,-w,0)\cdot(1,0,0) \\
  &=(0,0,0)
  \end{split}
  $$
  Por lo tanto $(C-Q)$ es perpendicular a $e_1$ 

* Probar que $d(P,C)=d(Q,C)$:
  $$
  \begin{split}
  d(P,C)&=\sqrt{(x_1-x_2)^2 + (y_1-y_2)^2 + (z_1-z_2)^2}\\
  &= \sqrt{(x-x)^2 + (y-0)^2 + (z-0)^2} \\
  &= \sqrt{(0)^2 + (y)^2 + (z)^2} \\
  &= \sqrt{y^2 + z^2}
  \end{split}
  $$

  $$
  \begin{split}
  d(Q,C)&=\sqrt{(x_1-x_2)^2 + (y_1-y_2)^2 + (z_1-z_2)^2}\\
  &= \sqrt{(x-x)^2 + (w-0)^2 + (0-0)^2} \\
  &= \sqrt{(0)^2 + (w)^2 + (0)^2} \\
  &= \sqrt{(w)^2 } = w
  \end{split}
  $$

  Desarrollamos la igualdad
  $$
  d(P,C) = d(Q,C) \\
  \sqrt{y^2+z^2}=w
  $$
  Como $w = \sqrt{\frac{(1-x²)}{2}}$
  $$
  \sqrt{y^2+z^2}= \sqrt{\frac{(1-x²)}{2}} \\
  y^2+z^2= \frac{(1-x²)}{2} \\
  2(y^2+z^2)= (1-x²) \\
  \sqrt{1-2(y^2+z^2)}-x = 0 \\
  $$
  Por lo tanto los puntos $(x,y,z) \in \mathscr{R}$ tiene que ser la ecuación cartesiana $\sqrt{1-2(y^2+z^2)}-x=0$

  <iframe src="https://www.geogebra.org/3d/nqqgdmf8?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>

***

### b) $\mathscr{G}:x^2 − 2y + 3 = 1, z = 0$ y $\ell$ es el eje $Y$.

Sean $C \in eje \ Y$$, $ $Q \in \mathscr{G}$  y $P \in \mathscr{R}$

Como $\mathscr{G}:"x^2 − 2y + 3 = 1"$ por lo tanto 

Se hace un cambio de variable $w = x$
$$
w = x =  \sqrt{-2+2y}
$$


Por el lema 2 y el corolario 2 podemos deducir los valores de $C$ y $Q$.

Donde $C=(0,y,0)$, $Q=(w,y,0)$, $P(x,y,z)$ y $v=e_2 = (0,1,0)$. 

* Probar que $(C-P)\bot v$:
  $$
  \begin{split}
  (C-P)\bot e_2 &= ((0,y,0)-(x,y,z))\cdot(0,1,0) \\
  &= (0-x,y-y,0-z)\cdot(0,1,0) \\
  &= (-x,0,-z)\cdot(0,1,0) \\
  &=(0,0,0)
  \end{split}
  $$
  Por lo tanto $(C-P)$ es perpendicular a $e_2$ 

* Probar que $(C-Q)\bot v$:
  $$
  \begin{split}
  (C-Q)\bot e_2 &= ((0,y,0)-(w,y,0))\cdot(0,1,0) \\
  &= (0-w,y-y,0-0)\cdot(0,1,0) \\
  &= (-w,0,0)\cdot(0,1,0) \\
  &=(0,0,0)
  \end{split}
  $$
  Por lo tanto $(C-Q)$ es perpendicular a $e_2$ 

* Probar que $d(P,C)=d(Q,C)$:
  $$
  \begin{split}
  d(P,C)&=\sqrt{(x_1-x_2)^2 + (y_1-y_2)^2 + (z_1-z_2)^2}\\
  &= \sqrt{(x-0)^2 + (y-y)^2 + (z-0)^2} \\
  &= \sqrt{(x)^2 + (0)^2 + (z)^2} \\
  &= \sqrt{x^2 + z^2}
  \end{split}
  $$

  $$
  \begin{split}
  d(Q,C)&=\sqrt{(x_1-x_2)^2 + (y_1-y_2)^2 + (z_1-z_2)^2}\\
  &= \sqrt{(w-0)^2 + (y-y)^2 + (0-0)^2} \\
  &= \sqrt{(w)^2 + (0)^2 + (0)^2} \\
  &= \sqrt{(w)^2 } = w
  \end{split}
  $$

  Desarrollamos la igualdad
  $$
  d(P,C) = d(Q,C) \\
  \sqrt{x^2+z^2}=w
  $$
  Como $w =\sqrt{2y-2}$
  $$
  \sqrt{x^2+z^2}= \sqrt{2y-2} \\
  x^2+z^2= 2y-2 \\
  \frac{x^2+z^2}{2} + 1 - y = 0 \\
  $$

Por lo tanto los puntos $(x,y,z) \in \mathscr{R}$ tiene que ser $\frac{x^2+z^2}{2} + 1=y$

**Gráfica**

<iframe src="https://www.geogebra.org/3d/usbxsav5?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>

---

### c) $\mathscr{G}: x^2 + 2y^2 + 6y − 7 = 1, z = 0$ y $\ell$ es el eje $X$.

Sean $C \in eje \ X$$, $ $Q \in \mathscr{G}$  y $P \in \mathscr{R}$

Como $\mathscr{G}:"x^2 + 2y^2 + 6y − 7 = 1"$ por lo tanto 

Se hace un cambio de variable $w = y$
$$
w = y =  \frac{1}{2 (-3 + \sqrt{25 - 2 x^2})}
$$
Por el lema 3 y el corolario 3 podemos deducir los valores de $C$ y $Q$

Donde $C=(x,0,0)$, $Q=(x,w,0)$, $P(x,y,z)$ y $v=e_1 = (1,0,0)$

* Probar que $(C-P)\bot v$:
  $$
  \begin{split}
  (C-P)\bot e_1 &= ((x,0,0)-(x,y,z))\cdot(1,0,0) \\
  &= (x-x,0-y,0-z)\cdot(1,0,0) \\
  &= (0,-y,-z)\cdot(1,0,0) \\
  &=(0,0,0)
  \end{split}
  $$
  Por lo tanto $(C-P)$ es perpendicular a $e_1$ 

* Probar que $(C-Q)\bot v$:
  $$
  \begin{split}
  (C-Q)\bot e_1 &= ((x,0,0)-(x,w,0))\cdot(1,0,0) \\
  &= (x-x,0-w,0-0)\cdot(1,0,0) \\
  &= (0,-w,0)\cdot(1,0,0) \\
  &=(0,0,0)
  \end{split}
  $$
  Por lo tanto $(C-Q)$ es perpendicular a $e_1$ 

* Probar que $d(P,C)=d(Q,C)$:
  $$
  \begin{split}
  d(P,C)&=\sqrt{(x_1-x_2)^2 + (y_1-y_2)^2 + (z_1-z_2)^2}\\
  &= \sqrt{(x-x)^2 + (y-0)^2 + (z-0)^2} \\
  &= \sqrt{(0)^2 + (y)^2 + (z)^2} \\
  &= \sqrt{y^2 + z^2}
  \end{split}
  $$

  $$
  \begin{split}
  d(Q,C)&=\sqrt{(x_1-x_2)^2 + (y_1-y_2)^2 + (z_1-z_2)^2}\\
  &= \sqrt{(x-x)^2 + (w-0)^2 + (0-0)^2} \\
  &= \sqrt{(0)^2 + (w)^2 + (0)^2} \\
  &= \sqrt{(w)^2 } = w
  \end{split}
  $$

  Desarrollamos la igualdad
  $$
  d(P,C) = d(Q,C) \\
  \sqrt{y^2+z^2}=w
  $$
  Como $w = \frac{1}{2 (-3 + \sqrt{25 - 2 x^2})}$

$$
\sqrt{y^2+z^2}= \frac{1}{2 (-3 + \sqrt{25 - 2 x^2})} \\
y = \frac{\sqrt{17 - x^2 + 3 \sqrt{25 - 2 x^2} - 512 z^2 + 128 x^2 z^2 - 
 8 x^4 z^2}}{(2 \sqrt{2} \sqrt{(-8 + x^2)^2})}
$$

Por lo tanto los puntos $(x,y,z) \in \mathscr{R}$ tiene que ser $\frac{x^2+z^2}{2} + 1=y$

**Gráfica**

<iframe src="https://www.geogebra.org/3d/h7nq4gvf?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>

---

### d) $\mathscr {G}: x^2 + 8y = 1, z = 0$ y $\ell$ es el eje $Y$.

---

### e) $\mathscr{G}:2x^2 − 5y + 7 = 1, z = 0$ y $\ell$ es el eje $X$.

## 10. Para cada uno de los siguientes incisos deberá:

* a) Identificar a $\mathscr{Q}$
* b) Obtener ecuaciones cartesianas de $\mathscr{Q}∩π_{XY}, \mathscr{Q}∩π_{YZ}$ y $\mathscr{Q}∩π_{XY}$ indicando qué lugar geométrico es. En caso de ser una cónica, indicar centros, vértices, ejes mayores y menores (donde existan según el caso).
* c) Hallar las secciones transversales de $\mathscr{Q}$ para $π_1 : x = 4, π_2 : y = 4, π_3 : z = 4$. En caso de ser una cónica, indicar centros, vértices, ejes mayores y menores (donde existan según el caso).

### i) $\mathscr{Q} : x²/9 + y²/16 − z^2/4 = 1$

### ii) $\mathscr{Q} : x²/4 + y²/9 = 0$

### iii) $\mathscr{Q} : 2y^2 − 4z^2 = x^2$

### iv) $\mathscr{Q} : 5y^2 + y²/3 − z = x^2$

### v) $\mathscr{Q} : x + y^3 − z/5 = x^2$


## 11. Indique si los siguientes enunciados son verdaderos o falsos, justifica tu respuesta con una demostración o un contra ejemplo.

### a) $\mathscr{G} : 5z^2 + 5y^2 = 1$ es un cilindro elíptico cuyo eje es el eje $X$

---

### b) $\mathscr{G}:x^2 + 2z^2 = 0$ posee las siete simetrías vistas en clase.

---

### c) Considera $P = (2, 3, 8)$ y $P' = (−2, −3, −8), P y P'$ son simétricos respecto al plano $π_{XZ}$

---

### d) Considera $P = (2, 3, 8)$ y $P' = (−2, −3, −8), P y P'$ son simétricos respecto al eje $Y$ .

---

### e) La intersección entre una superficie cuadrática y un plano cartesiano $(π_{XY} , π_{Y Z} , π_{XZ} )$ es una cónica.

---

### f) $x^2 + y^2 = 25$ Es la ecuación de una circunferencia con radio $5$

---

### g) Todo lugar geométrico cumple al menos una de las simetrías respecto a ejes, planos (coordenados) o el origen.
