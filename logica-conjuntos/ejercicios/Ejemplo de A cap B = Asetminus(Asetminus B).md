Ejemplo de $A \cap B = A\setminus(A\setminus B)$
$$
\begin{split}

\text{Por reducción al absurdo}\\
\text{Negamos }  A\setminus(A\setminus B)  \\
A \cap B &= A\setminus(A\setminus B) \\
x\in A \and x\in B &= x\in A\and x\notin(x\in A \and x\notin B)\\
&= \neg\big( x\in A\and x\notin(x\in A \and x\notin B)\big) \\
&= \neg(x\in A) \or \neg(x\notin(x\in A \and x\notin B)) \quad \text{Ley De Morgan}\\
&= x\notin A \or (x\in(x\in A \and x\notin B)) \quad \\
&= x\notin A \or (x\in A \and x\notin B) \quad \\
&= (x\notin A \or x\in A) \and(x\notin A \or x\notin B) \quad \text{Distribución}\\
&=\top \and(x\notin A \or x\notin B) \quad \ \quad \ \quad \ \quad \ \quad \ \quad p\or \neg p \equiv\top \\
&=x\notin A \or x\notin B \quad \ \quad \ \quad \ \quad \ \quad \ \quad \ \quad \ \quad \top\and  p \equiv p \\
&=\neg(x\in A \and x\in B) \quad \ \quad \ \quad \ \quad \ \quad \ \quad \ \quad \ \text{Ley De Morgan}\\
x\in A \and x\in B &= \neg(x\in A \and x\in B)  \quad \ \quad \ \quad \ \quad \ \quad \ \quad \ \quad \ \text{Contradicción } \\
\text{No es cierto negar }  A\setminus(A\setminus B) \\
 \text{Por lo tanto } A \cap B &= A\setminus(A\setminus B) \quad \blacksquare \\

\end{split}
$$
