f = @(x,y)  sqrt( (x - 1)*(2 - y))+1;
range = linspace (-80, 80, 41);
[X, Y] = meshgrid (range, range);
Z = f (X, Y);
surf (X, Y, Z);