clear all;

x=[0:.1:10]
a1=.5
b1=.5
l1 = 0
u1 = 10

a2=5
b2=1
l2 = 0
u2 = 10

a3=1
b3=3
l3 = 0
u3 = 10

a4=2
b4=2
l4 = 0
u4 = 10

a5=2
b5=5
l5 = 0
u5 = 10


for i=1:101
   f1(i)=gamma(a1+b1)*(x(i)-l1)^(a1-1)*(u1-x(i))^(b1-1)/(gamma(a1)*gamma(b1)*(u1-l1)^(a1+b1-1))
   f2(i)=gamma(a2+b2)*(x(i)-l2)^(a2-1)*(u2-x(i))^(b2-1)/(gamma(a2)*gamma(b2)*(u2-l2)^(a2+b2-1))
   f3(i)=gamma(a3+b3)*(x(i)-l3)^(a3-1)*(u3-x(i))^(b3-1)/(gamma(a3)*gamma(b3)*(u3-l3)^(a3+b3-1))
   f4(i)=gamma(a4+b4)*(x(i)-l4)^(a4-1)*(u4-x(i))^(b4-1)/(gamma(a4)*gamma(b4)*(u4-l4)^(a4+b4-1))
   f5(i)=gamma(a5+b5)*(x(i)-l5)^(a5-1)*(u5-x(i))^(b5-1)/(gamma(a5)*gamma(b5)*(u5-l5)^(a5+b5-1))
end



	plot(x,f1, x, f2, x, f3, x, f4, x, f5)
title("Beta Distribution (lower bound=0, upper bound = 10)")
xlabel("x")
ylabel("Probability Density Function")
	legend("a=.5, b=.5", "a=5, b=1", "a=1, b=3", "a=2, b=2", "a=2, b=5")
grid
saveas(gcf,'beta.png')
