# Conjuntos y lógica

**Rigoberto Canseco López**

## 1. Para los siguientes conjuntos de proposiciones, considera la interpretación de las variables proposicionales sugerida y traduce al lenguaje formal de la lógica proposicional.

### Ejercicio 1

Si Argentina o Brasil se incorpora a la alianza entonces si o Chile o Ecuador la boicotea entonces, aunque Perú no la boicotee, Venezuela la boicotea. Si o Perú o Nicaragua no la boicotea entonces Uruguay se incorpora a la alianza. **Por lo tanto**, si Argentina se incorpora a la alianza entonces si Chile la boicotea entonces Uruguay se incorpora a la alianza.

* $p_0 := \text {Argentina se incorpora a la alianza}$ 
  
* $p_1 := \text{Brasil se incorpora a la alianza}$

* $p_2 := \text{Chile boicotea la alianza}$ 

* $p_3 := \text{Ecuador boicotea la alianza}$ 

* $p_4 := \text{Perú boicotea la alianza}$

*  $p_5 := \text {Venezuela boicotea la alianza}$ 

* $p_6 := \text {Nicaragua boicotea la alianza}$ 

* $p_7 := \text{Uruguay se incorpora a la alianza}$

  
     $$
     %%((p_0 \or p_1) \Rightarrow ( ((p_2 \or p_3) \Rightarrow (\neg \ p_4 \and p_5)) \and ( \neg(p_4 \or  \ p_6) \Rightarrow p_7))) \Rightarrow (p_0 \Rightarrow (p_2 \Rightarrow p_7)) \\
     
     \bigg(\Big((p_0 \or p_1) \rightarrow \big(( p_2 \or p_3 )  \rightarrow (\neg p_4 \rightarrow p_5)\big) \Big) \and
     \Big(\neg(p_4 \or p_6) \rightarrow p_7\Big)\bigg) \rightarrow \bigg(p_0 \rightarrow (p_2 \rightarrow p_7)\bigg) \quad \blacksquare
     $$
     


***

### Ejercicio 2

Si te inscribes en el curso y estudias duro entonces pasarás, pero si te inscribes en el curso y no estudias duro, entonces no pasaras. **Por lo tanto**, si te inscribes en el curso entonces o estudias duro y pasarás o no estudias duro y no pasarás. 

* $p_0 := \text{Te inscribes en el curso}$ 

* $p_1 := \text{Estudias duro}$

* $p_2 := \text{Pasarás el curso}$

  

$$
\Big( \big ((p_0 \and p_1) \to p_2\big) \and \big((p_0 \and \neg p_1) \to \neg p_2\big)\Big) \to \Big(p_0 \to \big( (p_1 \and p_2) \or (\neg p_1 \and \neg p_2)\big) \Big) \quad \blacksquare
$$

***

## 2. Para cada inciso del ejercicio anterior, determina si el conjunto de fórmulas que antecede al "Por lo tanto" implica lógicamente a la fórmula que le precede.

### Ejercicio 1 

Tenemos la siguiente fórmula
$$
\underbrace{\bigg(\Big((p_0 \or p_1) \rightarrow \big(( p_2 \or p_3 )  \rightarrow (\neg p_4 \rightarrow p_5)\big) \Big) \and \Big(\neg(p_4 \or p_6) \rightarrow p_7\Big)\bigg) }_{\text{antecedente}}
\rightarrow \underbrace{\bigg(p_0 \rightarrow (p_2 \rightarrow p_7)\bigg) }_{\text{consecuente}}
$$

Reemplazamos las implicaciones $p \Rightarrow q = \neg p \or q$
$$
(( \neg(p_0 \or p_1) \or (\neg ( p_2 \or p_3 ) \or (p_4 \or p_5)) ) \and
((p_4 \or p_6) \or p_7)) \rightarrow (\neg p_0 \or (\neg p_2 \or p_7))
$$
Reemplazamos $\neg(p\or q) = \neg p \and \neg q \text { y } \neg(p\and q) = \neg p \or \neg q$
$$
(( \neg p_0 \and \neg p_1 \or ((\neg p_2 \and \neg p_3 ) \or p_4 \or p_5) ) \and
(p_4 \or p_6 \or p_7)) \rightarrow (\neg p_0 \or \neg p_2 \or p_7)
$$
Separamos la implicación

Antecedente:$\quad
( \neg p_0 \and \neg p_1 \or ((\neg p_2 \and \neg p_3 ) \or p_4 \or p_5) ) \and
(p_4 \or p_6 \or p_7)$
Consecuente:$\quad \neg p_0 \or \neg p_2 \or p_7$

