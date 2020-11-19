# Examen

Rigoberto Canseco López

## 1. Indique si los siguientes enunciados son verdaderos o falsos, justifica tu respuesta con una demostración o un contra ejemplo.

### a) x2 + y2 = 25 Es la ecuación de una circunferencia con radio 5.

Es verdadero

### b) Todo lugar geométrico cumple al menos una de las simetrías respecto a ejes, planos (coordenados) o el origen.

Es verdadero

## 2. En cada inciso halle la ecuación cartesiana para la superficie de revolución generada por el lugar geométrico G y la recta L.

### a) G : “x2 + 2y2 + 6y − 7 = 1, z = 0” L es el eje X.

Sean $C \in eje \ X$$, $ $Q \in \mathscr{G}$  y $P \in \mathscr{R}$

Como $\mathscr{G}:"x^2 + 2y^2 + 6y − 7 = 1"$ por lo tanto 

Se hace un cambio de variable $w = x$
$$
w = x =  \sqrt{8-2y^2-6y}
$$

* Por el lema 2 y el corolario 2 podemos deducir los valores de $C$ y $Q$.

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
    Como $w =  \sqrt{8-2y^2-6y}$
    $$
    \sqrt{x^2+z^2}=   \sqrt{8-2y^2-6y}\\
    x^2+z^2=   8-2y^2-6y \\
    x^2+z^2- 8+2y^2+6y=0 \\
    $$

  Por lo tanto los puntos $(x,y,z) \in \mathscr{R}$ tiene que ser $x^2+z^2- 8+2y^2+6y=0 $

<iframe src="https://www.geogebra.org/3d/yjhc668b?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>



### b) G : “x2 + 8y = 1, z = 0” y L el eje Y

Sean $C \in eje \ Y$$, $ $Q \in \mathscr{G}$  y $P \in \mathscr{R}$

Como $\mathscr{G}:"x^2 + 8y = 1"$ por lo tanto 

Se hace un cambio de variable $w = y$
$$
w = y =  \frac{1-x²}{8}
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
  Como $w = \frac{1-x²}{8}$
  $$
  \sqrt{y^2+z^2}= \frac{1-x²}{8} \\
  y^2+z^2= \frac{(1-x²)²}{64} \\
  y^2+z^2 -\frac{(1-x²)²}{64} = 0\\
  $$
  Por lo tanto los puntos $(x,y,z) \in \mathscr{R}$ tiene que ser la ecuación cartesiana $y^2+z^2 -\frac{(1-x²)²}{64} = 0$


