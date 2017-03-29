directory = '/Users/jinzhu/Google Drive/2017 spring/APC/Sharon/Asus result/unknown_item_asus/';
testdir = [directory 'test.txt'];
filelist = textread(testdir, '%s', -1);

for i = 1: size(filelist,1)
    filename = filelist{i,1};
    mask = load([directory 'output_unknown/out_' filename '.jpg.mat']);
    BW = mask.cdata;
    BW = BW>0.5;
    [r,c]=size(BW);
    im = imread([directory 'unknownitem/' filename '.jpg']);
    im =imresize(im, [r NaN]);
    BW =im2uint8(BW);
    BW = repmat(BW,[1 1 3]);
    %imshow(im+BW);
    output_file_name = [directory 'mask/' filename '.jpg'];
    imwrite(im+BW,output_file_name);
    

end