Negamos el consecuente y afirmamos el antecedente para llegar a una contradicción
$$
\neg p_0 \or \neg p_2 \or p_7 = \bot \quad \text{ Por lo tanto } p_0=\top, p_2= \top, p_7 = \bot
$$
Reemplazamos los valores de $p_0,p_2,p_7$ en el antecedente y lo simplificamos 
$$
( \neg (T) \and \neg p_1 \or ((\neg (T) \and \neg p_3 ) \or p_4 \or p_5) ) \and (p_4 \or p_6 \or (F))  \\
(F \and \neg p_1 \or ((F \and \neg p_3 ) \or p_4 \or p_5) ) \and (p_4 \or p_6 \or F)  \\
( F \and \neg p_1 \or (F \or p_4 \or p_5) ) \and(p_4 \or p_6 \or F)  \\
( F  \or (F \or p_4 \or p_5) ) \and (p_4 \or p_6 \or F)  \\
( F  \or p_4 \or p_5) \and (p_4 \or p_6 \or F)  \\
(p_4 \or p_5) \and (p_4 \or p_6 )
$$
Realizamos la tabla de verdad para $(p_4 \or p_5) \and (p_4 \or p_6 )$
$$
\begin{array} {|r|r|r|r|}
\hline
  p_4  &  p_5  &  p_6  &  (p_4 \or p_5) \and (p_4 \or p_6 )  \\
\hline
   1   &   1   &   1   &                1                \\
   1   &   1   &   0   &                1                \\
   1   &   0   &   1   &                1                \\
   1   &   0   &   0   &                1                \\
   0   &   1   &   1   &                1                \\
   0   &   1   &   0   &                0                \\
   0   &   0   &   1   &                0                \\
   0   &   0   &   0   &                0                \\
\hline
\end{array}
$$
Por lo tanto el antecedente es verdadero cuando $p_4 \or (p_5\and p_6) = \top$ , y como el antecedente es cierto y el consecuente  $\neg p_0 \or \neg p_2 \or p_7$ es falso la implicación es una contradicción. $\quad \blacksquare$

***

### Ejercicio 2

Tenemos la siguiente fórmula
$$
\underbrace {\Big( \big ((p_0 \and p_1) \to p_2\big) \and \big((p_0 \and \neg p_1) \to \neg p_2\big)\Big)}_{\text{antecedente}} \to \underbrace{\Big(p_0 \to \big( (p_1 \and p_2) \or (\neg p_1 \and \neg p_2)\big) \Big)}_{\text{consecuente}}
$$
Antecedente: $((p_0 \and p_1) \to p_2) \and ((p_0 \and \neg p_1) \to \neg p_2)$

Consecuente: $p_0 \to ( (p_1 \and p_2) \or (\neg p_1 \and \neg p_2))$

Negamos el consecuente y buscamos que el antecedente sea una tautología para llegar a una contradicción
$$
p_0 \to ( (p_1 \and p_2) \or (\neg p_1 \and \neg p_2)) \equiv \bot\\
p_0 = \bot ,\quad p_1=\top , \quad p_2 = \top
$$
Reemplazamos los valores de $p_0,p_1,p_2$ en el antecedente y lo simplificamos 
$$
((\bot \and \top) \to \top) \and ((\bot \and \neg \top) \to \neg \top) \\
(\bot \to \top) \and (\bot \to \neg \top) \\
\top \and (\bot \to\bot) \\
\top \and \top \\
\top
$$
Tenemos que el antecedente es Tautología y el consecuente es una contradicción, por lo tanto no se cumple la implicación. $\quad \blacksquare$ 

***

## 3. Paréntesis

Elimina tantos paréntesis como sea posible

*Solución*
$$
(p_0 \rightarrow ¬p_7) \and p_5 \\
p_0 \leftrightarrow p 1 \leftrightarrow \neg (p_5 \or p_6) \\
p_1 \and \neg p_0\or p 5 \and p 1
$$

***

Restaura los paréntesis de las siguientes fórmulas

*Solución*
$$
p_0 \or (¬p_1 \and p_5) \\
p_5 \rightarrow ¬(¬(¬p_1 \and p_0)) \\
(p_0 \rightarrow (¬((p_5 \and p_1) \rightarrow p_0 ) \and p_5)) \leftrightarrow p 1
$$

***

## 4. Para las siguientes fórmulas ofrece una fórmula equivalente en la que la negación afecte sólo a variables proposicionales, simplificando la fórmula dada a su expresión más simple.


