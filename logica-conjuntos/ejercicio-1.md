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

