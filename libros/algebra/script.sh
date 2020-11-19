#!/bin/bash
for number in 02 03 04 05 06 07 08 09 10 11 12 13 14 
do 
echo $number
wget 'https://docencia.dim.uchile.cl/algebra/material/presentacion_semana/Semana'$number'_print.pdf'
done 
exit 0