$$
\neg \big((p_0 \or p_1) \and p_5 \leftrightarrow \neg p_6 \rightarrow p_5\big)\\
(((p_0\or p_1)\and p_5) \leftrightarrow (\neg p_6 \rightarrow p_5)) \\
(\neg((p_0 \or p_1) \and p_5) \and(\neg p_6 \rightarrow p_5)) \or (((p_0 \or p_1) \and p_5) \and \neg(\neg p_6 \rightarrow p_5)) \\
(((\neg p_0 \and p_1)\or \neg p_5) \and (\neg p_6 \rightarrow p_5)) \or (((p_0 \or p_1) \and p_5) \and (\neg p_6 \and \neg p_5)) \\
\Big(\big( (\neg p_0 \and \neg p_1) \or \neg p_5\big)\and (\neg p_6 \rightarrow p_5) \Big) \or \Big(\big((p_0 \or p_1) \and p_5\big) \and (\neg p_6 \and \neg p_5)\Big) \quad \blacksquare
$$


***


$$
\neg(p_6 \leftrightarrow p_7 \and p_8 \or \neg(p_9 \and \neg p_6 \rightarrow p_8)) \\
\neg(((p_6 \leftrightarrow p_7) \and p_8) \or \neg((p_9 \and \neg p_6) \rightarrow p_8) ) \\
\neg((p_6 \leftrightarrow p_7) \and p_8) \and \neg ((p_9 \and \neg p_6) \rightarrow p_8) \\
(\neg(p_6 \leftrightarrow p_7) \or \neg p_8) \and ((p_9 \and \neg p_6) \rightarrow p_8) \\
\big((\neg p_6 \and p_7) \or (p_6 \and \neg p_7) \or \neg p_8\big) \and \big((p_9 \and \neg p_6) \rightarrow p_8 \big) \quad \blacksquare
$$

***

