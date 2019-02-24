clc;
function [res] = matmul(A, B)
  [m1, n1] = size(A);
  [m2, n2] = size(B);
  result = zeros([int32(n1), int32(m2)]);
  for i=1:m1
    for j=1:n2
      for k=1:m1
        result(i, j) += A(i, k) * B(k, j);
      end
    end
  end
  res = result;
end
disp(matmul([[1, 2]; [3, 4]], [[7, 5]; [4, 3]]));