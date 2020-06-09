clear all;

x=[0:.1:10]
u1=5
s1=1
square_zeta1=log(s1^2/u1^2 + 1);
zeta1 = sqrt(square_zeta1);
lambda1 = log(u1)-square_zeta1/2.0;

u2=6
s2=.5
u2=2
s2=2
square_zeta2=log(s2^2/u2^2 + 1);
zeta2 = sqrt(square_zeta2);
lambda2 = log(u2)-square_zeta2/2.0;

for i=1:101
	f1(i)=1.0/(sqrt(2*pi)*zeta1*x(i))*exp(-(.5*((log(x(i))-lambda1)/zeta1)^2));
	f2(i)=1.0/(sqrt(2*pi)*zeta2*x(i))*exp(-(.5*((log(x(i))-lambda2)/zeta2)^2));
end


plot(x,f1, x, f2)
title("Lognormal Distribution")
xlabel("x")
ylabel("Probability Density Function")
legend("mean = 5.0, std. dev = 1.0", "mean = 2.0, std. dev = 2.0")
grid
saveas(gcf,'lognormal.png')
