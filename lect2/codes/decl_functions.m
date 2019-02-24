clc;
function [res] = square(n)
  res = n * n;
end
function [res] = add(vec_d)
  sum_d = 0.0;
  for e=vec_d
    sum_d += square(e);
  end
  res = sum_d;
end
disp(add([1, 2, 3, 4]));