$$
\neg(p_5 \rightarrow p_7 \or p_2 \leftrightarrow p_9 \and p_2 \or p_7 \rightarrow p_8) \\
\neg((p_5 \rightarrow (p_7 \or p_2)) \leftrightarrow (((p_9 \and p_2) \or p_7) \rightarrow p_8) \\
\neg((p_5 \rightarrow (p_7 \or p_2)) \leftrightarrow (((p_9 \and p_2) \or p_7) \rightarrow p_8)) \\
(\neg (p_5 \rightarrow (p_7 \or p_2)) \and (((p_9 \and p_2) \or p_7) \rightarrow p_8)) \or ((p_5 \rightarrow(p_7 \or p_2)) \and \neg (((p_9 \and p_2) \or p_7) \rightarrow p_8)) \\
((p_5 \and \neg(p_7\or p_2)) \and (((p_9 \and p_2) \or p_7) \rightarrow p_8))  \or ((p_5 \rightarrow (p_7 \or p_2)) \and \neg ((p_9 \and p_2) \or p_7) \or p_8) \\
((p_5 \and \neg p_7 \and \neg p_2) \and (((p_9 \and p_2) \or p_7) \rightarrow p_8)) \or ((p_5 \rightarrow (p_7 \or p_2)) \and (\neg(p_9 \and p_2) \and \neg p_7) \or p_8) \\
\Big((p_5 \and \neg p_7 \and \neg p_2) \and \Big(\big((p_9 \and p_2) \or p_7 \big) \rightarrow p_8\Big)\Big) \or \Big(\big(p_5 \rightarrow (p_7 \or p_2)\big) \and \big((\neg p_9 \or \neg p_2) \and \neg p_7\big) \or p_8\Big) \quad \blacksquare
$$



***

## 5. Recuerde la definición de fórmula de primer orden vista en clase (puede consultarla al final de esta tarea). Proponga un lenguaje de primer orden y con él realice lo siguiente.

* Dé tres ejemplos de una fórmula en donde use al menos un cuantificador y al menos tres conectivos
  $$
  \begin{split}
  &f_0^1(x) := x \text { es ave} \\
  &f^1_2(x) := x \text { puede volar} \\
  &f^1_3(x) := x \text { tiene plumas} \\
  &f^1_4(x) := x \text { es ovíparo} \\
  &f^1_5(x) := x \text { es omnívoro} \\
  &f^1_6(x) := x \text { tiene pico} \\
  &f^1_7(x) := x \text { es terrestre} \\
  &f^1_8(x) := x \text { puede nadar} \\
  &f^1_9(x) := x \text { es acuático} \\
  \end{split}
  $$
  Existe un animal que es un ave terrestre tiene plumas pero no puede volar.
  $$
  \exist x \ (f^1_0(x)\and f^1_7(x)\and f^1_3(x)\and \neg f_2^1(x))
  $$
  Un animal es un ave si y sólo si  es ovíparo tiene pico y plumas.
  $$
  \forall x f_0^1 (x) \leftrightarrow (f_4^1(x) \and f_6^1(x) \and f_3^1(x))
  $$
   Todas las aves o son acuáticas o terrestres si es acuática entonces puede nadar.
  $$
  \forall x f_0^1(x)\and (f^1_9(x)\or f^1_7(x)) \and (f^1_9(x) \rightarrow f_2^1(x))
  $$
  
* Dé dos ejemplos de una expresión que no es fórmula de primer orden
  $$
  \text Los \ f_0^1(x) = \text{ vuelan}
  $$

  $$
  ¿\exist x, f_0^1(x) \neg f_1^1(x)?
  $$

  

***

## 6. En las siguientes fórmulas $A_1^1(x)$ significa $x$ es una persona, $A^2_1(x_1,x_2)$ significa $x_1$  odia a $x_2$ . Traduzca las siguientes fórmulas al lenguaje natural.

*Algunas personas odian a todas las personas*
$$
((\exist x_1 )A_1^1 (x_1) \and ((\forall x_2)A_1^1 (x_2) \rightarrow A^2_1 (x_1 , x_2 ))) \\
$$

*Existen personas que odian a las personas que se odian a ellas mismas*
$$
((\exist x_1 )A_1^1 (x_1) \and ((\forall x_2)A_1^1 (x_2) \rightarrow (A^2_1 (x_1 , x_2 ) \leftrightarrow A^2_1 (x_2, x_2 ))))
$$


***

## 7. Para las fórmulas del inciso anterior, dé un ejemplo de un universo y un conjunto de personas en la relación indicada que las haga verdaderas, y otro que las haga falsas.

$$
\text{Animales} = \{gato, pero\} \quad
\text{Personas} = \{Juan, Pedro\} \quad
\text {Universo} = \{P, A\} \\
$$

Verdaderos
$$
x_1 , x_2 \in \text{Personas}\\
x_1:= \text{Juan} \quad x_2:= \text{Pedro} \\

((\exist x_1 )A_1^1 (x_1) \and ((\forall x_2)A_1^1 (x_2) \rightarrow A^2_1 (x_1 , x_2 ))) \\
((\exist x_1 )A_1^1 (x_1) \and ((\forall x_2)A_1^1 (x_2) \rightarrow (A^2_1 (x_1 , x_2 ) \iff A^2_1 (x_2, x_2 ))))
$$
Falso 
$$
x_1 , x_2 \in \text{Animales}\\

x_1:= \text{Gato} \quad x_2:= \text{Perro} \\

((\exist x_1 )A_1^1 (x_1) \and ((\forall x_2)A_1^1 (x_2) \rightarrow A^2_1 (x_1 , x_2 ))) \\
((\exist x_1 )A_1^1 (x_1) \and ((\forall x_2)A_1^1 (x_2) \rightarrow (A^2_1 (x_1 , x_2 ) \leftrightarrow A^2_1 (x_2, x_2 ))))
$$

***

## 8. Para las siguientes proposiciones, dé un lenguaje de primer orden para su traducción

* Una persona que posee todas las virtudes es una persona virtuosa, pero hay personas virtuosas que no poseen todas las virtudes.
  $$
  A_0^1(x):= x \text{ es persona} \quad A_1^1(x):= x \text{ es virtud} \quad  A_2^2(x,y):= x \text{ tiene } y \quad  A_3^1(x):= x \text{ es virtuoso}  \\
  \Big(\exist x_1A_0^1(x)\and \big(\forall y_1A^1_1(y_1) \and A_2^2(x_1,y_1) \rightarrow A_3^1(x_1)\big ) \Big) \and \Big( \exist x_2 A_0^1(x_2)\and A_3^1(x_2) \and \neg(\forall y_2 A^1_1(y_2) \and A^2_2(x_2,y_2)) \Big) \quad \blacksquare
  $$
  
* Cada cual tiene algún atributo no usual
  $$
  A_0^2(x, y):= x \text{ tiene un } y  \quad A_1^1(x): = x \text{ es usual}\\
  
  \forall x\Big(\exist y\big(\neg A_1^1(y)\and A_0^2(x,y)\big)\Big) \quad \blacksquare
  $$
  
* Pancho Villa tenía todos los atributos de un gran general
  $$
  A_1^1(x):= x \text{ es Pancho Villa} \quad A_2^2(x,y):= x \text{ tiene } y \quad A_3^1(x):= x \text{ es atributo de general} \\
  \exist x A^1_1(x)\and \big(\forall y A^1_3(y) \and A_2^2(x,y) \big) \quad \blacksquare
  $$
  
* Si los círculos son elipses, entonces los círculos tienen todas las propiedades de las elipses
  $$
  A_0^1(x):= x \text{ es círculo} \quad 
  A_1^1(x):= x \text{ es elipse} \quad 
  A_2^2(x, y):= x \text{ tiene } y \quad 
  A_3^1(x):= x \text{ es una propiedad} \\
  \exist xA^1_0(x)\and A^1_1(x) \rightarrow (\forall y A_3^1(y)\and A_2^2(x,y)) \quad \blacksquare
  $$
  

***

## 9. Para las siguientes fórmulas, presenta una fórmula equivalente en la quge la negación afecte sólo a fórmulas atómicas.

$$
\neg(((\forall x_1 )A ^1_0 (x_3 ) \and A^1_1 (x_1 )) \rightarrow ((\exist x_2 )A^1_0 (x_2) \leftrightarrow A^1_1 (x_2 ))) \\
((\forall x_1) A^1_0(x_3) \and A^1_1(x_1)) \and \neg ((\exist x_2) A^1_0(x_2) \leftrightarrow A^1_1(x_2)) \\
((\forall x_1) A^1_0(x_3) \and A^1_1(x_1)) \and \neg ((\exist x_2) A^1_0(x_2) \leftrightarrow A^1_1(x_2)) \\
((\forall x_1)A^1_0(x_3)\and A^1_1(x_1)) \and \neg ((\exist x_2) A^1_0(x_2)) \and A^1_1(x_2) \or (\exist x_2 A^1_0)) \and \neg A^1_1(x_2) \\
((\forall x_1)A^1_0(x_3)\and A^1_1(x_1)) \and (\neg \exist x_2 A ^1_0(x_2 ) \or \neg A^1_1(x_2) \or ((\exist x_2 A^1_0(x_2)) \and \neg A^1_1(x_2))) \\
\big(\forall x_1 A^1_0(x_3)\and A_1^1(x_1) \big) \and \Big( \big(\forall x_2 \neg A^1_0(x_2) \or \neg A_1^1(x_2)\big) \or \big((\exist x_2 A^1_0(x_2)) \and \neg A^1_1(x_2) \big)\Big) \quad \blacksquare
$$

