## 5. Da un lenguaje de primer orden para traducir en él la siguiente proposición: Cualquier barbero en México afeita exactamente a aquellos hombres en México que no se afeitan a sí mismos

$$
A^1_0(x):= x \text{ es barbero en México} \\
A^1_1(x, y):= x \text{ afeita a } y \\
\ \\
(\exist x_0)(A^1_0(x_0))(\forall x_1) (\neg A^1_1(x_1,x_1)) \to A^1_1(x_0,x_1) \quad \blacksquare
$$

