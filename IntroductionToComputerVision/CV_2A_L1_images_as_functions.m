% import image and display
img = imread('tree.jpg');
imshow(img);

% load the image package
pkg load image;

% size of 3 channel image
disp(size(img));

% red channel extraction
img_red = img(:, :, 1);
imshow(img_red);
plot(img_red(80, :));

% convert to grayscale
gry = rgb2gray(img);

% size and class of image
disp(size(img));
disp(class(img));

% extract intensities from image
disp(gry(50, 100));
plot(gry(50, :));

% cropping image by slicing
disp(gry(101:103, 201:203));

% change brightness
function result = scale(image, value)
  result = image .* value;
endfunction

imshow(scale(img, 2));
imshow(scale(img, 0.5));

% import test images
img_1 = imread('cycle.jpeg');
img_2 = imread('tree.jpg');

min_h = min(size(img_1)(1), size(img_2)(1));
min_w = min(size(img_1)(2), size(img_2)(2));

img_1 = img_1(1:min_h, 1:min_w, :);
img_2 = img_2(1:min_h, 1:min_w, :);

% add images
imshow(img_1 + img_2);
imshow(img_1./2 + img_2./2);

% alpha blending
function result = blend(image_1, image_2, alpha)
  result = alpha .* image_1 + (1-alpha) .* image_2;
endfunction

imshow(blend(img_1, img_2, 0.75));
imshow(blend(img_1, img_2, 0.25));

% difference of images
imshow(img_1 - img_2);
imshow(img_2 - img_1);
imshow(img_1 - img_2 + img_2 - img_1);

imshow(imabsdiff(img_1, img_2));

% adding noise to image
imshow(imnoise(gry, 'salt & pepper', 0.1));
imshow(imnoise(gry, 'gaussian'));

noise = randn(size(gry)) .* 200;
imshow(gry + noise);

% plotting randn
noise = randn([1, 1000000]);
[n, x] = hist(noise, linspace(-5, 5, 50));
plot(x, n);
title('plot of randn function');
xlabel('x');
ylabel('n');
print -djpg randn-plot.jpg

