# Ejercicios Semana 3

**Lógica Matemática I**

Instrucciones: Lea cuidadosamente cada pregunta y conteste adecuadamente. Valor Total: 50 puntos

## 1. [30 puntos] Investiga qué dice el teorema de lectura única para el lenguaje proposicional (también conocido como teorema de descomposición  única) y demuéstralo utilizando alguna de las 3 construcciones que dimos para el lenguaje proposicional.

*Toda fórmula bien formada en el lenguaje proposicional se expresa de manera única*

Tenemos las siguientes fórmula bien formadas (**F.B.F.**) $f_1$ y $f_2$
$$
\begin{split}
&A=\{P_k | k\in \N\}\cup\{\neg, \and, \or,\to,\leftrightarrow\}\cup\{(,)\} \\
&\Phi = \text{Expresición bien formada}\\
&\Psi = \text{Expresición bien formada}\\

&\Phi_*(\alpha,\beta):= (*,\alpha, \beta) &\\
&\Psi_*(\gamma,\delta):= (*,\gamma, \delta) 

\end{split}
$$
Donde
$$
* \in \{ \or,\and,\to,\leftrightarrow \} \\
\Phi_*(\alpha,\beta)= (*,\alpha, \beta) = \Psi_*(\gamma,\delta)= (*,\gamma, \delta) 
$$
Por lo tanto
$$
\Phi_*(\alpha,\beta) = \Psi_*(\gamma,\delta)\\
(*,\alpha, \beta) = (*,\gamma, \delta) \\
* = *, \quad \alpha = \gamma, \quad \beta = \delta \\
\Phi = \Psi
$$

***

## 2. Determina si las siguientes expresiones son o no fórmulas bien formadas.

* a) [10 puntos] $((P0 ∧ (¬P1)) → (P8 ∨ (P2 ↔ P3)))$

  En el primer nivel
  $$
  %%\Big( \underbrace{ \big(P_0 \and (\neg P_1)\big) }_{\alpha} 
  %%\to 
  %%\big( \underbrace{ P_8 \or (P_2 \leftrightarrow P_3)\big)}_{\beta} \Big) \\
  \Big(\overbrace{\big(P_0 \and (\neg P_1)\big) }^{\alpha} \overbrace{\to}^* \overbrace{ \big( P_8 \or (P_2 \leftrightarrow P_3)\big)}^{\beta} \Big) \quad (\alpha, *, \beta) \quad  \text{donde } \alpha, \beta \in P \quad \text y \quad* = \to  \tag 1
  $$
  En el segundo nivel
  $$
  (\overbrace {P_0}^\alpha \overbrace \and ^* \overbrace{(\neg P_1)}^{\beta}\big) 
  \quad (\alpha, *, \beta) \quad  \text{donde } \alpha, \beta \in P \quad \text y \quad* = \and \tag{2}
  $$

  $$
  \big(\overbrace{ P_8}^\alpha \overbrace \or ^* \overbrace{(P_2 \leftrightarrow P_3)}^\beta\big)
  \quad (\alpha, *, \beta) \quad  \text{donde } \alpha, \beta \in P \quad \text y \quad* = \or \tag{3}
  $$

  * En $(2)$
    $$
    (P_0 \and \overbrace{(\neg P_1)}^{\alpha}\big)   \\
    P_0 \text{ es una fórmula bien formada} \\
    \alpha \text{ es una fórmula bien formada} \ (\neg,\alpha)\\
    $$

  * En $(3)$
    $$
    \big(\overbrace{ P_8}^\alpha \overbrace \or ^* \overbrace{(P_2 \leftrightarrow P_3)}^\beta\big) \\
    \alpha \text{ es una fórmula bien formada} \\
    $$

  En el tercer nivel
  $$
  (\overbrace{P_2}^\alpha \overbrace\leftrightarrow ^* \overbrace{P_3}^\beta ) \ \quad (\alpha, *, \beta) \quad  \text{donde } \alpha, \beta \in P \quad \text y \quad * = \leftrightarrow \tag{4}
  $$

  * En $(4)$
    $$
    P_2 \text{ es una fórmula bien formada} \\
    P_3 \text{ es una fórmula bien formada} \\
    $$

  Por lo tanto es una fórmula bien formada.  $\quad \blacksquare$

***

* b) [10 puntos] $(((¬P4 → P8) ↔ (P1 ∨ P7)) ∧ ((¬P3) ∨ P9))$

  En el primer nivel
  $$
  \Big(
  \overbrace{\big((\neg P_4 \to P_8) \leftrightarrow (P_1 \or P_7) \big)}^\alpha
  \overbrace \and ^ * 
  \overbrace{\big((\neg P_3) \or P_9\big) }^\beta\Big) 
  \quad (\alpha, *, \beta) \quad  \text{donde } \alpha, \beta \in P \quad \text y \quad* = \and \tag 1
  $$
  En el segundo nivel
  $$
  \big(\overbrace{(\neg P_4 \to P_8)}^\alpha \overbrace \leftrightarrow ^* \overbrace{(P_1 \or P_7)}^\beta \big)
  \quad (\alpha, *, \beta) \quad  \text{donde } \alpha, \beta \in P \quad \text y \quad* = \leftrightarrow \tag 2
  $$

  $$
  \big(\overbrace{(\neg P_3)}^\alpha \overbrace \or ^ * \overbrace{ P_9 }^\beta\big) 
  \quad (\alpha, *, \beta) \quad  \text{donde } \alpha, \beta \in P \quad \text y \quad* = \or \tag 3
  $$

  * En $(3)$
    $$
    \big(\overbrace{(\neg P_3)}^\alpha \overbrace \or ^ * \overbrace{ P_9 }^\beta\big) 
    \\
    \alpha \text{ es una fórmula bien formada} \ (\neg,\alpha)\\
    \beta \text{ es una fórmula bien formada}
    $$

  En el tercer nivel
  $$
  (\overbrace{\neg P_4}^\alpha \overbrace \to ^* \overbrace {P_8} ^\beta) 
  \quad (\alpha, *, \beta) \quad  \text{donde } \alpha, \beta \in P \quad \text y \quad* = \rightarrow \tag 4
  $$

  $$
  \overbrace{P_1}^\alpha \overbrace \or ^* \overbrace {P_7}^\beta 
  \quad (\alpha, *, \beta) \quad  \text{donde } \alpha, \beta \in P \quad \text y \quad* = \or
  \tag 5
  $$

  * En $(4)$
    $$
    (\overbrace{\neg P_4}^\alpha \overbrace \to ^* \overbrace {P_8} ^\beta) 
    \\
    \alpha \text{ es una fórmula mal formada ya que hace falta } () \\
    \beta \text{ es una fórmula bien formada}
    $$

  * En $(5)$
    $$
    \overbrace{P_1}^\alpha \overbrace \or ^* \overbrace {P_7}^\beta \\
    \alpha \text{ es una fórmula bien formada} \\
    \beta \text{ es una fórmula bien formada}
    $$

  

  Por lo tanto  no es una fórmula bien formada. $\quad \blacksquare$

***



