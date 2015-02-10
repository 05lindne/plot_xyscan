% scan_color_plot.m
% makes a 2D color encoded of a scan (confocal...)
% needs:	file containing measured value (level) for each pixel
% output:	color encoded 2D plot with color bar


clear all;
close all;

% set input folder
myFolder = '/mnt/Daten/measurements/CVD/RD02-14/140808/';

%data from measurements
baseFileName = 'scan_xy-05_APD1'
dataInFileName = [baseFileName, '.txt']
% dataInFileName = [ dataBaseFileName, '.dat']
dataFileIn=dlmread(fullfile(myFolder, dataInFileName), '\t');

% find smallest value of data to set display range
min_value = min( dataFileIn(:) );
value = dataFileIn - min_value;



hFigure = figure; 
pcolor(value);   
% imagesc(value);

colormap(jet(64));
view(2);  
axis square; %shading interp;
set(gca,'fontsize',16) %fontsize of axis numbers

titleFileName = strrep(dataInFileName, '_', '\_');
title( ['XY Scan (', titleFileName, ')'], 'Fontsize', 20 )

xlabel(texlabel('X-axis (pixel)'),'fontsize',20); 
ylabel(texlabel('Y-axis (pixel)'),'fontsize',20); 
colorbar('EastOutside');  


set(gca, 'CLim', [0, max(dataFileIn(:) )], 'FontSize', 14);
% set(gca, 'CLim', [0, 6000], 'FontSize', 14); % expand midrange color resolution ...
%													by mapping low values to the first color 
%													and high values to the last color in the colormap 
%													by specifying color value limits  


% customize color bar?
% set(hColorbar, 'YTick', [ 1.74655, 2.29702, 2.69838, 2.984, 3.1787]);
% set(hColorbar,'YTickLabel',{'1','5','10', '15', '19.3');


% Save as pdf or eps (Because a file name is specified, the figure will be printed to a file.)
% plotFileName = [myFolder, baseFileName, '.pdf']
% print(hFigure, '-dpdf','-r600', plotFileName)% save as pdf
plotFileName = [myFolder, baseFileName, '.eps']
print(hFigure, '-dpsc ','-r1200', plotFileName)% save as eps


