%CODE FOR FALLING BALL WITH NOISY DATA

clf, clear, clc

%IMPORT DATA FROM FILE
tred = readmatrix('treddata_use.txt');
hnoise = readmatrix('hnoisedata_use.txt');

%PERFORM CURVE FITTING AND RESIDUAL ANALYSIS

pballcoeffs = polyfit(tred,hnoise,12); % fit a quadratic polynomial to the noisy data
pballvals = polyval(pballcoeffs, tred); %store the values of the fitted polynomial
resid = hnoise - pballvals; %compute the residual

%plot the data and fitted curve
figure(1)
grid on
hold on

scatter(tred,hnoise,'ro','LineWidth',2)
plot(tred, pballvals, 'b', 'LineWidth', 2)

xlabel('Time $t$', 'Interpreter','latex', 'FontSize',14)
%ylabel('$h(t)$', 'Interpreter','latex', 'FontSize',14)
legend('Fall Data', 'Fitted Curve', 'Interpreter','latex', 'FontSize',14, 'Location', 'best')

hold off

%plot the residuals
figure(2)

scatter(tred, resid, 'ko', 'LineWidth', 2)
grid on

xlabel('Time $t$', 'Interpreter','latex', 'FontSize',14)
ylabel('Residuals', 'Interpreter','latex', 'FontSize',14)
