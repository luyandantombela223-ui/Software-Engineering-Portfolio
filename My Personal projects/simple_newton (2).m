% Filename: simple_newton.m
clc;
clear;

% Initial guess, tolerance and max iterations
x = -0.5;
tol = 1e-11;
max_iter = 50;

fprintf(' Iter |   x_n   \n');
fprintf('-------------------\n');
fprintf(' %4d | %10.9f\n', 0, x); % Print the initial guess

% Iterate Newton's Method
for iter = 1 : max_iter

    fx = f(x); % Evaluate f(x)
    dfx = df(x); % Evaluate f'(x)
    
    x_n = x - fx / dfx; % Newton's Method formula
    
    fprintf(' %4d | %10.9f\n', iter, x_n); % Print the subsequent approximations
    
    %Check for convergence
    if abs(x_n - x) < tol || abs(f(x_n)) < tol
        break;
    end
    
    x = x_n; % Store the "next" value we calculated as the new "current" value
end

fprintf('\nApproximate root found at x = %.6f after %d iterations.\n', x_n, iter);

% Plotting
x_vals = linspace(-1, 0.5, 500);
y_vals = arrayfun(@f, x_vals);

figure;
plot(x_vals, y_vals, 'b-', 'LineWidth', 2);
hold on;
plot(x_n, f(x_n), 'ro', 'MarkerSize', 10, 'MarkerFaceColor', 'r');
yline(0, '--k');
grid on;
xlabel('x');
ylabel('f(x)');
title('Newton''s Method: f(x) = x^2 - x');
legend('f(x)', 'Approximate Root', 'Location', 'best');

% Save the image produced directly to a file as either PNG or PDF
%saveas(gcf, 'newton_plot.png');
%saveas(gcf, 'newton_plot.pdf');

% Function definitions
function y = f(x)
    y = x^2 - x;
end

function dy = df(x)
    dy = 2*x - 1;
end
