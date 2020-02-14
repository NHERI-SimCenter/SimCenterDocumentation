clear all;

x=[0:.1:10]
U1=10
L1=0

for i=1:101
	f1(i)=1.0/(U1-L1)
end


plot(x,f1)
title("Uniform Distribution")
xlabel("x")
ylabel("f(x)")
legend("Ub = 10.0, Lb = 0.0")
grid
ylim([0,.2])
