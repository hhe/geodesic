function p = interpGreatCircle(p0, p1, t)

theta = acos(dot(p0, p1));
p = sin((1-t)*theta)/sin(theta).*p0 + sin(t*theta)/sin(theta).*p1;
