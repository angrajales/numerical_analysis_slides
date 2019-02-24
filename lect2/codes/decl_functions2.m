clc;
function [res err] = taylorSin(x, niter);
  result = 0.0;
  for i=0:niter;
    den = factorial(2 * i + 1);
    num = (-1) ^ i;
    mult = (x) ^ (2 * i + 1);
    result = result + (num / den) * mult;
  endfor
  res = result;
end
disp(taylorSin(1/2, 100));