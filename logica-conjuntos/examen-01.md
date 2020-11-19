# Examen

**Rigoberto Canseco López**

##  1. Considere la siguiente fórmula:

Da una fórmula equivalente en la que la negación afecte sólo a fórmulas atómicas
$$
\neg\bigg((\forall x_1)\Big((\exist x_2)\big(A^1_0(x_1)\to A^2_0(x_1,x_2)\big)\to A^1_1(x_2)\and\big((\forall x_3)A^1_2(x_3)\big)\Big)\bigg) \\
(\exist x_1)\neg\Big((\exist x_2)\big(A^1_0(x_1)\to A^2_0(x_1,x_2)\big)\to A^1_1(x_2)\and\big((\forall x_3)A^1_2(x_3)\big)\Big) \\
(\exist x_1)\Big(\neg(\exist x_2)\big(A^1_0(x_1)\to A^2_0(x_1,x_2)\big)\to A^1_1(x_2)\and\big((\forall x_3)A^1_2(x_3)\big)\Big) \\

(\exist x_1)\bigg((\forall x_2)\neg\Big(\big(A^1_0(x_1)\to A^2_0(x_1,x_2)\big)\to A^1_1(x_2)\and\big((\forall x_3)A^1_2(x_3)\big)\Big)\bigg) \\

(\exist x_1)\bigg((\forall x_2)\Big(\big(A^1_0(x_1)\to A^2_0(x_1,x_2)\big)\and \neg \big( A^1_1(x_2)\and((\forall x_3)A^1_2(x_3))\big)\Big)\bigg) \\

(\exist x_1)\bigg((\forall x_2)\Big(\big(A^1_0(x_1)\to A^2_0(x_1,x_2)\big)\and \big( \neg A^1_1(x_2)\or \neg ((\forall x_3)A^1_2(x_3))\big)\Big)\bigg) \\


(\exist x_1)\bigg((\forall x_2)\Big(\big(A^1_0(x_1)\to A^2_0(x_1,x_2)\big)\and \big(\neg  A^1_1(x_2)\or ((\exist x_3)\neg A^1_2(x_3))\big)\Big)\bigg) \\


(\exist x_1)(\forall x_2)\big(A^1_0(x_1)\to A^2_0(x_1,x_2)\big)\and \Big(\neg A^1_1(x_2)\or \big((\exist x_3)\neg A^1_2(x_3)\big)\Big) \quad \blacksquare
$$

***

## 2. Para la siguiente fórmula e interpretación, escribe su traducción al español ordinario y determina si es verdadera o falsa:

![](/home/rigoberto/.config/Typora/typora-user-images/image-20201016164222613.png)

**Existe un entero no negativo que sumado a si mismo es igual a 1.**

**Es falso.** 

***

## 3. Determina

$$
\begin{split}
&\Gamma = \{(p_0 \to p_1)\and (p_2 \to p_3), p_1 \or p_3 \to p_4, \neg p_4\} \\
&\alpha = \neg (p_0 \or p_4)
\end{split}
$$

Determinar $\Gamma \vDash \alpha$ 

Por demostrar que $\Gamma$ implica lógicamente a $\alpha$. 
Vamos a afirmar el antecedente y negar consecuente para llagar a una contradicción.
$$
p \to q \\
\top \to \bot \equiv \bot
$$
Tenemos que
$$
\underbrace{\Big(\big((p_0 \to p_1)\and (p_2 \to p_3) \big)\and \big(p_1 \or p_3 \to p_4 \big) \and \neg p_4\Big)}_{\text{antecedente}} \to \underbrace{\neg \Big(p_0 \or p_4\Big)}_{\text{consecuente}}
$$
Por lo tanto 
$$
\begin{split}
\underbrace{\Big(\big((p_0 \to p_1)\and (p_2 \to p_3) \big)\and \big(p_1 \or p_3 \to p_4 \big) \and \neg p_4\Big)}_{\top} \to \underbrace{\neg \Big(p_0 \or p_4\Big)}_{\bot} &\equiv \bot \\


\Big(\big((p_0 \to p_1)\and (p_2 \to p_3) \big)\and \big(p_1 \or p_3 \to p_4 \big) \and \neg p_4\Big) &\equiv \top\\ 
\neg \Big(p_0 \or p_4\Big) &\equiv \bot

\end{split}
$$
La tabla de verdad para $\neg \Big(p_0 \or p_4\Big) $
$$
\begin{array} {|r|r|r|}
\hline
  p_0  &  p_4  & \neg(p_0 \or p_4)  \\
\hline
   0   &   0   &   1\\
   0   &   1   &   0\\
   1   &   0   &   0\\
   1   &   1   &   0\\
\hline
\end{array}
$$
Solo nos fijaremos en las casos donde el resultado sea $0$.

Ahora vamos a intentar hacer verdadero a $\Big(\big((p_0 \to p_1)\and (p_2 \to p_3) \big)\and \big(p_1 \or p_3 \to p_4 \big) \and \neg p_4\Big)$, con los valores de $p_0 =1$ y $p_4=0$. Sustituimos los valores en la fórmula. 
$$
\Big(\big((\top \to p_1)\and (p_2 \to p_3) \big)\and \big(p_1 \or p_3 \to \bot \big) \and \neg \bot \Big)
$$
Cada elemento de la conjunción debe de ser verdadero para que toda la fórmula sea verdadera. Tenemos que:
$$
\begin{split}
\Big( \underbrace{\big((\top \to p_1)\and (p_2 \to p_3) \big)}_{\top}\and \underbrace{\big(p_1 \or p_3 \to \bot \big)}_{\top} \and \underbrace{\neg \bot}_{\top} \Big) &\equiv \top\\
\big((\top \to p_1)\and (p_2 \to p_3) \big) &\equiv \top \\
\big(p_1 \or p_3 \to \bot \big) & \equiv \top \\
\neg \bot &\equiv \top
\\
\end{split}
$$
Para $\neg \bot \equiv \top$ se cumple 

Para $\big(p_1 \or p_3 \to \bot \big) \equiv \top $ se cumple cuando $p_1 = 0$ y $p_3=0$

Ahora sustituimos el valor de $p_0,p_1,p_3, p_4$ en $\big((\top \to p_1)\and (p_2 \to p_3) \big) \equiv \top $ y validamos si se cumple
$$
\big((\top \to \bot)\and (p_2 \to \bot) \big) \equiv \top \quad \text{contradicción}
$$
Llegamos a una contradicción y vemos que no se cumple

Por lo tanto  $\Gamma$ no implica lógicamente a $\alpha$. $\quad \blacksquare$



***

## 4. ¿Qué puede decir de la siguiente fórmula?

$$
(¬p_0\to p_0)→p_0
$$

Seleccione una:

a. Nada

b. Que es contradicción

c. Que es una contingencia

d. **Que es tautología**

## 5. Da un lenguaje de primer orden para traducir en él la siguiente proposición: Cualquier barbero en México afeita exactamente a aquellos hombres en México que no se afeitan a sí mismos

$$
A^1_0(x):= x \text{ es barbero en México} \\
A^1_1(x, y):= x \text{ afeita a } y \\
\ \\
(\exist x_0)(A^1_0(x_0))(\forall x_1) (\neg A^1_1(x_1,x_1)) \to A^1_1(x_0,x_1)
$$

