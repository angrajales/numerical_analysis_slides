clc;
f = fopen("input.txt", 'r');
data = fread(f);
disp((data(2) - "0"));
fclose(f);