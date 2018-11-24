filename = 'beast.csv';
M = csvread(filename);
plot(M(:,2),M(:,3),'-', 'Color', 'k');

grid on;
grid minor;
box off;
hold on;

plot(5, 5, '*', 'Color', 'r');
plot(0, 0, '*', 'Color', 'b');

xx = xlabel('x (m)'); % x-axis label
y = ylabel('y (m)'); % y-axis label

ax = gca;
axis([-1 6 -1 6]);