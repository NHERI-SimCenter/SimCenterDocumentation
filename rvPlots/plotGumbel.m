clear all;

x=[-5:.1:25];


a1=0.5;
b1=0.5;
a2=0.5;
b2=1.0;
a3=1/3;
b3=1.5;
a4=1/4;
b4=3.0;



numSteps = size(x,2);
for i=1:numSteps
z1 = exp(-a1*(x(i)-b1));
f1(i)=a1*z1*exp(-z1);
f2(i)=a2*exp(-a2*(x(i)-b2))*exp(-exp(-a2*(x(i)-b2)));
f3(i)=a3*exp(-a3*(x(i)-b3))*exp(-exp(-a3*(x(i)-b3)));
f4(i)=a4*exp(-a4*(x(i)-b4))*exp(-exp(-a4*(x(i)-b4)));
end


plot(x,f1,x,f2,x,f3,x,f4)


title("Gumbel Distribution")
xlabel("x")
ylabel("Probability Density Function")
legend("alpha = 0.5, beta = 0.5","alpha = 0.5, beta = 1.0","alpha = 0.33, beta = 1.5","alpha = 0.25, beta = 3.0")
grid
saveas(gcf,'gumbel.png')
