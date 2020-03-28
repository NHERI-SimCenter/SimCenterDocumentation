clear all;

x=[0:.1:10]


k1=2
l1=1
k2=2
l2=2
k3=1
l3=2
k4=.5
l4=2

for i=1:101
f1(i)=(k1/l1)*((x(i)/l1)^(k1-1))*exp(-((x(i)/l1)^k1));
f2(i)=(k2/l2)*((x(i)/l2)^(k2-1))*exp(-((x(i)/l2)^k2));
f3(i)=(k3/l3)*((x(i)/l3)^(k3-1))*exp(-((x(i)/l3)^k3));
f4(i)=(k4/l4)*((x(i)/l4)^(k4-1))*exp(-((x(i)/l4)^k4));

end


plot(x,f1,x,f2,x,f3,x,f4)
title("Weibull Distribution")
xlabel("x")
ylabel("Probability Density Function")
legend("shape = 2.0, scale = 1.0", "shape = 2.0, scale = 2.0","shape = 1.0, scale = 2.0", "shape = 0.5, scale = 2.0")
grid
saveas(gcf,'weibull.png')