***

$$
\neg((\forall x_1 )((\exist x_2 )(A^ 2_0 (x_ 1 , x_ 2 ) \leftrightarrow A ^1_0 (x_ 1 )) \rightarrow (\exist x_ 4 )(\forall x_ 3 )A^ 2_0 (x_ 3 , x_ 4 ))) \\
(\exist x_1) \neg ((\exist x_2)( A ^2_0(x_1,x_2) \leftrightarrow A^1_0(x_1)) \rightarrow (\exist x_4) (\forall x_3) A^2_0(x_3,x_4)) \\
(\exist x_1)((\exist x_2)(A^2_0(x_1,x_2) \leftrightarrow A^1_0(x_1))) \and \neg (\exist x_4)(\forall x_3)A_0^2(x_3,x_4)  \\

(\exist x_1)((\exist x_2)(A^2_0(x_1,x_2) \leftrightarrow A^1_0(x_1))) \and (\forall x_4)\neg(\forall x_3)A_0^2(x_3,x_4)  \\

(\exist x_1)((\exist x_2)(A^2_0(x_1,x_2) \leftrightarrow A^1_0(x_1))) \and (\forall x_4)(\exist x_3)\neg A_0^2(x_3,x_4) \quad \blacksquare
$$

***

$$
\neg((\exist x_0 )A^ 1_1 (x_ 0 ) \rightarrow ((\forall x_ 1 )A^ 2_0 (x_ 1 , x_ 0 ) \and A^ 2_0 (x_ 0 , x_ 1 ))) \\
(\exist x_0) A^1_1(x_0)\and \neg((\forall x_1)A^2_0(x_1,x_0)\and A_0^2(x_0, x_1)) \\
(\exist x_0) A_1^1(x_0) \and (\neg(\forall x_1)A_0^2(x_1,x_0)\or \neg A_0^2(x_0,x_1)) \\
(\exist x_0)A^1_1(x_0) \and ((\exist x_0) \neg A^2_0(x_1,x_0)\or \neg A^2_0(x_0,x_1)) \quad \blacksquare
$$

***