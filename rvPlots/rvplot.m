%% Gumbel

clear all;
output = containers.Map()

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
f(1,i)=a1*z1*exp(-z1);
f(2,i)=a2*exp(-a2*(x(i)-b2))*exp(-exp(-a2*(x(i)-b2)));
f(3,i)=a3*exp(-a3*(x(i)-b3))*exp(-exp(-a3*(x(i)-b3)));
f(4,i)=a4*exp(-a4*(x(i)-b4))*exp(-exp(-a4*(x(i)-b4)));
end

l = ["$\\alpha = 0.5$ \n $\\beta = 0.5$","$\\alpha = 0.5$ \n $\\beta = 1.0$", "$\\alpha = 0.33$ \n $\\beta = 1.5$", "$\\alpha = 0.25$ \n $\\beta = 3.0$"]

% plot(x,f1,x,f2,x,f3,x,f4)


output('Gumbel') = containers.Map({'x','y','l'},{x,f,l});

% title("Gumbel Distribution")
% xlabel("x")
% ylabel("Probability Density Function")
% legend("alpha = 0.5, beta = 0.5","alpha = 0.5, beta = 1.0","alpha = 0.33, beta = 1.5","alpha = 0.25, beta = 3.0")
% grid
% saveas(gcf,'gumbel.png')

%% Lognormal %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear x f;

x=[0:.1:10]
u1=5
s1=1
square_zeta1=log(s1^2/u1^2 + 1);
zeta1 = sqrt(square_zeta1);
lambda1 = log(u1)-square_zeta1/2.0;

u2=6
s2=.5
square_zeta2=log(s2^2/u2^2 + 1);
zeta2 = sqrt(square_zeta2);
lambda2 = log(u2)-square_zeta2/2.0;

for i=1:101
	f(1,i)=1.0/(sqrt(2*pi)*zeta1*x(i))*exp(-(.5*((log(x(i))-lambda1)/zeta1)^2));
	f(2,i)=1.0/(sqrt(2*pi)*zeta2*x(i))*exp(-(.5*((log(x(i))-lambda2)/zeta2)^2));
end


% plot(x,f1, x, f2)
l = ["$\\mu = 5.0$ \n $\\sigma = 1.0$", "$\\mu = 6.0$ \n $\\sigma = 0.5$"];

output('Lognormal') = containers.Map({'x','y','l'},{x,f,l});
% title("Lognormal Distribution")
% xlabel("x")
% ylabel("Probability Density Function")
% legend("mean = 5.0, std. dev = 1.0", "mean = 6.0, std. dev = 0.5")
% grid
% saveas(gcf,'lognormal.png')

%% Uniform %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear x f;

x=[0:.1:10]
U1=10
L1=0

for i=1:101
	f(i)=1.0/(U1-L1)
end


% plot(x,f1)
l = ["$U_b = 10.0$ \n $L_b = 0.0$"];
output("Uniform") = containers.Map({'x','y', 'l'},{x,f,l});
% xlabel("x")
% ylabel("f(x)")
% legend("Ub = 10.0, Lb = 0.0")
% grid
% ylim([0,.2])

%% Weibull
clear x f;

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
f(1,i)=(k1/l1)*((x(i)/l1)^(k1-1))*exp(-((x(i)/l1)^k1));
f(2,i)=(k2/l2)*((x(i)/l2)^(k2-1))*exp(-((x(i)/l2)^k2));
f(3,i)=(k3/l3)*((x(i)/l3)^(k3-1))*exp(-((x(i)/l3)^k3));
f(4,i)=(k4/l4)*((x(i)/l4)^(k4-1))*exp(-((x(i)/l4)^k4));
end


% plot(x,f1,x,f2,x,f3,x,f4)
l = ["$k = 2.0$ \n $\\lambda = 1.0$", "$k = 2.0$ \n $\\lambda = 2.0$","$k = 1.0$ \n $\\lambda = 2.0$", "$k = 0.5$ \n $\\lambda = 2.0$"]

output("Weibull") = containers.Map({'x','y','l'},{x,f,l});
% xlabel("x")
% ylabel("Probability Density Function")
% legend("shape = 2.0, scale = 1.0", "shape = 2.0, scale = 2.0","shape = 1.0, scale = 2.0", "shape = 0.5, scale = 2.0")
% grid
% saveas(gcf,'weibull.png')
delete 'rvplot.json';
jsonout = jsonencode(output);
fid = fopen('rvplot.json','wt');
fprintf(fid, jsonout);
fclose(fid);
fclose all
