function ax = aceleracionx(x,y,a,b)
    ax = -((x-a)/((x-a)^2+(y-b)^2)^1.5);
end
function ay = aceleraciony(x,y,a,b)
    ay = -((y-b)/((x-a)^2+(y-b)^2)^1.5);
end
clear, clf, hold off; n=0;
% Constantes del Sistema
%M_sol = 1.9885e30;
M_sol = 1; %1 masa de sol
%g_sol = 274;
g_sol = 1; %1 gravedad del sol
%R=0.7e9;
R=1; % 1 radio del sol
h=1; tfin=16000;
GM = M_sol*g_sol;
a = 0;
b = 0;
th2 = 0:0.01:2*pi;
xunit2 = a + 1 * cos(th2);
yunit2 = b + 1 * sin(th2);
hold on;
plot(xunit2, yunit2, 'g');
    % Condiciones iniciales
    x=-458.33079; y=2665.95683; vx=0.090026; vy=-0.304333;px(1)=x; py(1)=y; n=0;
    for t=0:h:tfin
        ax=(aceleracionx(x,y,a,b)*GM)/R^2; ay=(aceleraciony(x,y,a,b)*GM)/R^2;
        vx = vx + ax*h; x = x + vx*h;
        vy = vy + ay*h; y = y + vy*h;
        px(n+1) = x; py(n+1) = y; n=n+1;
    end
    plot(px,py);
    grid on;
xlim([-3000 3000]);
ylim([-3000 3000]);
