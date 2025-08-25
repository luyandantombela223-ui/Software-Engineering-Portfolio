% Main Script: simple_bisection.m
% Bisection method to find root of x^2 - x = 0 and save the function plot

clc;
clear;

% Initial interval
x_L = -1;
x_R = 0.5;

% Tolerance and maximum iterations
tol = 1e-6;
max_iter = 50;

% Header for output
fprintf(' Iter |     x_L     |     x_R     |     x_M     |   f(x_L)   |   f(x_R)   |   f(x_M)   \n');
fprintf('----------------------------------------------------------------------------------------\n');

for iter = 1:max_iter
    x_M = (x_L + x_R) / 2;
    
    fL = fx(x_L);
    fR = fx(x_R);
    fM = fx(x_M);
    
    % Print current iteration's data
    fprintf(' %4d | %11.6f | %11.6f | %11.6f | %10.6f | %10.6f | %10.6f \n', ...
        iter, x_L, x_R, x_M, fL, fR, fM);
    
    % Check for convergence
    if abs(fM) < tol || (x_R - x_L)/2 < tol %uses short-circuit OR
        break;
    end
    
    % Check which endpoint, x_R or x_L needs to change
    if fL * fM < 0
        x_R = x_M;
    else
        x_L = x_M;
    end
end

fprintf('\nApproximate root found at x = %.6f after %d iterations.\n', x_M, iter);

% Plotting
x_vals = linspace(-1, 0.5, 500);
y_vals = arrayfun(@fx, x_vals);

figure; % Make a new figure
plot(x_vals, y_vals, 'b-', 'LineWidth', 2);
hold on;
plot(x_M, fx(x_M), 'ro', 'MarkerSize', 10, 'MarkerFaceColor', 'r');
yline(0, '--k');
grid on;
xlabel('x');
ylabel('f(x)');
title('Bisection Method: f(x) = x^2 - x');
legend('f(x)', 'Approximate Root', 'Location', 'best')

% Save the figure
%saveas(gcf, 'bisection_plot.png');  % Save as PNG
saveas(gcf, 'bisection_plot.pdf');  % Save as PDF

% Function Definition for f(x) = 0
function y = fx(x)
    y = x^2 - x;
end