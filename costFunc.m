function f = cost(x, a1, a2, b1, b2, c1, c2)

anorm = cross(a1,a2);
bnorm = cross(b1,b2);
cnorm = cross(c1,c2);

f = dot(x, anorm).^2 + dot(x, bnorm).^2 + dot(x, cnorm).^2 + (norm(x) - 1).^2;