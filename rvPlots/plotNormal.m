clear all;

x=[0:.1:10]
u1=5
s1=1
u2=6
s2=.5

for i=1:101
   f1(i)=1.0/(sqrt(2*pi)*s1)*exp(-(.5*((x(i)-u1)/s1)^2));
   f2(i)=1.0/(sqrt(2*pi)*s2)*exp(-(.5*((x(i)-u2)/s2)^2));
end



plot(x,f1, x, f2)
title("Normal Distribution")
xlabel("x")
ylabel("Probability Density Function")
legend("mean = 5.0, std. dev = 1.0", "mean = 6.0, std. dev = 0.5")
grid
saveas(gcf,'normal.png')
