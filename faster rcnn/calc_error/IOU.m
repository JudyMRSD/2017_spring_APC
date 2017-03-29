fileID = fopen('1_7.txt','r');

%read xmin, ymin, xmax, ymax 
%sizeA = [1 Inf];
%bbx = zeros(1,4);
%str='';
%score= 0 ;
[str count]=fscanf(fileID,'%s %s')
[bbx(1,1),bbx(1,2),bbx(1,3),bbx(1,4),score]=fscanf(fileID,'%f %f %f %f %f');
bbx





%{


%}
%{
x = 1:1:5;
y = [x;rand(1,5)];
fileID = fopen('nums2.txt','w');
fprintf(fileID,'%d %4.4f\n',y);
fclose(fileID);

type nums2.txt
fileID = fopen('nums2.txt','r');

formatSpec = '%d %f';
sizeA = [2 Inf];


A = fscanf(fileID,formatSpec,sizeA)
fclose(fileID);
%}

