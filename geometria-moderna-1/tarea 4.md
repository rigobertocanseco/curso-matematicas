# Teorema de Ceva
### 1. Pruebe que las medianas de un triángulo son concurrentes
![](/home/rigoberto/Im%C3%A1genes/Captura%20de%20pantalla%20de%202020-09-06%2018-06-47.png)  

Tenemos el trángulo **ABC** y las rectas medianas que concurren en el punto **O**.  
Por el teorema de Ceva tenemos que tres cenevas **AD**, **BH** y **CG** que son las medianas son concurrentes en un punto **O** si y solo si.
$$
 \frac{AG}{GB} \cdot \frac{BD}{DC} \cdot \frac{CH}{HA} = 1
$$

Demostración  

Trazamos una paralela al segmento **BC** que pase por el punto **A**.
![](/home/rigoberto/Im%C3%A1genes/Captura%20de%20pantalla%20de%202020-09-06%2018-05-29.png)

Sea **I**, **J** las intersecciones de **CG** y **BH**, respectivamente. 

Se tiene que:  

* El triángulo **BOD** y el triángulo **AOJ** son semejantes ya que las rectas **BC** y **IJ** son paralelas cortadas por la transversal **AD** por lo tanto $$\frac{BD}{DO} = \frac{JA}{AO} \space(1)$$ 
* De igual manera el triángulo **COD** y el triángulo **AOI** son semejantes por lo tanto $$\frac{OD}{CD} = \frac{OA}{AI} \space(2)$$
* El triángulo **CHB** y el triángulo **AHJ** son semejantes ya que las rectas **BC** y **IJ** son paralelas cortadas por la transversal **AC**  por lo tanto $$\frac{CH}{HA}  = \frac{BC}{JA} \space(3)$$
* El triángulo **BGC** y el triángulo **AGI** son semejantes ya que las rectas **BC** y **IJ** son paralelas cortadas por la transversal **AB**  por lo tanto $$\frac{AG}{GB} = \frac{AI}{BC} \space(4)$$

Multiplicando **(1), (2), (3) y (4)**
$$ 
\frac{BD}{DO} \cdot \frac{OD}{CD} \cdot \frac{CH}{HA} \cdot \frac{AG}{GB} = \frac{JA}{AO} \cdot \frac{OA}{AI} \cdot \frac{BC}{JA} \cdot \frac{AI}{BC} = 1 
$$
$$
\frac{BD}{CD}  \cdot \frac{CH}{HA} \cdot \frac{AG}{GB} = 1
$$

Como los puntos **D**. **G** y **H** son los puntos medios de los segmentos **BC**, **AB** y **AC**, respectivamente tenemos que   **BD = CD**, **CH = HA** y **AG = GB** 

Por lo tanto las medianas **AD**, **BH** y **CG** del triángulo **ABC** concurren en el punto **O**.

### 2. Pruebe que las alturas de un triángulo son concurrentes.
![](/home/rigoberto/Im%C3%A1genes/Captura%20de%20pantalla%20de%202020-09-06%2018-53-47.png)

Tenemos el siguiente triángulo **ABC** y las alturas **AF**, **BG** y **CE** que concurren en el punto **O**.

Demostración

Los triángulos **BGC** y **AFC** son semejantes por ángulo-ángulo-ángulo, por lo tanto
$$
\frac{CG}{FC} = \frac{BC}{AC} \space (1)
$$ 

Los triángulos **BEC** y **BAF** son semejantes  por ángulo-ángulo-ángulo, por lo tanto
$$
\frac{BF}{EB} = \frac{AB}{BC} \space (2)
$$

Los triángulos **ABG** y **AEC** son semejantes  por ángulo-ángulo-ángulo, por lo tanto
$$
\frac{AE}{AG} = \frac{CA}{AB} \space (3)
$$

Multiplicando **(1), (2), (3)** tenemos 
$$
\frac{CG}{FC} \cdot \frac{BF}{EB} \cdot \frac{AE}{AG}  = \frac{BC}{AC} \cdot  \frac{AB}{BC} \cdot \frac{CA}{AB}  = 1 \space (4)
$$

Además por el teorema de Ceva aplicado a el triángulo **ABC** 
$$
 \frac{AE}{EB} \cdot \frac{BF}{FC} \cdot \frac{CG}{GA} = 1 \space (5)
$$

Por **(4) y (5)**, tenemos que  
$$
\frac{CG}{FC} \cdot \frac{BF}{EB} \cdot \frac{AE}{AG} = \frac{AE}{EB} \cdot \frac{BF}{FC} \cdot \frac{CG}{GA} = 1
$$

Por lo tanto, las alturas AF, BG y CE son concurrentes.

### 3. Demuestre que AD es una bisectriz de ángulo en la figura siguiente
sustituyendo 