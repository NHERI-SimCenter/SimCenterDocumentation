$$
f_Z(z) = \int_{-\infin}^{\infin} f_{XY}(x,y) \left| \dfrac{dz}{dy}\right|^{-1}dx
$$
$$
f_Z(z) = \int_{-\infin}^{\infin} f_{XY}(x,y^{(1)}) \left| \dfrac{dz}{dy}\right|^{-1}dx +\int_{-\infin}^{\infin} f_{XY}(x,y^{(2)}) \left| \dfrac{dz}{dy}\right|^{-1}dx
$$
Because the random variables of this problem are assumed to be statistically independent, the joint PDF $p_{XY}$

The analytic solution is first obtained by integrating the Rosenbrock function with respect to $x$ and $y$ as follows:
    
$$\int g(x,y)dx = -\frac{1}{3}\left(a-x\right)^3+b\left(-\frac{1}{3}x^5+\frac{8x^5}{15}-\frac{2}{3}yx^3+y^2x\right)+C$$

$$\int g(x,y)dy = a^2y-2axy+x^2y+bx^4y-bx^2y^2+\frac{by^3}{3}+C$$

$$\int_Ag(x,y) dA = Cy+b\left(\frac{8x^5}{15}y-\frac{1}{3}x^5y+\frac{xy^3}{3}-\frac{x^3y^2}{3}\right)-\left(a-x\right)^3\frac{1}{3}y+C$$

$$
y^{(1)}=x^2+i\sqrt{\frac{a^2+x^2-z-2ax}{b}},\\
y^{(2)}=x^2-i\sqrt{\frac{a^2+x^2-z-2ax}{b}}
$$

$$\dfrac{dg}{dy}=2b\left(y-x^2\right)$$

### Jointly Normal

<!-- $$f_{XY}(x, y)=\frac{1}{2 \pi \sigma_{1} \sigma_{2} \sqrt{1-\rho^{2}}}\exp{\left(-\frac{1}{2(1-\rho)^{2}}\left[\left(\frac{x-\mu_{1}}{\sigma_{1}}\right)^{2}-2 \rho\left(\frac{x-\mu_{1}}{\sigma_{1}}\right)\left(\frac{y-\mu_{2}}{\sigma_{2}}\right)+\left(\frac{y-\mu_{2}}{\sigma_{2}}\right)^{2}\right]\right)}$$ -->

$$f_{XY}(x, y)=\frac{1}{2 \pi \sigma_{1} \sigma_{2}}\exp{\left(-\frac{1}{2}\left[\left(\frac{x-\mu_{1}}{\sigma_{1}}\right)^{2}+\left(\frac{y-\mu_{2}}{\sigma_{2}}\right)^{2}\right]\right)}$$

$$f_{XY}(x, y)=\frac{1}{2 \pi \sigma_{1} \sigma_{2}}\exp{\left(-\frac{1}{2}\left[\left(\frac{x-\mu_{1}}{\sigma_{1}}\right)^{2}+\left(\frac{y-\mu_{2}}{\sigma_{2}}\right)^{2}\right]\right)}$$
