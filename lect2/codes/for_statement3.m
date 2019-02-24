clc;
n = int32(input(""));
disp(n);
iters = 1:2:n;
for i = iters
  printf("%d\n", i);
end