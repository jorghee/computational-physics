clear; clf; close all;

% Base parameters
m1 = 1; m2 = 1; m3 = 1; % masses (kg)
h = 0.01;              % integration step (s)
tfin = 50;             % final time (s)

% Initial conditions
x0 = 1;  vx0 = 2.36;
y0 = 1;  vy0 = 0.0;
z0 = 1;  vz0 = 0.0;

% Acceleration functions
function ax = acel_x(x, k1, m1)
    ax = -(k1 / m1) * x;
end

function ay = acel_y(y, k2, m2)
    ay = -(k2 / m2) * y;
end

function az = acel_z(z, k3, m3)
    az = -(k3 / m3) * z;
end

% Frequency triples (l, n, p)
casos = [
    1, 2, 1;  % (a)
    1, 3, 1;  % (b)
    2, 3, 1;  % (c)
    3, 4, 1;  % (d)
    3, 5, 2;  % (e)
    4, 5, 3;  % (f)
    5, 6, 4   % (g)
];

num_casos = size(casos, 1);

% Prepare figure with 3D subplots
figure('Name', 'Figuras de Lissajous 3D', 'NumberTitle', 'off');
tiledlayout(3, 3, 'TileSpacing', 'compact', 'Padding', 'compact');

for idx = 1:num_casos
    l = casos(idx, 1);
    n = casos(idx, 2);
    p = casos(idx, 3);

    k1 = l^2;  % m1 = 1
    k2 = n^2;  % m2 = 1
    k3 = p^2;  % m3 = 1

    % Storage arrays
    N = round(tfin / h) + 1;
    px = zeros(1, N); py = zeros(1, N); pz = zeros(1, N);

    % Initial state
    x = x0; vx = vx0;
    y = y0; vy = vy0;
    z = z0; vz = vz0;
    px(1) = x; py(1) = y; pz(1) = z;

    n_step = 1;
    for t = h:h:tfin
        % Accelerations
        ax_val = acel_x(x, k1, m1);
        ay_val = acel_y(y, k2, m2);
        az_val = acel_z(z, k3, m3);

        % Euler-Cromer update
        vx = vx + ax_val * h;
        x  = x  + vx * h;
        vy = vy + ay_val * h;
        y  = y  + vy * h;
        vz = vz + az_val * h;
        z  = z  + vz * h;

        n_step = n_step + 1;
        px(n_step) = x; py(n_step) = y; pz(n_step) = z;
    end

    % Trim arrays
    px = px(1:n_step); py = py(1:n_step); pz = pz(1:n_step);

    % 3D plot in a subplot
    nexttile;
    plot3(px, py, pz, 'b-', 'LineWidth', 0.8);
    xlabel('x'); ylabel('y'); zlabel('z');
    title(sprintf('l=%d, n=%d, p=%d', l, n, p));
    grid on;
    view(30, 30);
    axis equal;
end

sgtitle('Curvas de Lissajous en tres dimensiones');
